import re
import argparse
import os

emails = re.compile(r'[\w\.-]+@[\w\.-]+')
ips = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
urls = re.compile(r'\w{1,20}://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

parser = argparse.ArgumentParser()
parser.add_argument('--email', action="store_true", help= 'extract all emails from target file')
parser.add_argument('--ip', action="store_true", help= 'extract all ip addresses from target file')
parser.add_argument('--url', action="store_true", help= 'extract all urls from target file')
parser.add_argument("filename", help="enter filename to parse")
args = parser.parse_args()

if args.email:
    print("""
Emails:
    """)
    for i, line in enumerate(open(args.filename,'r')):
        for match in re.findall(emails, line):
            print (match)

if args.ip:
    print("""
IP Addresses:
        """)
    for i, line in enumerate(open(args.filename,'r')):
        for match in re.findall(ips, line):
            print (match)

if args.url:
    print("""
URL's:
        """)
    for i, line in enumerate(open(args.filename,'r')):
        for match in re.findall(urls, line):
            print (match)

