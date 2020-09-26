import sys
import time 
import hashlib

def time_nanosecond():
	return int(time.time()*1000)

def check_hex(data):
	valid_chars = "0123456789abcdefABCDEF"
	for i in data:
		if i not in valid_chars:
			return False
	return True

try:
	index = int(input("Index: "))
except:
	print("Index should be integer") 
	sys.exit()

parent_hash = input("Parent Hash: ")

if len(parent_hash)!=64 or (not check_hex(parent_hash)):
	print("Parent Hash should be of 32 bytes and should contain hex characters")
	sys.exit()

target = input("Target: ")
if len(target)!=64 or (not check_hex(target)):
	print("Target should be of 32 bytes and should contain hex characters")
	sys.exit()

block_body_data_path = input("Relative path to the block body: ")
try:
	f = open(block_body_data_path,"rb")
except:
	print("No such file found")
	sys.exit()

block_data = f.read()
# print(s)
f.close()

block_header = index.to_bytes(4,'big')
block_header += bytes.fromhex(parent_hash) 
block_header += bytes.fromhex(hashlib.sha256(block_data).hexdigest())
block_header += bytes.fromhex(target)

trial=1 

print(block_header.hex())
start = time.time()

while(True):
	t = time_nanosecond() 
	temp = block_header + t.to_bytes(8,"big") + trial.to_bytes(8,"big")
	temp_hash = hashlib.sha256(temp).hexdigest()
	if temp_hash<target:
		print('')
		print("Hash:" + temp_hash)
		print("Nonce: " +str(trial))
		print("timestamp: " + str(t))
		break
	trial +=1

print("Total time taken " +str(int(time.time()-start)) + " sec")
