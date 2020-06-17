from azure.cli.core import get_default_cli as az
import random
import global_variables

def create_windows_server():
    lab_name = global_variables.lab_name
    number_winserv_vms = int(global_variables.winserv_vms)
    password = str(global_variables.password_vms)
    for i in range(0, number_winserv_vms):
        random_number = random.randrange(21, 30)
        vm_name = f'{lab_name}19{random_number}'
        az().invoke(['vm', 'create', '-n', vm_name, '-g', lab_name, '--image', 'MicrosoftWindowsServer:WindowsServer:2019-Datacenter:latest', '--vnet-name', f'{lab_name}vnet', '--subnet', f'{lab_name}windowsserver', '--nsg', f'{lab_name}windowsservernsg', '--admin-username', f'{lab_name}User', '--admin-password', password])
#        print(f'Credentials for Windows10 is: {lab_name}User and Password is {password}')