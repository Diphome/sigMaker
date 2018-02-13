#-*- coding: utf-8 -*-

'''
Enter n desired signatures, a valid one will
be outputed and put into clipboard.
'''

import argparse
from Tkinter import Tk

def base_address_calculator(x):
    x = int(x)
    if x == 32:
      return 8
    elif x == 64:
      return 16
    else:
      raise argparse.ArgumentTypeError("Your process is either 64bits or 32bits.")    

ap = argparse.ArgumentParser()

ap.add_argument("-p", "--perfect", required=False, action='store_true',
  help="If a single bit is not maching in one address, the full address will be convert.")

ap.add_argument("-b", "--base", required=False, type=base_address_calculator, default=8,
  help="Enter 32 or 64 wether your AOB is from 32bits or 64bits process.")

ap.add_argument("-s", "--spaces", required=False, action='store_true',
  help="Outputed signature will have spaces every two characters.")

args = vars(ap.parse_args())

signatures = []

print "\n" + "Enter all your signatures, when done enter a blank line "
sp = "user input"
while sp != "":
    try:
        sp = raw_input("")
    except EOFError:
        break
    signatures.append(sp)

signatures = filter(None,signatures)

if len(signatures) < 2:
    raise ValueError("Enter at least 2 signatures...")

bestSignature = [""] * len(signatures)
bestSignature[0] = signatures[0]

for index, value in enumerate(signatures):
  if index + 1 == len(signatures):
    break
  for x,y in zip(bestSignature[index], signatures[index + 1]):
    if x != y:
      bestSignature[index + 1] += "?"
    else:
      bestSignature[index + 1] += x

if args["perfect"]:
  bestSignatureForced = bestSignature[-1].replace(" ","")
  bestSignatureForced = [bestSignatureForced[i:i+args["base"]] for i in range(0, len(bestSignatureForced), args["base"]) ]
  for index, value in enumerate(bestSignatureForced):
      for v in value:
            if v == '?':
              bestSignatureForced[index] = '?' * args["base"]
              break
  finalSignature = ''.join(bestSignatureForced)
else:
  finalSignature = bestSignature[-1].replace(" ","")

if args["spaces"]:
  finalSignature = " ".join(a+b for a,b in zip(finalSignature[::2], finalSignature[1::2]))

r = Tk()
r.withdraw()
r.clipboard_clear()
r.clipboard_append(finalSignature)

print "\n" + "Crafted signature :"
print finalSignature
print "\n" + "Crafted signature has been put on your clipboard."