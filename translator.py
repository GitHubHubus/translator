#!/usr/bin/python

import sys
import requests

url = 'https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&dt=t&dt=bd&dj=1&tl=ru&text='
input = sys.argv 

print(input)

def translate(url):
 sys.stdout.write('> ')
 data = raw_input()

 if data == '\exit':
  return False;

 output = requests.get(url + data).json()

 if 'sentences' in output.keys() and len(output['sentences']) > 0 and  'trans' in output['sentences'][0].keys():
  sys.stdout.write('< ' + output['sentences'][0]['trans'])

 sys.stdout.write('\n')
 return True

def getHelp():
 print('-i - interactive mode')
 print('-h - instruction')

if len(input) < 2:
 translate(url)
elif input[1] == '-i':
 while True:
  if translate(url) == False:
   break
elif input[1] == '-h':
 getHelp()
