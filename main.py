import global_variables
import core_create
import windows10
import WindowsServer
import LinuxServer
import jumpbox

global_variables.login()
global_variables.lab_name()
global_variables.win10_vms()
global_variables.winserv_vms()
global_variables.linuxserv_vms()
global_variables.password_vms()
global_variables.password_jumpbox()
core_create.create_core()
windows10.create_windows10()
WindowsServer.create_windows_server()
LinuxServer.create_linux_server()
jumpbox.create_jumpbox_server()
print(f'Your VMs credentials are: {global_variables.lab_name}user | {global_variables.password_vms}')
print(f'Your JumpBox credentials are: {global_variables.lab_name}user | {global_variables.password_jumpbox}')
