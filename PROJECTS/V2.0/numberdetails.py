# pip install phonenumbers.
#pip install colorama
# Credits to "Mr.WhiteHatBAWA".

from colorama import Fore, init 
import random

logo_design1 = Fore.RED + '''
                      ,____
                      |---.\\
              ___     |    `      PDF_CRACKER
             / .-\  ./=)
            |  |"|_/\/|
            ;  |-;| /_|         Reap the cheater !!!
           / \_| |/ \ |
          /      \/\( |
          |   /  |` ) |
          /   \ _/    |
         /--._/  \    |
         `/|)    |    /
           /     |   |
         .'      |   |
        /         \  |
       (_.-.__.__./  /

'''



logo_design2 = Fore.CYAN + '''
    .o oOOOOOOOo                                            OOOo
    Ob.OOOOOOOo  OOOo.      oOOo.                      .adOOOOOOO
    OboO"""""""""""".OOo. .oOOOOOo.    OOOo.oOOOOOo.."""""""""'OO
    OOP.oOOOOOOOOOOO "POOOOOOOOOOOo.   `"OOOOOOOOOP,OOOOOOOOOOOB'
    `O'OOOO'     `OOOOo"OOOOOOOOOOO` .adOOOOOOOOO"oOOO'    `OOOOo
    .OOOO'            `OOOOOOOOOOOOOOOOOOOOOOOOOO'            `OO
    OOOOO                 '"OOOOOOOOOOOOOOOO"`                oOO
   oOOOOOba.                .adOOOOOOOOOOba               .adOOOOo.
  oOOOOOOOOOOOOOba.    .adOOOOOOOOOO@^OOOOOOOba.     .adOOOOOOOOOOOO
 OOOOOOOOOOOOOOOOO.OOOOOOOOOOOOOO"`  '"OOOOOOOOOOOOO.OOOOOOOOOOOOOO
 "OOOO"       "YOoOOOOMOIONODOO"`  .   '"OOROAOPOEOOOoOY"     "OOO"
    Y           'OOOOOOOOOOOOOO: .oOOo. :OOOOOOOOOOO?'         :`
    :            .oO%OOOOOOOOOOo.OOOOOO.oOOOOOOOOOOOO?         .
    .            oOOP"%OOOOOOOOoOOOOOOO?oOOOOO?OOOO"OOo
                 '%o  OOOO"%OOOO%"%OOOOO"OOOOOO"OOO':
                      `$"  `OOOO' `O"Y ' `OOOO'  o             .
    .                  .     OP"          : o     .                     BAWANTHA_MADUSHAN_BELIWATHTHA

'''

banner = random.choice([logo_design1,logo_design2])
print (Fore.YELLOW + banner)

Fore.YELLOW

print("By Mr.WhiteHatBAWA")

print(" ")
print(" ")
print(" ")
import phonenumbers
from phonenumbers import timezone,geocoder,carrier

cont = str(input("You wanna continue (True Or False) :  "))
print("")
print("")
while (cont=="True"):
    pn = str(input("Phone number : "))

    phonenumber = phonenumbers.parse(pn)

    timezone = timezone.time_zones_for_number(phonenumber)
    # You can change these to any language. I'm a Sri Lankan citizen & I used Sinhala. [for English use 'en'].
    Carrier = carrier.name_for_number(phonenumber,'si')

    Region = geocoder.description_for_number(phonenumber, 'si')

    Valid = phonenumbers.is_valid_number(phonenumber)

    Possible = phonenumbers.is_possible_number(phonenumber)

    print("Your phonenumber : " , phonenumber)
    print("timezone : " , timezone)
    print("Carrier : " , Carrier)
    print("Country : " , Region)
    print("Is valid number : " , Valid)
    print("Is possible number : " , Possible)
    print("")
    print("")
    cont = str(input("You wanna continue (True Or False) :  "))
    print("")
    print("")


