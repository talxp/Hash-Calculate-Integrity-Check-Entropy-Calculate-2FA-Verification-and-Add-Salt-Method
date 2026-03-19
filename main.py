import hashlib

print("Δώσε όνομα αρχείου .txt")
giveFile=input()
openFile=open(giveFile,"rb")
readFile=openFile.read()
print(readFile)

print("Επίλεξε Αλγόριθμο MD5(1),SHA256(2),SHA3(3) ή όλους(4)")
algSelect=input()

if algSelect=="1":
 
 hashMD5=hashlib.md5(readFile)
 print(f"Το MD5 hash του {giveFile} είναι:{hashMD5.hexdigest()}")

elif algSelect=="2":
 
 hashSHA256=hashlib.sha256(readFile)
 print(f"Το SHA256 hash του {giveFile} είναι:{hashSHA256.hexdigest()}")

elif algSelect=="3":
 
 hashSHA3=hashlib.sha3_256(readFile)
 print(f"Το SHA3 hash του {giveFile} είναι:{hashSHA3.hexdigest()}")

else:
 
 hashMD5=hashlib.md5(readFile)
 print(f"Το MD5 hash του {giveFile} είναι:{hashMD5.hexdigest()}")

 hashSHA256=hashlib.sha256(readFile)
 print(f"Το SHA256 hash του {giveFile} είναι:{hashSHA256.hexdigest()}")

 hashSHA3=hashlib.sha3_256(readFile)
 print(f"Το SHA3 hash του {giveFile} είναι:{hashSHA3.hexdigest()}")
 