from simple_chalk import chalk
from email_bomber import ebombingwin
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
    print(chalk.red.bold("SMS Bomber is under development. Please try again later."))
    sys.exit()

elif opt == 3:
    print(chalk.red.bold("WhatsApp Bomber is under development. Please try again later."))
    sys.exit()

elif opt == 4:
    print(chalk.red.bold("Instagram Bomber is under development. Please try again later."))
    sys.exit()
