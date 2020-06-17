from azure.cli.core import get_default_cli as az
import random
import global_variables

def create_windows10():
    lab_name = global_variables.lab_name
    number_win10_vms = int(global_variables.win10_vms)
    password = str(global_variables.password_vms)
    for i in range(0, number_win10_vms):
        random_number = random.randrange(10, 20)
        vm_name = f'{lab_name}10{random_number}'
        az().invoke(['vm', 'create', '-n', vm_name, '-g', lab_name, '--image', 'MicrosoftWindowsDesktop:Windows-10:20h1-pron-g2:19041.264.2005110456', '--vnet-name', f'{lab_name}vnet', '--subnet', f'{lab_name}windows10', '--nsg', f'{lab_name}windows10nsg', '--admin-username', f'{lab_name}User', '--admin-password', password])
#        print(f'Credentials for Windows10 is: {lab_name}User and Password is {password}')
