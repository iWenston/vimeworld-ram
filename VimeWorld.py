#RAM for VimeWorld

import os, base64

def base64_encode(text):
    return base64.b64encode(bytes(text, 'utf-8')).decode('ascii')


ram = input('Enter RAM amount (example 3G, 3000M): ')
os.system('cmd /d /c start "" /D "%APPDATA%\\.vimeworld" "%APPDATA%\\.vimeworld\\VimeWorld.exe" -home "%APPDATA%\\.vimeworld\\" -jre "%APPDATA%\\.vimeworld\\jre-x64" -jvmargs -Xmx' + ram + ' -XX:+UnlockExperimentalVMOptions -XX:+UseG1GC -jar "launcher.jar" -updater ' + base64_encode(os.getenv('APPDATA') + '\\.vimeworld\\VimeWorld.exe') + ' -appdata ' + base64_encode(os.getenv('APPDATA')))