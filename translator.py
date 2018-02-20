#!/usr/bin/env python

import os
import sys
import requests
import readline

def getFormat(string, color = '\033[92m'):
 sys.stdout.write(color + string + '\033[0m')

def showSingleWordTranslate(data):
 value = data['terms'] if 'terms' in data else data['trans']

 if type(value) is unicode:
  getFormat('< ' + value)
 else:
  for i in range(0, len(value)):
   getFormat(' ' + str(i + 1) + ') ' + value[i] + '\n', '\033[94m')

def showTextTranslate(data):
 getFormat('< ')

 for i in range(0, len(data)):
  getFormat(data[i]['trans'])

def translate(url):
 data = raw_input('> ')

 if data == '\quit' or data == '\q':
  return False;

 output = requests.get(url + data).json()

 if 'sentences' in output.keys() and len(output['sentences']) > 0 and  'trans' in output['sentences'][0].keys():
  if ' ' not in data:
   showSingleWordTranslate(output['dict'][0] if 'dict' in output else output['sentences'][0])
  else:
   showTextTranslate(output['sentences'])

 sys.stdout.write('\n')
 return True

def getHelp():
 str = ('-i - Interactive mode. Exit from this mode by enter in command line "\exit" \n' + 
        '-r - Revert input/output language (without flag en -> ru and with ru -> en) \n')
 sys.stdout.write(str)

def getUrl(lg):
 return 'https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&dt=t&dt=bd&dj=1&tl=' + lg + '&ie=UTF-8&oe=UTF-8&text='

def main():
 input = sys.argv
 url = getUrl('en' if '-r' in input else 'ru')

 if '-i' in input:
  while True:
   if not translate(url):
    break
 elif '-h' in input or '--help' in input:
  getHelp()
 else:
  translate(url)

main()
