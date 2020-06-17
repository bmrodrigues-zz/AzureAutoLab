# AzureAutoLab
Easy and simple way to create Azure Labs for you in a safe environment.

Instalation:
pip install azure-cli

Run:
python main.py

Comments:
If you just want an empty lab, set all VM numbers to 0. A jumpbox will still be created allowing you access to the VM's. Please use ssh port forwarding (EX: ssh -L 33899:192.168.1.4:3389 user@jumpboxpublicip) to access and manage the VMs. You can tweak the NSG's and lab after creation.
