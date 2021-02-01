import requests
import urllib3
import json
from base64 import b64encode
from time import sleep
import os
import sys
import urllib.parse
import psutil
import time
import datetime

gamedirs = [r'C:\Riot Games\League of Legends',r'R:\Riot Games\League of Legends', r'D:\Riot Games\League of Legends', r'E:\Riot Games\League of Legends', r'D:\Games\League of Legends', r'E:\Games\League of Legends']

stopWhenMatchStarts = False

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def request(method, path, query='', data=''):
    if not query:
        url = '%s://%s:%s%s' % (protocol, host, port, path)
    else:
        url = '%s://%s:%s%s?%s' % (protocol, host, port, path, query)

    fn = getattr(s, method)

    if not data:
        r = fn(url, verify=False, headers=headers)
    else:
        r = fn(url, verify=False, headers=headers, json=data)

    return r


lockfile = None

while not lockfile:
    for gamedir in gamedirs:
        lockpath = r'%s\lockfile' % gamedir

        if not os.path.isfile(lockpath):
            continue

        print('Found running League of Legends, dir %s' % gamedir)
        lockfile = open(r'%s\lockfile' % gamedir, 'r')

lockdata = lockfile.read()

lockfile.close()

lock = lockdata.split(':')

procname = lock[0]
pid = lock[1]

protocol = lock[4]
host = '127.0.0.1'
port = lock[2]

username = 'riot'
password = lock[3]

userpass = b64encode(bytes('%s:%s' % (username, password), 'utf-8')).decode('ascii')
headers = { 'Authorization': 'Basic %s' % userpass }

s = requests.session()
