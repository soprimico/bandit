import os
os.system("sudo apt install python3-phonenumbers")
os.system("sudo apt install python3-exifread")
os.system("cls" if os.name == "nt" else "clear")
import time
import random
from colorama import init, Fore, Back, Style
import requests
import exifread


from phonenumbers import carrier, geocoder, timezone
import phonenumbers

def phonefinder():
    numero = input("Número (ej: +34600111222): ")

    try:
        parsed = phonenumbers.parse(numero, None)

        print("\n=== Resultados ===")
        print("Código país:", parsed.country_code)
        print("Número nacional:", parsed.national_number)

        print(
            "Formato internacional:",
            phonenumbers.format_number(
                parsed,
                phonenumbers.PhoneNumberFormat.INTERNATIONAL
            )
        )

        print(
            "Formato E164:",
            phonenumbers.format_number(
                parsed,
                phonenumbers.PhoneNumberFormat.E164
            )
        )

        print("Posible:", phonenumbers.is_possible_number(parsed))
        print("Válido:", phonenumbers.is_valid_number(parsed))

        print(
            "Ubicación:",
            geocoder.description_for_number(parsed, "es")
        )

        print(
            "Operador:",
            carrier.name_for_number(parsed, "es")
        )

        print(
            "Zona horaria:",
            ", ".join(timezone.time_zones_for_number(parsed))
        )

    except Exception as e:
        print("Error:", e)

def image_exif():
    path = input("Image file name (must be in the same folder as this script, e.g. hello.png): ").strip()
    try:
        with open(path, 'rb') as image_file:
            tags = exifread.process_file(image_file)

        print("\n=== EXIF DATA ===")
        if not tags:
            print("No se encontraron datos EXIF.")
        else:
            for tag in tags.keys():
                print(f"{tag}: {tags[tag]}")

    except FileNotFoundError:
        print("file not found! MIGHT BE BECAUSE ITS NOT ON THE SAME FOLDER AS THE SCRIPT!")
    except Exception as e:
        print("Error:", e)

def lookup_ip():
    ip_address = input("Enter a public IP address: ").strip()
    url = f"https://ipwhois.app/json/{ip_address}"

    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        data = resp.json()

        if data.get("success", True):
            print(f"IP: {data.get('ip')}")
            print(f"ISP: {data.get('isp')}")
            print(f"Organization: {data.get('org')}")
            print(f"Country: {data.get('country')}")
            print(f"ASN: {data.get('asn')}")
        else:
            print(f"Lookup failed: {data.get('message', 'Unknown error')}")

    except requests.exceptions.RequestException as e:
        print("Error:", e)

def nmapPersCMD():
    global commando
    global nmapstop
    ip_opala = ""
    commando = input("bandit cmd>: ")
    if commando == "ex1":
        nmapstop = True
        return
    if commando == "start nmap now":
        clear()
        print("Diferent types of attack: (put command: what (number of command) for know what it does): ")
        print("(example: what 1)")
        print("number 1: sudo start nmap attack 1")
    if commando == "what 1":
        print("Scans all TCP ports, detects running services and versions, and provides verbose output.")
    if commando == "sudo start nmap attack 1":
        clear()
        inputip = input("Put here the public or private ip: ")
        ip_opala = inputip
        os.system(f"nmap -Pn -p- -sV -vv {ip_opala}")
    if commando == "help":
        clear()
        print(Fore.GREEN + "Nmap tool! (write ex1 and enter for go back to the tool!)")
        printearesto = "(start nmap now)"
        print(f"Use the command: {printearesto} to start personalized attack.")
        
    os.system(commando)
