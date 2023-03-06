import os
import time

REPEAT_INTERVAL = 10

while True:
    command = '''
    PowerShell -Command "Add-Type -AssemblyName PresentationFramework;[System.Windows.MessageBox]::Show('Hey - Drink Water')"
    '''

    os.system(command)
    time.sleep(REPEAT_INTERVAL)