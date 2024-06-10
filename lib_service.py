import subprocess

nssm_path = r'C:\automacoes_sem_parar\01\nssm.exe'
executable_file = r'C:\automacoes_sem_parar\01\Service_tester_EXE.exe'
service_name = 'Teste Essias'

def create_service(nssm_path, executable_file, service_name):
    command = [nssm_path, 'install', service_name, executable_file]
    try:
        subprocess.run(command, check=True)
        print("Service created successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error creating the service: {e}")

if __name__ == "__main__":
    create_service(nssm_path, executable_file, service_name)
