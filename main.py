import hashlib

file_md5="md5.hash"
file_sha256="sha256.hash"
file_sha3= "sha3.hash"


try:
 print("Δώσε όνομα αρχείου .txt")
 giveFile=input()
 openFile=open(giveFile,"rb")
 readFile=openFile.read()
 openFile.close()
except FileNotFoundError:
 print("Το αρχείο δεν βρέθηκε, δοκίμασε ξανά")
 giveFile=input()

print("Επίλεξε Αλγόριθμο MD5(1),SHA256(2),SHA3(3) ή όλους(4)")
algSelect=input()

if algSelect=="1":
 
 hashMD5=hashlib.md5(readFile).hexdigest()
 print(f"Το MD5 hash του {giveFile} είναι:{hashMD5}")
 f_md5=open(file_md5,"w")
 f_md5.write(hashMD5)
 f_md5.close()
 print(f"Το MD5 hash αποθηκεύτηκε στο αρχείο {file_md5}")

elif algSelect=="2":
 
 hashSHA256=hashlib.sha256(readFile).hexdigest()
 print(f"Το SHA256 hash του {giveFile} είναι:{hashSHA256}")
 f_sha256=open(file_sha256,"w")
 f_sha256.write(hashSHA256)
 f_sha256.close()
 print(f"Το SHA256 hash αποθηκεύτηκε στο αρχείο {file_sha256}")
elif algSelect=="3":
 
 hashSHA3=hashlib.sha3_256(readFile).hexdigest()
 print(f"Το SHA3 hash του {giveFile} είναι:{hashSHA3}")
 f_sha3=open(file_sha3,"w")
 f_sha3.write(hashSHA3)
 f_sha3.close()
 print(f"Το SHA3 hash αποθηκεύτηκε στο αρχείο {file_sha3}")

elif algSelect=="4":
 
 hashMD5=hashlib.md5(readFile).hexdigest()
 print(f"Το MD5 hash του {giveFile} είναι:{hashMD5}")
 f_md5=open(file_md5,"w")
 f_md5.write(hashMD5)
 f_md5.close()
 print(f"Το MD5 hash αποθηκεύτηκε στο αρχείο {file_md5}")

 hashSHA256=hashlib.sha256(readFile).hexdigest()
 print(f"Το SHA256 hash του {giveFile} είναι:{hashSHA256}")
 f_sha256=open(file_sha256,"w")
 f_sha256.write(hashSHA256)
 f_sha256.close()
 print(f"Το SHA256 hash αποθηκεύτηκε στο αρχείο {file_sha256}")

 hashSHA3=hashlib.sha3_256(readFile).hexdigest()
 print(f"Το SHA3 hash του {giveFile} είναι:{hashSHA3}")
 f_sha3=open(file_sha3,"w")
 f_sha3.write(hashSHA3)
 f_sha3.close()
 print(f"Το SHA3 hash αποθηκεύτηκε στο αρχείο {file_sha3}")
 
else:
 print("Μη έγκυρη επιλογή, δοκίμασε ξανά")
 algSelect=input()


 