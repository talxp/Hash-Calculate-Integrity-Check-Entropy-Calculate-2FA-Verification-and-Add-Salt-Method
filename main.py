import hashlib
import os

file_md5="md5.hash"
file_sha256="sha256.hash"
file_sha3= "sha3.hash"

import os

def hash_integrityCheck(hashFile, hashValue):
    if not os.path.exists(hashFile) or os.path.getsize(hashFile) == 0:
        print("Πρώτη εγγραφή, δεν υπάρχει προηγούμενο hash.")
        return
    with open(hashFile, "r") as f:
        storedHash = f.read().strip()
    if storedHash == hashValue:
        print("Το αρχείο δεν έχει τροποποιηθεί ")
    else:
        print("Το αρχείο έχει αλλοιωθεί ")

#Αποθήκευση των hash σε αρχείο .hash
def saveHash(hashFile,hashValue):
 with open(hashFile,"w") as f:
  f.write(hashValue)
 print(f"Το hash αποθηκεύτηκε στο αρχείο {hashFile}")

#Είσοδος αρχείου και έλεγχος αν υπάρχει
try:
 
 print("Δώσε όνομα αρχείου .txt")
 giveFile=input()

 with open(giveFile,"rb") as f:
  readFile=f.read()
  
except FileNotFoundError:
 print("Το αρχείο δεν βρέθηκε, δοκίμασε ξανά")
 giveFile=input()

#Επιλογή αλγορίθμου και υπολογισμός hash
print("Επίλεξε Αλγόριθμο MD5(1),SHA256(2),SHA3(3) ή όλους(4)")
algSelect=input()

#υπολογισμός MD5 hash
if algSelect=="1":
 
 hashMD5=hashlib.md5(readFile).hexdigest()
 print(f"Το MD5 hash του {giveFile} είναι:{hashMD5}")
 hash_integrityCheck(file_md5,hashMD5)
 saveHash(file_md5,hashMD5)

#υπολογισμός SHA256 hash
elif algSelect=="2":
 
 hashSHA256=hashlib.sha256(readFile).hexdigest()
 print(f"Το SHA256 hash του {giveFile} είναι:{hashSHA256}")
 hash_integrityCheck(file_sha256,hashSHA256)
 saveHash(file_sha256,hashSHA256)

#υπολογισμός SHA3 hash
elif algSelect=="3":

 hashSHA3=hashlib.sha3_256(readFile).hexdigest()
 print(f"Το SHA3 hash του {giveFile} είναι:{hashSHA3}")
 hash_integrityCheck(file_sha3,hashSHA3)    
 saveHash(file_sha3,hashSHA3)
 
#υπολογισμός όλων των hash
elif algSelect=="4":
 
 hashMD5=hashlib.md5(readFile).hexdigest()
 print(f"Το MD5 hash του {giveFile} είναι:{hashMD5}")
 hash_integrityCheck(file_md5,hashMD5)
 saveHash(file_md5,hashMD5)

 hashSHA256=hashlib.sha256(readFile).hexdigest()
 print(f"Το SHA256 hash του {giveFile} είναι:{hashSHA256}")
 hash_integrityCheck(file_sha256,hashSHA256)
 saveHash(file_sha256,hashSHA256)

 hashSHA3=hashlib.sha3_256(readFile).hexdigest()
 print(f"Το SHA3 hash του {giveFile} είναι:{hashSHA3}")
 hash_integrityCheck(file_sha3,hashSHA3)
 saveHash(file_sha3,hashSHA3)

#Ελεγχος για έγκυρη επιλογή αλγορίθμου
else:
 
 print("Μη έγκυρη επιλογή, δοκίμασε ξανά")
 algSelect=input()


 