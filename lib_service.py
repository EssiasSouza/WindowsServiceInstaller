import subprocess

def create_service(service_name, display_name, bin_path, start_type="auto", description=""):
    try:
        subprocess.run([
            "sc", "create", service_name,
            "binPath=", bin_path,
            "DisplayName=", display_name,
            "start=", start_type
        ], check=True)
        
        if description:
            subprocess.run([
                "sc", "description", service_name, description
            ], check=True)

        print(f"Service {service_name} created successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to create service {service_name}: {e}")

if __name__ == "__main__":
    service_name = "MyPythonService"
    display_name = "My Python Service"
    bin_path = r"C:\path\to\your\executable.exe"  # Caminho para o executável que o serviço deve rodar
    description = "This is a sample Python-created service"

    create_service(service_name, display_name, bin_path, description=description)
