import hashlib
import sys

if (len(sys.argv)!=2):
	print("USAGE : python3 assignment1.py <input_string>")
	sys.exit()

raw_string = sys.argv[1]

target ="0000" 
for i in range(60):
	target+='f'

# print(target) 
# print(len(target))


i=1
while True:
	raw2 = raw_string +str(i) 
	converted = hashlib.sha256(raw2.encode()).hexdigest()

	if converted < target:
		print(f"string : {raw_string}")
		print(f"Magic Number : {i}")
		print(f"SHA256 hash value : {converted}")
		break
	i+=1
	