from eosDownloader import EOS_DOWNLOADER
from zipfile import ZipFile
from os import system

system(f'PowerShell -Command "Add-Type -AssemblyName PresentationFramework;[System.Windows.MessageBox]::Show(\'Starting EOS Launcher\', \'EOS Launcher\')"')
fileId = '15orxKbmGm4foV5Lpc0RYnz9Imvp3IbWF'
fileName = 'EOS-Client.zip'
downloader = EOS_DOWNLOADER(fileId=fileId, savedFileName=fileName)
downloader.launch()

if not downloader.status:
    system(f'PowerShell -Command "Add-Type -AssemblyName PresentationFramework;[System.Windows.MessageBox]::Show(\'Download Failed!\', \'EOS Launcher\')"')
    exit()
else:
    system(f'PowerShell -Command "Add-Type -AssemblyName PresentationFramework;[System.Windows.MessageBox]::Show(\'Download Successful at D:\\EOSs\\{fileName}\', \'EOS Launcher\')"')
    try:
        with ZipFile(f"D:\\EOSs\\{fileName}") as pack:
            pack.extractall("D:\\EOSs\\")
        system(f'PowerShell -Command "Add-Type -AssemblyName PresentationFramework;[System.Windows.MessageBox]::Show(\'Extracted at D:\\EOSs\\\', \'EOS Launcher\')"')
    except Exception as e:
        system(f'PowerShell -Command "Add-Type -AssemblyName PresentationFramework;[System.Windows.MessageBox]::Show(\'{e}\', \'Error\', \'Ok\', \'Error\')"')
    system(f'PowerShell -Command "Add-Type -AssemblyName PresentationFramework;[System.Windows.MessageBox]::Show(\'Opening EOSClient.exe\')"')
    system("D:\\Coding\\Py\\DriveAPI\\EOSClient.lnk")

    
