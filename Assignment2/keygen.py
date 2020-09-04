from Crypto.PublicKey import RSA

key = RSA.generate(4096)
private_key = key.export_key()
file_out = open("private.pem", "wb")
file_out.write(private_key)
file_out.close()
public_key = key.publickey().export_key()
file_out = open("public.pem", "wb")
file_out.write(public_key)
file_out.close()
# print(private_key)
# print(public_key)
 