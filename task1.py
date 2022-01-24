#!/bin/python3
import sys
import random
import string
import time
import hashlib
start_time = time.time()
if __name__ == "__main__":
    try:
        le=10
        st=00
        fi='randomfile.txt'
        for i, param in enumerate(sys.argv):
            if param=='-n':
                le=int(sys.argv[i+1])
            if param =='-m':
                st=sys.argv[i+1]
            if param=='-f':
                fi=sys.argv[i+1]
        strin=''.join([random.choice(string.ascii_uppercase+string.digits ) for n in range(le)])
        result = hashlib.md5(strin.encode())
        res=result.hexdigest()
        while st!=res[:2]:
            strin=''.join([random.choice(string.ascii_uppercase+string.digits ) for n in range(le)])
            result = hashlib.md5(strin.encode())
            res=result.hexdigest()
        final=open(fi, 'w').write(strin+'\n')
        print(f'[+] Got in {time.time() - start_time}: {res} {strin}')
    except:
        print('[-]')
        
    