import os, socket, sys
import rich
from rich import print
from colorama import Fore, Back, Style
import time

time.sleep(1)
try:
    print("[bold red]PING-TEST | SOCKET-PING[/bold red]")
    ip_ping_type = input(Fore.RED + "[+] METHOD PING: ")

    if ip_ping_type=="PING-TEST":
       ip_check_ping = input(Fore.RED + "[+] IP: ")
       os.system('echo "PING test on: '+ip_check_ping+'" >> ddosed_ips.txt')
       print("[blue]----------------------------------------------------------[/blue]")
       print("[bold white]INFO: [/bold white][red]checking IP for valid[/red]")
       time.sleep(0.2)
       print("[bold white]INFO: [/bold white][red]pinging host "+ip_check_ping+"[/red]")
       print("[blue]----------------------------------------------------------[/blue]")
       time.sleep(1)
       os.system('ping {0}'.format(ip_check_ping))

    elif ip_ping_type=="SOCKET-PING":
         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         ip_ping = input(Fore.RED + "[+] IP: ")
         port = input(Fore.RED + "PORT: ")
         os.system('echo "PING socket on: '+ip_ping+'" >> ddosed_ips.txt')
         print("[blue]----------------------------------------------------------[/blue]")
         print("[bold white]INFO: [/bold white][red]checking IP for valid[/red]")
         time.sleep(0.2)
         print("[bold white]INFO: [/bold white][red]pinging host "+ip_ping+"[/red]")
         print("[blue]----------------------------------------------------------[/blue]")
         time.sleep(1)
         while True:
              try:
                  s.connect(ip_ping, port)
                  print("[white]from local IP sent=socket socket=64-bit HOST [ "+ip_ping+" ] is [/white][bold green]UP[/bold green]")
                  time.sleep(1)
                  s.close()
              except:
                  print("[white]from local IP sent=socket socket=64-bit HOST [ "+ip_ping+" ] is [/white][bold red]DOWN[/bold red]")
                  time.sleep(1)
                  s.close()

except KeyboardInterrupt:
    print("""[yellow]
    Ctrl + C pressed
    [/yellow]""")
    sys.exit()
