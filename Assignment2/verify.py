from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import  SHA256
from base64 import b64encode, b64decode
import sys


def importKey(externKey):
    return RSA.importKey(externKey)

def verify(message, signature, pub_key):
    signer = PKCS1_v1_5.new(pub_key)
    digest = SHA256.new()
    message = message.encode()
    digest.update(message)
    return signer.verify(digest, signature)

path = input("Enter the relative path to publickey - ")
try:
	f = open(path,"r")
except:
	print("No such File exists")
	sys.exit()
publickey = f.read()
publickey = importKey(publickey)
# print(publickey)
f.close()

message = input("Enter the unencrypted text to be checked - ")
path2 = input("Enter the relative path to file with encrypted message - ")

try:
	f = open(path2,"r")
except:
	print("No such File exists")
	sys.exit()

signature = f.read()
# print(signature)
f.close()

verify = verify(message, b64decode(signature.encode()), publickey)

if verify is True:
	print("User is authenticated")
else:
	print("USer is not authenticated")