#!/usr/bin/env python

import os
import sys
import requests
import readline

def getFormat(string, color = '\033[92m'):
 return color + string + '\033[0m'

def showSingleWordTranslate(data):
 value = data['terms'] if 'terms' in data else data['trans']

 if type(value) is unicode:
  sys.stdout.write(getFormat('< ' + value))
 else:
  for i in range(0, len(value)):
   sys.stdout.write(getFormat(' ' + str(i + 1) + ') ' + value[i] + '\n', '\033[94m'))

def showTextTranslate(data):
 sys.stdout.write(getFormat('< '))

 for i in range(0, len(data)):
  sys.stdout.write(getFormat(data[i]['trans']))

def translate(url):
 data = raw_input('> ')

 if data == '\exit':
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
 print('-i - Interactive mode. Exit from this mode by enter in command line "\exit"')
 print('-r - Revert input/output language (without flag en -> ru and with ru -> en)')

def getUrl(lg):
 return 'https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&dt=t&dt=bd&dj=1&tl=' + lg + '&ie=UTF-8&oe=UTF-8&text='

def main():
 input = sys.argv
 language = 'en' if '-r' in input else 'ru'
 url = getUrl(language)

 if '-i' in input:
  while True:
   if not translate(url):
    break
 elif '-h' in input or '--help' in input:
  getHelp()
 else:
  translate(url)

main()
