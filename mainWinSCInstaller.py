import zipfile
import os
import requests
import shutil
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import platform
import struct
import lib_copier
import lib_service

os.system('cls')
print('Starting application')
print('++++++++++++++++++++++++++++++++++++++++')
print('++ Welcome to Windows Service Creator ++')
print('+++++++ REQUIRE ADMIN PRIVILEGES +++++++')
print('++++++++++++++++++++++++++++++++++++++++')
print('This application works easily to create a Windows service with some steps')

print('This application:')
print('- Copies all files of your application to the destination folder')
print('- Checks if there is NSSM file on the current directory')
print('- Download NSSM file is it doesn`t exists')
print('- Unzip NSSM file to the current folder')
print('- Checks the operation system is 64 or 32 bits based')
print('- Copies NSSM for the operation system base.')
print('- Create the application as a service')
input("Press ENTER")
os.system('cls')

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Function to download NSSM
def download_nssm(url, save_path):
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print("Download NSSM finished.")
    else:
        print("Error during download.")

url = "https://nssm.cc/release/nssm-2.24.zip"
save_path = "nssm-2.24.zip"
extract_to = "NSSM"

# Function to unzip the downloaded file
def unzip_file(save_path, extract_to):
    with zipfile.ZipFile(save_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print("NSSM unzipped successfully.")

# Function to check if NSSM already exists, if not, download and unzip it
def checkNSSMExist(save_path):
    if not os.path.exists(save_path):
        download_nssm(url, save_path)
    else:
        print(f"{save_path} already downloaded.")

    if not os.path.exists(extract_to):
        unzip_file(save_path, extract_to)
    else:
        print("NSSM package already exists.")

checkNSSMExist(save_path)

install_default = r"C:\automacoes_sem_parar"

def path_set(install_default):
    current_path = install_default
    global install_location
    install_location = current_path
    print(f"The current installation path is: {install_location}")
    confirmation = input("Is this correct? Type Y(YES) to confirm or N(NO) to change it:\n")
    return install_location, confirmation

def main(install_default):
    while True:
        install_location, confirmation = path_set(install_default)
        if confirmation.lower() in {"y", "yes"}:
            break
        else:
            install_default = input("Please type the installation directory below:\n")

if __name__ == "__main__":
    main(install_default)

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
        else:
            print(f"Source file does not exist: {source_file}")
    except Exception as e:
        print(f"Error copying the file: {e}")

if is_64bit_windows():
    arch = 64
    nssm_dir = os.path.join(extract_to, 'nssm-2.24\win64')
    source_file = os.path.join(nssm_dir, 'nssm.exe')
else:
    arch = 32
    nssm_dir = os.path.join(extract_to, 'nssm-2.24\win32')
    source_file = os.path.join(nssm_dir, 'nssm.exe')

print(f"Source file path: {source_file}")
print(f"Installation location: {install_location}")

create_directory_structure(install_location)
copy_file(source_file, install_location, arch)

source_dir = '.'
dest_dir = install_location
exceptions = ['NSSM', 'nssm-2.24.zip', 'windows_service_installer.exe']

lib_copier.copy_files(source_dir, dest_dir, exceptions)

executable_file = input('\nType the executable application (app.exe):\n')
service_name = input('\nType the friendly Service Name:\n')
nssm_path = install_location + f'\\nssm.exe'
lib_service.create_service(nssm_path, executable_file, service_name)
