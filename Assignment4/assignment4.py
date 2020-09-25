import sys
import hashlib

sys.path.insert(1,"../Assignment3/")
import headers

file_name = input("Enter the name of file containing data\n>")
print('')

try:
	f = open(file_name ,"rb")
	data = f.read()
except:
	print("No such file found")
	sys.exit()

transactionID = hashlib.sha256(data).hexdigest() 
print("Transaction ID:  " + transactionID +"\n")

input_array ,output_array = headers.transactionToArray(data)
print("Number of inputs: " + str(len(input_array)) + "\n")
for i in range(len(input_array)):
	print("Input Data " + str(i+1))
	input_array[i].show()
	print('')

print("Number of outputs: " + str(len(output_array)) + "\n")
for o in range(len(output_array)):
	print("Output Data " + str(o+1))
	output_array[o].show() 
	print('')