from subprocess import call
from termcolor import colored 

call('clear',shell=True)
print("\n")
print('             888        8888888b. 888    8888888888b.  ')
print('             888        888   Y88b888    888888   Y88b ')
print('             888        888    888888    888888    888 ')
print(' 8888b.  .d88888888  888888   d88P8888888888888   d88P ')
print('    "88bd88" 888888  8888888888P" 888    8888888888P"  ')
print('.d888888888  888Y88  88P888       888    888888        ')
print('888  888Y88b 888 Y8bd8P 888       888    888888        ')
print('"Y888888 "Y88888  Y88P  888       888    888888     ')

print("\n")
try:
    interface = input(str("interface [eth0/wlan0] > "))
    if(interface == "eth0"):
        newmac = input(str("MAC address[eth0]> "))
    elif(interface == "wlan0"):
        newmac = input(str("MAC address[wlan0]> "))
    else:
        error = colored("[!] Unknown interface, try again", "white", "on_red", ["bold"])
        print(error)
        exit()
    call(f'ifconfig {interface} down',shell=True)
    call(f'ifconfig {interface} hw ether {newmac}',shell=True)
    call(f'ifconfig {interface} up',shell=True)
    status_color = colored(" [+] MAC address changed successfully ", "white", "on_green", ["bold"])
    print(status_color)
    
except Exception:
    print("[!] There is an error")