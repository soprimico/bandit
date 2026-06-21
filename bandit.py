import os
import time
import random


from phonenumbers import carrier, geocoder, timezone
import phonenumbers

def phonefinder():
    numero = input("Número (ej: +34600111222): ")

    try:
        parsed = phonenumbers.parse(numero, None)

        print("\n=== RESULTADOS ===")
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



bandit_title = """
██████╗░░█████╗░███╗░░██╗██████╗░██╗████████╗
██╔══██╗██╔══██╗████╗░██║██╔══██╗██║╚══██╔══╝
██████╦╝███████║██╔██╗██║██║░░██║██║░░░██║░░░
██╔══██╗██╔══██║██║╚████║██║░░██║██║░░░██║░░░
██████╦╝██║░░██║██║░╚███║██████╔╝██║░░░██║░░░
╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░╚═╝░░░╚═╝░░░"""

start = True
version = 1.02

def clear():
   os.system("cls" if os.name == "nt" else "clear")


def options():
    print("0 return")
    print("1 russian wheel")
    print("2 phone basic info")
    print("99 exit")
    
def returning():
    global answer
    global start
    global bstart
    print("Returning")
    time.sleep(1)
    clear()
    start = True
    
        
while True:
    if start == True:
        print(f"Welcome back to BANDIT tool version {version}!")
        bstart = int(input("0 to enter to this tool: "))
        if bstart == 0:
            clear()
            print(bandit_title)
            print("We're BANDIT")
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

            if answer == 99:
                start = False
                break
        
                
        


