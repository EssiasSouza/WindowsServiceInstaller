import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import lib_copier
import lib_service
import lib_functions
import os

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

executable, application_name = lib_functions.first_message()
url = "https://nssm.cc/release/nssm-2.24.zip"
save_path = "nssm-2.24.zip"
extract_to = "NSSM"

lib_functions.checkNSSMExist(save_path, extract_to, url)

if application_name == None:
    install_default = r"C:\automacoes_sem_parar"

else:
    install_default = f"C:\\automacoes_sem_parar\\{application_name}"
    service_name = application_name

if __name__ == "__main__":
    install_location = lib_functions.confirm(install_default)

if lib_functions.is_64bit_windows():
    arch = 64
    nssm_dir = os.path.join(extract_to, 'nssm-2.24\win64')
    source_file = os.path.join(nssm_dir, 'nssm.exe')
else:
    arch = 32
    nssm_dir = os.path.join(extract_to, 'nssm-2.24\win32')
    source_file = os.path.join(nssm_dir, 'nssm.exe')

os.system('cls')
print(f"Installation location: {install_location}")

lib_functions.create_directory_structure(install_location)
lib_functions.copy_file(source_file, install_location, arch)

source_dir = '.'
dest_dir = install_location
exceptions = ['NSSM', 'nssm-2.24.zip', 'mainWinSCInstaller.exe', 'mainWinSCInstaller.zip', 'mainWinSCInstaller' ]

lib_copier.copy_files(source_dir, dest_dir, exceptions)

dest_dir = install_location

if executable == None: 
    if __name__ == '__main__':
        selected_executable = lib_functions.choose_executable(dest_dir)
        if selected_executable:
            print(f"You selected: {selected_executable}")
        else:
            print("No executable selected.")

    executable_file = f"{install_location}\{selected_executable}"
    service_name = input('\nType the friendly Service Name:\n')
    nssm_path = install_location + f'\\nssm.exe'
    lib_service.create_service(nssm_path, executable_file, service_name, install_location)

else:
    selected_executable = executable
    executable_file = f"{install_location}\{selected_executable}"
    service_name = application_name
    nssm_path = install_location + f'\\nssm.exe'
    lib_service.create_service(nssm_path, executable_file, service_name, install_location)
