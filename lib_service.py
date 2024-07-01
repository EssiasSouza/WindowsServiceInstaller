import subprocess

nssm_path = r'C:\automacoes_sem_parar\01\nssm.exe'
executable_file = r'C:\automacoes_sem_parar\01\Service_tester_EXE.exe'
service_name = 'Teste Essias'

def create_service(nssm_path, executable_file, service_name, install_location):
    command1 = [nssm_path, 'install', service_name, executable_file]
    command2 = [nssm_path, 'set', service_name, 'AppDirectory', install_location]
    command3 = [nssm_path, 'set', service_name, 'AppStdout', install_location + '\stdout.log']
    command4 = [nssm_path, 'set', service_name, 'AppStderr', install_location + '\stderr.log']
    command5 = [nssm_path, 'edit', service_name]
    try:
        subprocess.run(command1, check=True)
        print("Service created successfully!")
        try:
            subprocess.run(command2, check=True)
            print("Directory setup ok!")
            try:
                subprocess.run(command3, check=True)
                print("Log stdout ok!")
                try:
                    subprocess.run(command4, check=True)
                    print("Log stderr ok!")
                    try:
                        subprocess.run(command5, check=True)
                        print("Log edit opened!")
                    except subprocess.CalledProcessError as e:
                        print(f"Error creating the service: {e}")
                except subprocess.CalledProcessError as e:
                    print(f"Error creating the service: {e}")
            except subprocess.CalledProcessError as e:
                print(f"Error creating the service: {e}")
        except subprocess.CalledProcessError as e:
            print(f"Error creating the service: {e}")
    except subprocess.CalledProcessError as e:
        print(f"Error creating the service: {e}")
