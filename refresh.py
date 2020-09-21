import subprocess
import time

SSID = 'ShabanM'

lines = subprocess.check_output('netsh wlan show interfaces').splitlines()
lines = [str(x)[2:-1].strip() for x in lines]

current_net = ''

for i in lines:
    if(i.startswith('SSID')):
        current_net = i.split(':')[1].strip()
    
    if(i.startswith('State')):
        current_state = i.split(':')[1].strip()

print(current_net, current_state)

if(current_state == 'connected' and current_net == SSID):
    cmd = "netsh wlan disconnect";
    k = subprocess.run(cmd, capture_output=True, text=True).stdout
    print(k)
    time.sleep(1)
    cmd = str.format("netsh wlan connect ssid={0}", SSID)
    k = subprocess.run(cmd, capture_output=True, text=True).stdout