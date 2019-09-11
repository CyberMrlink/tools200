#decompiled by MRLINKERRORSYSTEM
import os, sys
print '\x1b[1;33mSudah punya ID dan Password nya?'
print '\x1b[1;32mSilahkan Login '
import os, sys

def wa():
    os.system('xdg-open https://api.whatsapp.com/send?phone=6283847277532&text=Assalamualaikum')


def restart():
    ngulang = sys.executable
    os.execl(ngulang, ngulang, *sys.argv)


user = raw_input('ID: ')
import getpass
sandi = raw_input('Password: ')
if sandi == 'Link' and user == 'Mr':
    print 'Anda Telah Login'
    sys.exit
else:
    print 'Login GAGAL, Silahkan hubungi ADMIN'
    wa()
    restart()
import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib
from multiprocessing.pool import ThreadPool
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
else:
    try:
        import requests
    except ImportError:
        os.system('pip2 install requests')

from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():
    print '\x1b[1;91m[!] Keluar'
    os.sys.exit()


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.1)

