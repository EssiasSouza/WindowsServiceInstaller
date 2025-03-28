import os
import time
from lib_lister import choose_executable
from lib_lister import list_executables
import requests
import zipfile
import shutil
import platform
import struct

def manual_install():
    input("Press ENTER")
    os.system('cls')

def auto_install():
    first_executables = list_executables(".\\")

    if first_executables != []:

        for executable in first_executables:
            
            if executable == ".\\mainWinSCInstaller.exe":
                executable = None
                continue
            elif executable == ".\\main_trx_inspector.exe":
                executable = executable.replace(".\\", "")
                application_name = 'TRX_INSPECTOR'
                print(f'Instalando serviço para a Aplicação TRX Inspector em Concessionária')

            elif executable == ".\\conc_limpa_backup.exe":
                executable = executable.replace(".\\", "")
                application_name = 'CONC_LIMPA_BACKUP'
                print(f'Instalando serviço para a Aplicação CONC_LIMPA_BACKUP em Concessionária')

            else:
                application_name = None
    else:
        application_name = None
        executable = None
    
    return executable, application_name


def first_message():
    os.system('cls')
    print('Starting application')
    print('++++++++++++++++++++++++++++++++++++++++')
    print('++ Welcome to Windows Service Creator ++')
    print('+++++++ REQUIRE ADMIN PRIVILEGES +++++++')
    print('++++++++++++++++++++++++++++++++++++++++')
    time.sleep(2)
    print('This application works easily to create a Windows service with some steps')
    print('This application:')
    print('- Copies all files of your application to the destination folder')
    print('- Checks if there is NSSM file on the current directory')
    print('- Download NSSM file is it doesn`t exists')
    print('- Unzip NSSM file to the current folder')
    print('- Checks the operation system is 64 or 32 bits based')
    print('- Copies NSSM for the operation system base.')
    print('- Create the application as a service')
    time.sleep(2)
    application_name = auto_install()
    return application_name


# Function to download NSSM
def download_nssm(url, save_path):
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print("Download NSSM finished.")
    else:
        print("Error during download.")

# Function to unzip the downloaded file
def unzip_file(save_path, extract_to):
    with zipfile.ZipFile(save_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print("NSSM unzipped successfully.")

# Function to check if NSSM already exists, if not, download and unzip it
def checkNSSMExist(save_path, extract_to, url):
    if not os.path.exists(save_path):
        download_nssm(url, save_path)
    else:
        print(f"{save_path} already downloaded.")

    if not os.path.exists(extract_to):
        unzip_file(save_path, extract_to)
    else:
        print("NSSM package already exists.")

def path_set(install_default):
    current_path = install_default
    install_location = current_path
    print(f"The current installation path is: {install_location}")
    confirmation = input("Is this correct? Type Y(YES) to confirm or N(NO) to change it:\n")
    return install_location, confirmation

def confirm(install_default):
    while True:
        install_location, confirmation = path_set(install_default)
        if confirmation.lower() in {"y", "yes"}:
            break
        else:
            install_default = input("Please type the installation directory below:\n")

    return install_location

# Function to check if the system is 64-bit
def is_64bit_windows():
    return platform.machine().endswith('64') or struct.calcsize("P") * 8 == 64

def create_directory_structure(to_create_path):
    try:
        os.makedirs(to_create_path, exist_ok=True)
        print(f"Directory created successfully: {to_create_path}")
    except Exception as e:
        print(f"Error creating directory: {e}")

def copy_file(source_file, install_location, arch):
    try:
        if os.path.exists(source_file):
            shutil.copy(source_file, install_location)
            print(f"This system is running a Windows {arch}-bit OS.")
            print(f"NSSM {arch}-bit copied to {install_location} successfully.")
            print('-------------------------------------------------------------')
            time.sleep(2)
        else:
            print(f"Source file does not exist: {source_file}")
    except Exception as e:
        print(f"Error copying the file: {e}")

