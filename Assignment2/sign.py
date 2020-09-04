from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import  SHA256
from base64 import b64encode, b64decode
import sys

def importKey(externKey):
    return RSA.importKey(externKey)

def sign(message, priv_key):
    signer = PKCS1_v1_5.new(priv_key)
    digest = SHA256.new()
    message = message.encode()
    digest.update(message)
    return signer.sign(digest)

path = input("Enter the relative path to privatekey - ")
try:
	f = open(path,"r")
except:
	print("No such File exists")
	sys.exit()
privatekey = f.read()
privatekey = importKey(privatekey)

message = input("Enter the text to be signed  - ")
output_to = input("Enter the name of file to which the output is to written - ")
signature = b64encode(sign(message, privatekey))

f = open(output_to , "w")
f.write(signature.decode())
f.close