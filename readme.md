## Service creator application
### Goals
The application goal is install a service easier than download the application NSSM, create folders and etc.
This application checks if the machine has the NSSM application in the target directory and if it doesn't exist, the application download it.

### HOW TO USE?

To use the application please follow the steps below.

- Put the mainWinSCInstaller.exe (Compiled application) in the same directory that is the application wich is going to bem installed as a service on the Windows.
- Exceute the mainWinSCInstaller.exe (This application will be require elevation as an administrator)
- Read the first informations to avoid errors and press ENTER
- Check if the application directory is correct, if no type NO and press ENTER or type YES and press ENTER to continue.
- If you typed NO, you can change the directory path typing the new one.
- If you typed YES, the application will copy all files on the source diretory to the target directory, listing all of EXE files exists on the target directory.
- Choose by number your executable file that will be your service and press ENTER.
- Type your service name and press ENTER.
- Configure your user admin on the NSSM interface to provide permission for your application.
+ NOTE - If your application doesn`t need permission to access a directory or other resource you can jump this step.

Your service should be created.

- Open your CMD
- Type "services.msc" and press ENTER
- Look for your service name and press START.

### TIPS

If your service doesn't run, check some problems with your application. It maybe is wrong or broken.
To check it, you can run it direct on your application accessing the complete path.