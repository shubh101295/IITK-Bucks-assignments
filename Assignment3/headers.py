
class Input:
	def __init__(self, transactionID ,index, sign,len_sign= None):
		self.transactionID = transactionID
		self.index = index
		self.sign = sign
		self.len_sign = len_sign==None and len(sign) or len_sign

	def show(self):
		print("TransactionID: " + self.transactionID)
		print("Index: " + str(self.index))
		print("Length of the signature:  " + str(self.len_sign))
		print("Signature:  " + self.sign)

	def getBytes(self):
		bytes_transactionID = bytes.fromhex(self.transactionID)
		bytes_index = self.index.to_bytes(4,'big')
		bytes_sign = bytes.fromhex(self.sign)
		bytes_len_sign = self.len_sign.to_bytes(4,'big')
		return bytes_transactionID +bytes_index+bytes_len_sign + bytes_sign 

	def isValid(self):
		valid_chars = "0123456789abcdefABCDEF"
		for c in self.transactionID:
			if c not in valid_chars:
				print("Error - TransactionID should be a hex value")
				return False
		for c in self.sign:
			if c not in valid_chars:
				print("Error - Signature should a hex value")
				return False
		l = len(self.transactionID)
		if l>64:
			print("Error - TransactionID should have 64 hex characters")
			return False

		if l<64:
			print("Length of TransactionID is less than 64 hex characters, appending '0' at the end")
			while l<64:
				self.transactionID += '0'
				l+=1

		if len(self.sign)%2==1:
			print("Error - Signature should have even hex characters")
			return False

		for d in self.index:
			if (not d.isdigit()):
				print(d)
				print("Error - Index should be an integer ")
				return False 
		self.len_sign= self.len_sign//2
		self.index =int(self.index)
		return True

class Output:
	def __init__(self, coins,public_key_path=None ,public_key=None ,public_key_len=None ):
		self.coins = coins 
		self.public_key_path= public_key_path
		self.public_key = public_key
		self.public_key_len = public_key_len

	def show(self):
		print("No. of Coins:  " +str(self.coins))
		print("Length of public key: " +str(self.public_key_len))
		print("Public Key: \n" + self.public_key)

	def getBytes(self):
		bytes_coins = self.coins.to_bytes(8,'big')
		bytes_public_key_len = self.public_key_len.to_bytes(4,'big')
		bytes_public_key = self.public_key.encode()
		return bytes_coins + bytes_public_key_len + bytes_public_key

	def isValid(self):
		for d in self.coins:
			if not d.isdigit():
				print("Error - No.of Coins should be integer")
				return False 
		self.coins = int(self.coins)
		try:
			f = open(self.public_key_path,"r")
		except:
			print("Error - Enter a valid path to publickey")
			return False
		self.public_key = f.read()
		f.close()
		self.public_key_len = len(self.public_key)
		return True
		
class Transaction:
	def __init__(self, input_array,output_array):
		self.input_array = input_array
		self.output_array = output_array

def transactionToBytes(transaction):
	data = len(transaction.input_array).to_bytes(4,'big')
	for i in transaction.input_array:
		data += i.getBytes()
	data += len(transaction.output_array).to_bytes(4,'big')
	for o in transaction.output_array:
		data += o.getBytes()
	return data 

def transactionToArray(data):
	x = data[0:4]
	y = int.from_bytes(x,"big")
	pos = 4
	done =0 
	input_array =[]
	while done<y:
		done+=1 
		transactionID =  data[pos:pos+32].hex()
		pos+=32 
		index = int.from_bytes(data[pos:pos+4],"big")
		pos+=4
		l = int.from_bytes(data[pos:pos+4],"big")
		pos+=4 
		sign = data[pos:pos+l].hex()
		pos+=l
		i = Input(transactionID , index , sign ,l)
		input_array.append(i)
	y = int.from_bytes(data[pos:pos+4],"big")
	pos+=4 
	done = 0
	output_array = []
	while done<y:
		done+=1 
		coins = int.from_bytes(data[pos:pos+8] , "big")
		pos+= 8
		pub_key_len = int.from_bytes(data[pos:pos+4] , "big") 
		pos+=4
		pub_key= data[pos:pos+pub_key_len].decode("utf-8")
		pos+=pub_key_len
		o = Output(coins=coins, public_key=pub_key ,public_key_len= pub_key_len)
		output_array.append(o)
	return input_array, output_array
