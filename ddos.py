import os, socket, random, time, subprocess, threading, sys
from termcolor import colored
import rich
from rich import print
import requests
import webbrowser
import colorama
from colorama import Fore, Back, Style
from time import sleep

time.sleep(2)
subprocess.run('clear' , shell=True)
print("""[bold red]
▄▄▄▄    ▒█████  ▄▄▄█████▓ ███▄    █ ▓█████▄▄▄█████▓
▓█████▄ ▒██▒  ██▒▓  ██▒ ▓▒ ██ ▀█   █ ▓█   ▀▓  ██▒ ▓▒
▒██▒ ▄██▒██░  ██▒▒ ▓██░ ▒░▓██  ▀█ ██▒▒███  ▒ ▓██░ ▒░
▒██░█▀  ▒██   ██░░ ▓██▓ ░ ▓██▒  ▐▌██▒▒▓█  ▄░ ▓██▓ ░ 
░▓█  ▀█▓░ ████▓▒░  ▒██▒ ░ ▒██░   ▓██░░▒████▒ ▒██▒ ░ 
░▒▓███▀▒░ ▒░▒░▒░   ▒ ░░   ░ ▒░   ▒ ▒ ░░ ▒░ ░ ▒ ░░   
▒░▒   ░   ░ ▒ ▒░     ░    ░ ░░   ░ ▒░ ░ ░  ░   ░    
 ░    ░ ░ ░ ░ ▒    ░         ░   ░ ░    ░    ░      
 ░          ░ ░                    ░    ░  ░        
      ░                                             
[/bold red]""")
print("[yellow]version 2.3[/yellow]")
sleep(2)
try:
    print("[bold green][+] connect to internet![/bold green]")
    print("""[bold green]
   ._________________.
   |.---------------.|
   ||               ||
   || connected to  ||
   ||   internet    ||
   ||               ||
   || ready to ddos ||
   ||_______________||
   /.-.-.-.-.-.-.-.-.\ 
  /.-.-.-.-.-.-.-.-.-.\ 
 /.-.-.-.-.-.-.-.-.-.-.\ 
/______/__________\___o_\ 
\_______________________/
    [/bold green]""")
except ConnectionError:
    print("[bold red][+] connection to internet error[/bold red]")
    print("""[bold red]
   ._________________.
   |.---------------.|
   ||               ||
   || not connected ||
   ||  to internet  ||
   ||               ||
   ||check your wifi||
   ||_______________||
   /.-.-.-.-.-.-.-.-.\ 
  /.-.-.-.-.-.-.-.-.-.\ 
 /.-.-.-.-.-.-.-.-.-.-.\ 
/______/__________\___o_\ 
\_______________________/
    [/bold red]""")
    sys.exit()

time.sleep(0.1)
try:
    f = open("ddosed_ips.txt", "r")
    print("[bold yellow][+][/bold yellow][bold red] recent ddosed ip addresses[/bold red]")
    print(f.read())
    print("[blue]----------------------------------------------------------[/blue]")
except FileNotFoundError:
    print("[bold red]File not found making new one[/bold red]")
    nf = open('ddosed_ips.txt', 'w')
    nf.write('NEW FILE ')
    print("[bold green]file saved at [/bold green][blue]/home/kali/botnet/ddosed_ips.txt[/blue]")

print("[bold red]TCP-STRESSER | HTTP-STRESSER[/bold red]")
method = input(Fore.RED + "[+] METHOD: ")
if method=="TCP-STRESSER":
   from modules import ipstresser

elif method=="HTTP-STRESSER":
     from modules import httpstresser
else:
    print("[blue]not a option[/blue]")
