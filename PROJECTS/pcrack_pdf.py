import pikepdf 
from tqdm import tqdm
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
passwords = [] 

password_text_file = str(input("Path To The 'Password.txt' File : "))
print(" ")
print(" ")
print(" ")
pdf = str(input("Path to pdf : "))

for line in open(password_text_file): 
    passwords.append(line.strip()) 

print(" ")
print(" ")
print(" ")
for password in tqdm(passwords, "Cracking PDF File"): 

    try: 
        with pikepdf.open(pdf, 
                          password = password) as p: 
            print("[+] Password found:", password) 

            break

    except pikepdf._qpdf.PasswordError as e: 

        continue
