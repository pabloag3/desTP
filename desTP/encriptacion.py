from pydes import *

key = "secret_k"
text = "Hello wo"
d = des()
ciphered = d.encrypt(key, text)
plain = d.decrypt(key, ciphered)
print("Ciphered: %r" % ciphered)
print("Deciphered: ", plain)
