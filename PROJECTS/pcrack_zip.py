import zipfile
from colorama import Fore, init 
import random


logo_design1 = Fore.RED + '''
                      ,____
                      |---.\\
              ___     |    `      ZIP_CRACKER
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

def cp (pwl, obj):
    idx = 0

    with open(pwl, "rb") as file:
        for line in file:
            for word in line.split():
                try:
                    idx += 1
                    obj.extactall(pwd = word)
                    print("password found at line ", idx)
                    print("password is ", word.decode())
                    return True
                except:
                    continue
    return False


pwl = str(input("Path To The 'Password.txt' File : "))

zip = str(input("Zip file : "))

obj = zipfile.ZipFile(zip)

cnt = len(list(open(pwl, "rb")))

print ("There are total", cnt, "Number of passwords to test")

if cp(pwl, obj) == False:
    print("Password is not found in there !")
