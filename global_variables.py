from azure.cli.core import get_default_cli as az
import random
import secrets
import string

# Global Variable for the all Lab

def login():
    az().invoke (['login'])

def lab_name():
    global lab_name
    greek_gods = ['aphrodite', 'apollo', 'ares', 'artemis', 'athena', 'demeter', 'dionysus', 'hades', 'hephaestus', 'hera', 'hermes', 'hestia', 'poseidon', 'zeus']
    lab_name = random.choice(greek_gods)

def win10_vms():
    global win10_vms
    win10_vms = input('Number of Windows 10 VMs to create: ')

def winserv_vms():    
    global winserv_vms
    winserv_vms = input('Number of Windows Server VMs to create: ')

def linuxserv_vms():
    global linuxserv_vms
    linuxserv_vms = input('Number of Linux Server VMs to create: ')

def password_vms():
    global password_vms
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password_vms = ''.join(secrets.choice(alphabet) for i in range(12))

def password_jumpbox():
    global password_jumpbox
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password_jumpbox = ''.join(secrets.choice(alphabet) for i in range(12))