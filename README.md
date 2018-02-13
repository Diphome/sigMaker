# sigMaker

This script is made to help you craft AoB signatures, it was made in python.

Considering the two following signatures :

**8C DB 60 00 00 00 83 EC 0C C7 04 58**

**8D B7 00 00 00 00 83 EC 0C C7 05 58**

sigMaker.py without args will output :

**8????000000083EC0CC70?58**

Use -s put one space every two characters :

**8? ?? ?0 00 00 00 83 EC 0C C7 0? 58**

Use -p to get a perfect signature, with -s to have spaces :

**?? ?? ?? ?? 00 00 83 EC ?? ?? ?? ??**