def evilwinrma():
    global commd
    global evilwinrm
    global nameopalaew
    global passopalaew
    global ipopalaew
    global ipv4ipwmEvilrn1
    global commandevil
    commd = input("bandit cmds>: ")
    if commd == "help":
        print(f"Put the command: {commandevil}")
    if commd == "ex1":
        evilwinrm = True
        return
    if commd == "evilrm start":
        print("Diferent types of attack: (put command: what (number of command) for know what it does): ") 
        print("example: what 1")
        print("number 1: sudo start local evil")
        print("number 2: sudo look ifOpenedPorts True")
    if commd == "sudo start local evil":
        clear()
        nameopalaew = input("put here the pc name: ")
        passopalaew = input("Put here the pc password: ")
        ipopalaew = input("Put here the ip: ")
        clear()
        print("lets start >:3")
        time.sleep(1)
        os.system(f"sudo evil-winrm -i {ipopalaew} -u {nameopalaew} -p '{passopalaew}'")
    if commd == "sudo look ifOpenedPorts True":
        clear()
        print("For looking if the ports of that pc are opened you need to put the ipv4 ip:")
        ipv4ipwmEvilrn1 = input("Private pc ip(ipv4): ")
        os.system(f"sudo nmap -p 5985,5986 {ipv4ipwmEvilrn1}")
    if commd == "what 1":
        print("The first command(number 1 command) is used for acces to other local pc form ur lan")
    if commd == "what 2":
        print("This one is basically for searching the needed ports, if they're opened then it should work perfectly!")
    os.system(commd)
    

bandit_title = """
██████╗░░█████╗░███╗░░██╗██████╗░██╗████████╗
██╔══██╗██╔══██╗████╗░██║██╔══██╗██║╚══██╔══╝
██████╦╝███████║██╔██╗██║██║░░██║██║░░░██║░░░
██╔══██╗██╔══██║██║╚████║██║░░██║██║░░░██║░░░
██████╦╝██║░░██║██║░╚███║██████╔╝██║░░░██║░░░
╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░╚═╝░░░╚═╝░░░"""

start = True
version = 1.03

def clear():
   os.system("cls" if os.name == "nt" else "clear")


def options():
    print("0 return")
    print("1 russian wheel")
    print("2 phone basic info")
    print("3 ip lookup")
    print("4 image exif")
    print("5 nmap (search ports and more on networks)")
    print("6 evil-winrm: Access to pc (like ssh)")
    print("99 exit")

def returning():
    global answer
    global start
    global bstart
    print(Fore.RESET + "Returning")
    time.sleep(1)
    clear()
    start = True
    
        
while True:
    if start == True:
        print(f"Welcome back to BANDIT tool version {version}!")
        bstart = int(input("0 to enter to this tool: "))
        if bstart == 0:
            clear()
            init()
            print(Fore.RED + bandit_title)
            print(Fore.LIGHTRED_EX + Style.BRIGHT + "We're BANDIT")
            print("Who made this: bielicus")
            options()
            answer = int(input("Choose one number and press enter: "))
            if answer == 0:
                returning()
            if answer == 1:
                clear()
                playernum = int(input("Give me number 1 to the one you'll put here: "))
                botnum = random.randint(1,playernum)
                onetonum = int(input(f"Alright, so it will be 1 to {playernum}, choose number 1 to {playernum}: "))
                if botnum == onetonum:
                    print("Bang!")
                    os.system("ip a")
                    os.system("ipconfig")
                else:
                    print("U're safe...")
            if answer == 2:
                clear()
                phonefinder()
            if answer == 3:
                clear()
                lookup_ip()
            if answer == 4:
                clear()
                image_exif()
            if answer == 5:
                clear()
                print("LINUX OS NEEEDED!!!")
                time.sleep(1)
                clear()
                os.system("sudo apt install nmap")
                clear()
                print(Fore.GREEN + "Nmap tool! (write ex1 and enter for go back to the tool!)")
                printearesto = "(start nmap now)"
                print(f"Use the command: {printearesto} to start personalized attack.")
                nmapstop = False
                while not nmapstop:
                    nmapPersCMD()
            if answer == 6:
                clear()
                print("LINUX OS NEEEDED!!!")
                time.sleep(1)
                clear()
                os.system("yes | sudo apt install ruby ruby-dev build-essential")
                os.system("yes | sudo gem install evil-winrm")
                clear()
                print(Fore.GREEN + "Evil-WinRM tool! (write ex1 and enter for go back to the tool!)")
                evilwinrm = False
                commandevil = "evilrm start"
                print(f"Put the command: {commandevil}")
                while not evilwinrm:
                    evilwinrma()

            if answer == 99:
                clear()
                start = False
                break
