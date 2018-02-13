# sigMaker

This script is made to help you craft AoB signatures, it was made in python.

For the following cases, I will use those two signatures :

8C DB 60 00 00 00 83 EC 0C C7 05 58

8D B7 00 00 00 00 83 EC 0C C7 05 58

sigMaker.py :

**8????000000083EC0CC70558**

Use -s put one space every two characters :

sigMaker.py -s

**8? ?? ?0 00 00 00 83 EC 0C C7 05 58**

use the -p for a perfect signature :

sigMaker.py -p -s 

**?? ?? ?? ?? 00 00 83 EC ?? ?? ?? ??**

You can also use -b to specify wether you are in 32bits or 64bits system, for instance :

sigMaker.py -b 64 -p -s

**?? ?? ?? ?? ?? ?? ?? ?? 0C C7 05 58**
