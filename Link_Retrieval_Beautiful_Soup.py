import socket
import sys
import requests
from bs4 import BeautifulSoup

from requests.api import request

print('Hello World!! This program retrieve all the links in a guven URL. Please enter the right information so the program works properly.')

while True:
    try:
        host = input(
            'Enter URL to retrieve links, examples (google.com, amazon.com, london.ca): ')
        schenumber = input('Please press 1 for HTTP or 2 for HTTPS: ')
        if schenumber == '1':
            print('HTTP was selected')
            sche = 'http'
            port = 80
        elif schenumber == '2':
            print('HTTPS was selected')
            sche = 'https'
            port = 443
        else:
            print('Option incorrect!!!')
            continue
        path = input(
            'Indicate the path to analyze (if you do not want to analyze a path, please press ENTER) **** example: /about/ **** : ')
        break
    except OSError:
        print('Incorrect URL')

if path:
    if path[0] != '/':  # user did not write correctly the path
        finalhost = sche + '://' + host + '/' + path
    else:
        finalhost = sche + '://' + host + path
else:
    finalhost = sche + '://' + host

fh2 = sche + '://' + host

print('# Creating socket')
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print('Failed to create socket')
    sys.exit()

print('# Getting remote IP address')
try:
    remote_ip = socket.gethostbyname(host)
except socket.error:
    print('Failed to get IP address')
    sys.exit()

print('# Connecting to server, ' + host +
      ' (' + remote_ip + ') on port: ' + str(port))
s.connect((remote_ip, int(port)))

try:
    reqs = requests.get(finalhost)
except requests.RequestException:
    reqs = requests.get(finalhost)

soup = BeautifulSoup(reqs.text, 'html.parser')

for link in soup.find_all('a'):
    val = str(link.get('href'))
    val2 = ''
    if val[0] == '/':
        val = fh2 + link.get('href')
        if val[0] == 'h':
            val2 = val
        print(val2)

#Explanation: The first thing I did was to ask for a URL to analyze. Then, the script asks for the schema to use (HTTP or HTTPS). 
#Also, this script ask for a path, it is optional. Some validations are done, for instance, if the user does not provide a correct path it is fixed. 
#Using the socket library the IP address of the URL is obtained and using BeautifulSoup the search for links on the given URL is started 
#(if the user provided a path all the link are retrieved from the path). Finally, I did some validations to only show links that starting with 
#the letter h (this letter is the first letter of http or https - I did this because some web pages contains links to "#" or even to phone numbers ¯\_(ツ)_/¯). 
#At the end all the links are printed on the screen.