import sys 
import headers
import hashlib

try:
	n = int(input("Enter number of inputs: "))
except:
	print("Integer was expected")
	sys.exit()

print("")
input_array = []
for i in range(n):
	print("Input "+str(i+1))
	transactionID = input("Enter the transactionID: ")
	index = input("Enter the index of output: ")
	print("Signature should a hex value containing even hex characters")
	signature = input("Enter a signature: ")
	my_input = headers.Input(transactionID,index,signature)
	if not my_input.isValid():
		sys.exit()
	input_array.append(my_input)
	print("")

print(input_array)

try:
	n= int(input("Enter number of outputs - "))
except:
	print("Integer was expected")
	sys.exit()
print("")

output_array = []
for i in range(n):
	coins = input("Enter the number of coins for output: ")
	publicKeyPath = input("Enter the relative path to publickey: ")
	my_output = headers.Output(coins, publicKeyPath)
	if not my_output.isValid():
		sys.exit()
	output_array.append(my_output)
	print("")

try:
	my_transaction = headers.Transaction(input_array,output_array)
	x = headers.transactionToBytes(my_transaction)
	file_name = hashlib.sha256(x).hexdigest() + ".dat"
	with open(file_name ,"wb") as f:
		f.write(x)
	print("Transaction Successfull")
	print("Saving data to " + file_name)
except:
	print("Some Error occurred in transaction")