import zipfile
import os
import requests
import shutil
from requests.packages.urllib3.exceptions import InsecureRequestWarning

print('Starting application')

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def download_nssm(url, save_path):
    response = requests.get(url, verify=False) 
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print("Download finished.")
    else:
        print("Error during download.")
url = "https://nssm.cc/release/nssm-2.24.zip"
save_path = "nssm-2.24.zip"
extract_to = "NSSM"
def unzip_file(save_path, extract_to):
    with zipfile.ZipFile(save_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print("NSSM unzipped succesfully.")

def checkNSSMExist (save_path):
    if not os.path.exists(save_path):
        download_nssm(url, save_path)
    else:
        print(f"{save_path} already was downloaded")
        if not os.path.exists(extract_to):
            unzip_file(save_path, extract_to)
        else:
            print()

checkNSSMExist(save_path)

def path_set():
    current_path = os.getcwd()
    install_location = input(f"The current path is: {current_path}\nPlease type the installation directory below:\n")
    print(f"The application path was defined as: {install_location}")
    confirmation = input("Type Y/N: ")
    return install_location, confirmation

install_location, confirmation = path_set()

while True:
    install_location, confirmation = path_set()
    if confirmation.lower() in {"y", "yes"}:
        break
    print("Let's try again...")




# shutil.copy(install_location):

