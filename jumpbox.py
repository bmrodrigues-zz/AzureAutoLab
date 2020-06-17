from azure.cli.core import get_default_cli as az
import global_variables

def create_jumpbox_server():
    lab_name = global_variables.lab_name
    password = str(global_variables.password_jumpbox)
    vm_name = f'{lab_name}JumpBox'
    az().invoke(['vm', 'create', '-n', vm_name, '-g', lab_name, '--image', 'Canonical:UbuntuServer:18.04-LTS:latest', '--os-disk-size-gb', '500', '--vnet-name', f'{lab_name}vnet', '--subnet', f'{lab_name}jumpbox', '--nsg', f'{lab_name}jumpboxnsg', '--admin-username', f'{lab_name}user', '--admin-password', password])