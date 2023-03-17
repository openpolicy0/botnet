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
print("[yellow]version 2.9[/yellow]")
sleep(2)
try:
    f = open("ddosed_ips.txt", "r")
    print("[bold yellow][+][/bold yellow][bold red] recent ddosed ip addresses[/bold red]")
    print(f.read())
    print("[blue]----------------------------------------------------------[/blue]")
except FileNotFoundError:
    print("[bold red]File not found making new one[/bold red]")
    nf = open('ddosed_ips.txt', 'w')
    nf.write('')
    print("[bold green]file saved at [/bold green][blue]/home/kali/botnet/ddosed_ips.txt[/blue]")

try:
    print("[bold red]TCP-STRESSER | HTTP-STRESSER | PING-HOST[/bold red]")
    method = input(Fore.RED + "[+] METHOD: ")
    if method=="TCP-STRESSER":
       from Modules import ipstresser

    elif method=="HTTP-STRESSER":
         from Modules import httpstresser

    elif method=="PING-HOST":
         from Modules import pinghost

    else:
         print("[blue]not a option[/blue]")

except KeyboardInterrupt:
    print("""[bold red]
[+] EXITING botnet tool
    [/bold red]""")
    sleep(1)
