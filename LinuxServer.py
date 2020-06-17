from azure.cli.core import get_default_cli as az
import random
import global_variables

def create_linux_server():
    lab_name = global_variables.lab_name
    number_linuxserv_vms = int(global_variables.linuxserv_vms)
    password = str(global_variables.password_vms)
    for i in range(0, number_linuxserv_vms):
        random_number = random.randrange(31, 40)
        vm_name = f'{lab_name}18{random_number}'
        az().invoke(['vm', 'create', '-n', vm_name, '-g', lab_name, '--image', 'Canonical:UbuntuServer:18.04-LTS:latest', '--os-disk-size-gb', '200', '--vnet-name', f'{lab_name}vnet', '--subnet', f'{lab_name}linux', '--nsg', f'{lab_name}linuxnsg', '--admin-username', f'{lab_name}user', '--admin-password', password])
#        print(f'Admin username is: {lab_name}user')
