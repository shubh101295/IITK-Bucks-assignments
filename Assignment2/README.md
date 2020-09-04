# Assignment 2 solution

This folder contains 3 python files
#### 1) keygen.py
 
 `python3 keygen.py`
 It creates a private and public key pair and stores them in private.pem and public.pem respectively .

#### 2) sign.py 

`python3 sign.py`

```
Enter the relative path to privatekey - ./private.pem
Enter the text to be signed  - shubh  {here enter the unencrypted message} 
Enter the relative path to file to which the output is to written - ./output.txt
```

Then it writes signed string to output.txt 

#### 3) verify.py

`python3 verify.py`

```
Enter the relative path to publickey - ./public.pem 
Enter the unencrypted text to be checked - shubh
Enter the relative path to file with encrypted message - ./output.txt
```

if output is `User is authenticated` then the publickey matches to the privatekey 
else if the output is `User is not authenticated` then the publickey matches to privatekey 

if you enter `./public2.pem` in the path to publickey it returns `User is not authenticated` as it is not correct publickey to privatekey in `./private.pem`