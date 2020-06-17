from azure.cli.core import get_default_cli as az
import global_variables

def create_core():
    lab_name = global_variables.lab_name
    az().invoke(['account', 'list', '--output', 'table'])
    subscription = input('Please select a subscription ID(enter for default): ')
    az().invoke(['group', 'create', '--name', lab_name, '--location', 'eastus'])
    print('{} Resouce Group created'.format(lab_name))
    az().invoke(['network', 'nsg', 'create', '--name', f'{lab_name}windows10nsg', '--resource-group', lab_name])
    az().invoke(['network', 'nsg', 'create', '--name', f'{lab_name}windowsservernsg', '--resource-group', lab_name])
    az().invoke(['network', 'nsg', 'create', '--name', f'{lab_name}linuxnsg', '--resource-group', lab_name])
    az().invoke(['network', 'nsg', 'create', '--name', f'{lab_name}jumpboxnsg', '--resource-group', lab_name])
    az().invoke(['network', 'nsg', 'rule', 'create', '--name', f'{lab_name}rdp', '--resource-group', lab_name, '--nsg-name', f'{lab_name}windows10nsg', '--priority', '400', '--source-address-prefixes', '192.168.4.0/24', '--destination-address-prefixes', 'VirtualNetwork', '--protocol', 'Tcp', '--destination-port-ranges', '3389'])
    az().invoke(['network', 'nsg', 'rule', 'create', '--name', f'{lab_name}rdp', '--resource-group', lab_name, '--nsg-name', f'{lab_name}windowsservernsg', '--priority', '400', '--source-address-prefixes', '192.168.4.0/24', '--destination-address-prefixes', 'VirtualNetwork', '--protocol', 'Tcp', '--destination-port-ranges', '3389'])
    az().invoke(['network', 'nsg', 'rule', 'create', '--name', f'{lab_name}web', '--resource-group', lab_name, '--nsg-name', f'{lab_name}windowsservernsg', '--priority', '498', '--source-address-prefixes', 'Internet', '--destination-address-prefixes', 'VirtualNetwork', '--protocol', 'Tcp', '--destination-port-ranges', '80'])
    az().invoke(['network', 'nsg', 'rule', 'create', '--name', f'{lab_name}webs', '--resource-group', lab_name, '--nsg-name', f'{lab_name}windowsservernsg', '--priority', '497', '--source-address-prefixes', 'Internet', '--destination-address-prefixes', 'VirtualNetwork', '--protocol', 'Tcp', '--destination-port-ranges', '443'])
    az().invoke(['network', 'nsg', 'rule', 'create', '--name', f'{lab_name}ssh', '--resource-group', lab_name, '--nsg-name', f'{lab_name}linuxnsg', '--priority', '400', '--source-address-prefixes', '192.168.4.0/24', '--destination-address-prefixes', 'VirtualNetwork', '--protocol', 'Tcp', '--destination-port-ranges', '22'])
    az().invoke(['network', 'nsg', 'rule', 'create', '--name', f'{lab_name}web', '--resource-group', lab_name, '--nsg-name', f'{lab_name}linuxnsg', '--priority', '498', '--source-address-prefixes', 'Internet', '--destination-address-prefixes', 'VirtualNetwork', '--protocol', 'Tcp', '--destination-port-ranges', '80'])
    az().invoke(['network', 'nsg', 'rule', 'create', '--name', f'{lab_name}webs', '--resource-group', lab_name, '--nsg-name', f'{lab_name}linuxnsg', '--priority', '497', '--source-address-prefixes', 'Internet', '--destination-address-prefixes', 'VirtualNetwork', '--protocol', 'Tcp', '--destination-port-ranges', '443'])
    az().invoke(['network', 'nsg', 'rule', 'create', '--name', f'{lab_name}ssh', '--resource-group', lab_name, '--nsg-name', f'{lab_name}jumpboxnsg', '--priority', '100', '--source-address-prefixes', 'Internet', '--destination-address-prefixes', 'VirtualNetwork', '--protocol', 'Tcp', '--destination-port-ranges', '22'])
    az().invoke(['network', 'vnet', 'create', '--name', f'{lab_name}vnet', '--resource-group', lab_name, '--address-prefixes', '192.168.0.0/16'])
    az().invoke(['network', 'vnet', 'subnet', 'create', '--vnet-name', f'{lab_name}vnet', '--resource-group', lab_name, '--name', f'{lab_name}windows10', '--address-prefixes', '192.168.1.0/24', '--network-security-group', f'{lab_name}windows10nsg'])
    az().invoke(['network', 'vnet', 'subnet', 'create', '--vnet-name', f'{lab_name}vnet', '--resource-group', lab_name, '--name', f'{lab_name}windowsserver', '--address-prefixes', '192.168.2.0/24', '--network-security-group', f'{lab_name}windowsservernsg'])
    az().invoke(['network', 'vnet','subnet', 'create', '--vnet-name', f'{lab_name}vnet' , '--resource-group', lab_name, '--name', f'{lab_name}linux', '--address-prefixes', '192.168.3.0/24', '--network-security-group', f'{lab_name}linuxnsg'])
    az().invoke(['network', 'vnet','subnet', 'create', '--vnet-name', f'{lab_name}vnet' , '--resource-group', lab_name, '--name', f'{lab_name}jumpbox', '--address-prefixes', '192.168.4.0/24', '--network-security-group', f'{lab_name}jumpboxnsg'])
    