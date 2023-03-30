#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ishac123
#
# Created:     30-03-2023
# Copyright:   (c) ishac123 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import time
now = time.ctime()
qna = {
       "hi":"hey",
       "how are you":"I am fine",
       "what is your name":"my name is ishu",
       "How old are you":"I am 20 years old",
       "what is the time now" : now,
}

while True:
    qs = input()

    if(qs == "quit"):
        break

    else:
        print(qna[qs])