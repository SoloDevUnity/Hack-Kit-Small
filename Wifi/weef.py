import subprocess
import os

def run_command(command):
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    return result.stdout.strip()

#get script directory
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "wificreds.txt")

#get wifi SSID
wifi_output = run_command('netsh wlan show interfaces')
wifi_name = ""

for line in wifi_output.split("\n"):
    if "SSID" in line and "BSSID" not in line:
        wifi_name = line.split(":")[-1].strip()
        break

if not wifi_name:
    print("No Wi-FI connection found")
    exit()

#check if profile exists
profile_output = run_command("netsh wlan show profile")
if wifi_name not in profile_output:
    print(f"Profile '{wifi_name}' not found")
    exit()

#extract password
wifi_password_info = run_command(f'netsh wlan show profile "{wifi_name}" key=clear')

#save to file
with open(file_path, "w", encoding="utf-8") as file:
    file.write(wifi_password_info)

#open notepad
subprocess.run(f'notepad.exe "{file_path}"', shell=True)

print(f"Wi-Fi credentials saved to {file_path}")