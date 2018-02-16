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
 print('-i - Interactive mode')
 print('-h - Instruction')
 print('-l - Inverse language')

def inverseLanguage():
 os.environ['TRANS_OL'], os.environ['TRANS_IL'] = os.getenv('TRANS_IL'), os.getenv('TRANS_OL')
 print('Input language: ' + os.getenv('TRANS_IL'))
 print('Output language: ' + os.getenv('TRANS_OL'))

def getUrl():
 return 'https://translate.googleapis.com/translate_a/single?client=gtx&sl=' + os.getenv('TRANS_IL') + '&dt=t&dt=bd&dj=1&tl=' + os.getenv('TRANS_OL') + '&ie=UTF-8&oe=UTF-8&text='


def init():
 if not os.getenv('TRANS_IL') or not os.getenv('TRANS_OL'):
  os.environ['TRANS_IL'] = 'en'
  os.environ['TRANS_OL'] = 'ru'

def main():
 init()
 input = sys.argv

 if len(input) < 2:
  translate(getUrl())
 elif input[1] == '-i':
  url = getUrl()
  while True:
   if translate(url) == False:
    break
 elif input[1] == '-h':
  getHelp()
 elif input[1] == '-l':
  inverseLanguage()

main()
