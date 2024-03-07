from simple_chalk import chalk
from email_bomber import ebombingwin
from sms_bomber import smsbombingwin
from whatsapp_bomber import wpbombingwin
from instagram_bomber import igbombingwin
import sys

Bomber = """
            ▄████████  ▄█        ▄█             ▄█  ███▄▄▄▄         ▄██████▄  ███▄▄▄▄      ▄████████ 
           ███    ███ ███       ███            ███  ███▀▀▀██▄      ███    ███ ███▀▀▀██▄   ███    ███ 
           ███    ███ ███       ███            ███▌ ███   ███      ███    ███ ███   ███   ███    █▀  
           ███    ███ ███       ███            ███▌ ███   ███      ███    ███ ███   ███  ▄███▄▄▄     
         ▀███████████ ███       ███            ███▌ ███   ███      ███    ███ ███   ███ ▀▀███▀▀▀     
           ███    ███ ███       ███            ███  ███   ███      ███    ███ ███   ███   ███    █▄  
           ███    ███ ███▌    ▄ ███▌    ▄      ███  ███   ███      ███    ███ ███   ███   ███    ███ 
           ███    █▀  █████▄▄██ █████▄▄██      █▀    ▀█   █▀        ▀██████▀   ▀█   █▀    ██████████ 
                      ▀         ▀                                                                    
                ▀█████████▄   ▄██████▄    ▄▄▄▄███▄▄▄▄   ▀█████████▄     ▄████████    ▄████████    
                  ███    ███ ███    ███ ▄██▀▀▀███▀▀▀██▄   ███    ███   ███    ███   ███    ███    
                  ███    ███ ███    ███ ███   ███   ███   ███    ███   ███    █▀    ███    ███    
                 ▄███▄▄▄██▀  ███    ███ ███   ███   ███  ▄███▄▄▄██▀   ▄███▄▄▄      ▄███▄▄▄▄██▀    
                ▀▀███▀▀▀██▄  ███    ███ ███   ███   ███ ▀▀███▀▀▀██▄  ▀▀███▀▀▀     ▀▀███▀▀▀▀▀       
                  ███    ██▄ ███    ███ ███   ███   ███   ███    ██▄   ███    █▄  ▀███████████    
                  ███    ███ ███    ███ ███   ███   ███   ███    ███   ███    ███   ███    ███    
                ▄█████████▀   ▀██████▀   ▀█   ███   █▀  ▄█████████▀    ██████████   ███    ███    
                                                                                    ███    ███    
"""

Creds = """
                                ************************************************  
                                *   All In One Bomber - By NocturnalCompiler   * 
                                *            Version 2.0.0 (Stable)            *       
                                *         Discord : fyodor_dostoyevsky.        *      
                                ************************************************                                     

"""

Options = """
    |-TYPE---------------------|
    | [1] - Email Bomber       |
    | [2] - SMS Bomber         |
    | [3] - WhatsApp Bomber    |
    | [4] - Instagram Bomber   |
    | [5] - Exit               |
    |--------------------------|"""

print(chalk.yellow.bold(Bomber))
print(chalk.cyanBright(Creds))
print(chalk.red.bold("                              Please use this tool for educational purpose only.                            "))
print(chalk.red.bold("                      Github : https://github.com/Nocturnal-Compiler/Better-Email-Bomber                  "))
print('\n')
print(chalk.green.bold(Options))
opt = int(input(chalk.blue.bold("    |-> Enter the option number : ")))

if opt == 1:
    ebombingwin()

elif opt == 2:
    smsbombingwin()

elif opt == 3:
    wpbombingwin()

elif opt == 4:
    igbombingwin()
