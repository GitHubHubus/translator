#!/usr/bin/env python

import os
import sys
import requests

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
 print('-i - Interactive mode. Exit from this mode by enter in command line "\exit"')
 print('-r - Revert input/output language (without flag en -> ru and with ru -> en)')

def getUrl(lg):
 return 'https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&dt=t&dt=bd&dj=1&tl=' + lg + '&ie=UTF-8&oe=UTF-8&text='

def main():
 input = sys.argv
 language = 'en' if '-r' in input else 'ru'

 if '-i' in input:
  url = getUrl(language)
  while True:
   if not translate(url):
    break
 elif '-h' in input or '--help' in input:
  getHelp()
 else:
  translate(getUrl(language))

main()
