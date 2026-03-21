import hashlib


file_md5="md5.hash"
file_sha256="sha256.hash"
file_sha3= "sha3.hash"
file_sha256double="sha256double.hash"

#Έλεγχος ακεραιότητας αρχείου με βάση το αποθηκευμένο hash
def hash_integrityCheck(hashFile, hashValue):

    #Εισαγωγή βιβλιοθήκης os για έλεγχο ύπαρξης αρχείου αλλα και για να μην κανουμε το προγραμμα ποιο πολυπλοκο
    import os
    
    #Ελέγχουμε αν το αρχείο hash υπάρχει και αν είναι άδειο. 
    # Αν δεν υπάρχει σημαίνει ότι είναι η πρώτη εγγραφή και δεν υπάρχει προηγούμενο hash για σύγκριση.  
    if not os.path.exists(hashFile) or os.path.getsize(hashFile) == 0:
        print("Πρώτη εγγραφή, δεν υπάρχει προηγούμενο hash.")
        return
    
    # Αν υπάρχει διαβάζουμε το αποθηκευμένο hash και συγκρίνουμε με το νέο hash που υπολογίσαμε.
    with open(hashFile, "r") as f:
        storedHash = f.read().strip()

    #Αν τα δύο hash είναι ίδια σημαίνει ότι το αρχείο δεν έχει τροποποιηθεί.
    if storedHash == hashValue:
        print("Το αρχείο δεν έχει τροποποιηθεί ")

    # Αν είναι διαφορετικά σημαίνει ότι το αρχείο έχει αλλοιωθεί.
    else:
        print("Το αρχείο έχει αλλοιωθεί ")

#Αποθήκευση των hash σε αρχείο .hash
def saveHash(hashFile,hashValue):
   
   with open(hashFile,"w") as f:
     
     f.write(hashValue)

   print(f"Το hash αποθηκεύτηκε στο αρχείο {hashFile}")

#Το menu επιλογών για τον χρήστη
def menu():

    print("\n" + "="*30)
    print("        ΜΕΝΟΥ ΕΠΙΛΟΓΩΝ")
    print("="*30)
    print("1. Υπολογισμός Hash")
    print("2. Έλεγχος Ακεραιότητας")
    print("5. Έξοδος")
    print("="*30)

#Το menu επιλογών για τον χρήστη για να επιλέξει τον αλγόριθμο που θέλει να χρησιμοποιήσει
def menu_algorithms():

    print("\n" + "="*30)
    print("  ΜΕΝΟΥ ΕΠΙΛΟΓΩΝ ΑΛΓΟΡΙΘΜΟΥ")
    print("="*30)
    print("1. MD5 hash")
    print("2. SHA256 hash")
    print("3. SHA3 hash")
    print("4. Διπλό SHA256 hash")
    print("5. Όλα τα hash")
    print("-"*30)

def menu_integrityCheck():

    print("\n" + "="*30)
    print("  ΜΕΝΟΥ ΕΠΙΛΟΓΩΝ ΑΛΓΟΡΙΘΜΟΥ")
    print("    ΈΛΕΓΧΟΣ ΑΚΕΡΑΙΟΤΗΤΑΣ")
    print("="*30)
    print("1. md5.hash")
    print("2. sha256.hash")
    print("3. sha3.hash")
    print("4. sha256double.hash")
    print("5. Όλα τα hash")
    print("-"*30)

#Είσοδος αρχείου και έλεγχος αν υπάρχει
while True:
 try:
    print("Δώσε όνομα αρχείου .txt")
    giveFile=input()
    with open(giveFile,"rb") as f:
     readFile=f.read()
    break
 except FileNotFoundError:
    print("Το αρχείο δεν βρέθηκε, δοκίμασε ξανά")
    continue
 

while True:

    menu()
    epilogi=int(input("Επίλεξε  (1-5):"))

    #Επιλογή υπολογισμού hash
    if epilogi==1:

        menu_algorithms()
        #Επιλογή αλγορίθμου και υπολογισμός hash
        algSelect=input()

        #υπολογισμός MD5 hash
        if algSelect=="1":

            #Υπολογισμός του MD5 hash του αρχείου χρησιμοποιώντας τη βιβλιοθήκη hashlib και αποθήκευση του αποτελέσματος σε μεταβλητή
            hashMD5=hashlib.md5(readFile).hexdigest()
            print(f"Το MD5 hash του {giveFile} είναι:{hashMD5}")
            saveHash(file_md5,hashMD5)
            

        #υπολογισμός SHA256 hash
        elif algSelect=="2":

            #Υπολογισμός του SHA256 hash του αρχείου χρησιμοποιώντας τη βιβλιοθήκη hashlib και αποθήκευση του αποτελέσματος σε μεταβλητή
            hashSHA256=hashlib.sha256(readFile).hexdigest()
            print(f"Το SHA256 hash του {giveFile} είναι:{hashSHA256}")
            saveHash(file_sha256,hashSHA256)
            

        #υπολογισμός SHA3 hash
        elif algSelect=="3":

            #Υπολογισμός του SHA3 hash του αρχείου χρησιμοποιώντας τη βιβλιοθήκη hashlib και αποθήκευση του αποτελέσματος σε μεταβλητή
            hashSHA3=hashlib.sha3_256(readFile).hexdigest()
            print(f"Το SHA3 hash του {giveFile} είναι:{hashSHA3}")  
            saveHash(file_sha3,hashSHA3)
            
        elif algSelect=="4":
           
           #Υπολογισμός του διπλού SHA256 hash του αρχείου χρησιμοποιώντας τη βιβλιοθήκη hashlib και αποθήκευση του αποτελέσματος σε μεταβλητή
           hashSHA256=hashlib.sha256(readFile).hexdigest()
           hashSHA256double=hashlib.sha256(hashSHA256.encode()).hexdigest()
           print(f"Το διπλό SHA256 hash του {giveFile} είναι:{hashSHA256double}")
           saveHash(file_sha256double,hashSHA256double)
            
        #υπολογισμός όλων των hash
        elif algSelect=="5":
        
            hashMD5=hashlib.md5(readFile).hexdigest()
            print(f"Το MD5 hash του {giveFile} είναι:{hashMD5}")
            saveHash(file_md5,hashMD5)

            hashSHA256=hashlib.sha256(readFile).hexdigest()
            print(f"Το SHA256 hash του {giveFile} είναι:{hashSHA256}")
            saveHash(file_sha256,hashSHA256)

            hashSHA3=hashlib.sha3_256(readFile).hexdigest()
            print(f"Το SHA3 hash του {giveFile} είναι:{hashSHA3}")
            saveHash(file_sha3,hashSHA3)

            hashSHA256double=hashlib.sha256(hashSHA256.encode()).hexdigest()
            print(f"Το διπλό SHA256 hash του {giveFile} είναι:{hashSHA256double}")
            saveHash(file_sha256double,hashSHA256double)
            
            
        #Ελεγχος για μη έγκυρη επιλογή αλγορίθμου
        else:

            print("Μη έγκυρη επιλογή, υπολογίστε ξανά")

            algSelect=input()
    
    #Επιλογή ελέγχου ακεραιότητας
    elif epilogi==2:
        #Εισαγωγή βιβλιοθήκης os για έλεγχο ύπαρξης αρχείων hash και για να μην κανουμε το προγραμμα ποιο πολυπλοκο
        import os

        #Έλεγχος για αρχεία hash στον τρέχοντα φάκελο 
        hashFiles = [f for f in os.listdir() if f.endswith(".hash")]

        #Αν υπάρχουν αρχεία hash εμφανίζουμε το menu επιλογών για έλεγχο ακεραιότητας 
        # και ζητάμε από τον χρήστη να επιλέξει ποιο hash θέλει να χρησιμοποιήσει για τον έλεγχο ακεραιότητας του αρχείου.
        if hashFiles:

            print("="*30)
            print("   ΔΙΑΘΕΣΙΜΑ ΑΡΧΕΙΑ HASH ")
            print("  ΓΙΑ ΕΛΕΓΧΟ ΑΚΕΡΑΙΟΤΗΤΑΣ:")
            print("="*30)
            for f in hashFiles:
                print(f"-->{f}")

            menu_integrityCheck()
            hashFileSelect=int(input())

            #Ξανα ανοίγουμε το αρχείο σε περίπτωση που ο χρήστης έχει επιλέξει έλεγχο ακεραιότητας την στιγμή που τρέχει το πρόγραμμα και έχει τροποποιήσει το αρχείο,
            # έτσι ώστε να διαβάσουμε το νέο περιεχόμενο του αρχείου και να υπολογίσουμε τα νέα hash για τον έλεγχο ακεραιότητας
            with open(giveFile, "rb") as f:
               readFile = f.read()

             

            if hashFileSelect==1:
                
                #Υπολογισμός του τρέχοντος MD5 hash του αρχείου και ελεγχος της ακεραιότητας συγκρίνοντας το τρέχον hash με το αποθηκευμένο hash
                hashMD5=hashlib.md5(readFile).hexdigest()
                print(f"Το τρέχον MD5 hash του {giveFile} είναι:{hashMD5}")
                hash_integrityCheck(file_md5,hashMD5)

            elif hashFileSelect==2:

                #Υπολογισμός του τρέχοντος SHA256 hash του αρχείου και ελεγχος της ακεραιότητας συγκρίνοντας το τρέχον hash με το αποθηκευμένο hash
                hashSHA256=hashlib.sha256(readFile).hexdigest()
                print(f"Το τρέχον SHA256 hash του {giveFile} είναι:{hashSHA256}")
                hash_integrityCheck(file_sha256,hashSHA256)

            elif hashFileSelect==3:

                #Υπολογισμός του τρέχοντος SHA3 hash του αρχείου και ελεγχος της ακεραιότητας συγκρίνοντας το τρέχον hash με το αποθηκευμένο hash
                hashSHA3=hashlib.sha3_256(readFile).hexdigest()
                print(f"Το τρέχον SHA3 hash του {giveFile} είναι:{hashSHA3}")
                hash_integrityCheck(file_sha3,hashSHA3)

            elif hashFileSelect==4:

                #Υπολογισμός του τρέχοντος διπλού SHA256 hash του αρχείου και ελεγχος της ακεραιότητας συγκρίνοντας το τρέχον hash με το αποθηκευμένο hash
                hashSHA256=hashlib.sha256(readFile).hexdigest()
                hashSHA256double=hashlib.sha256(hashSHA256.encode()).hexdigest()
                print(f"Το τρέχον διπλό SHA256 hash του {giveFile} είναι:{hashSHA256double}")
                hash_integrityCheck(file_sha256double,hashSHA256double)

            elif hashFileSelect==5:

                #Υπολογισμός όλων των τρέχοντων hash του αρχείου και ελεγχος της ακεραιότητας συγκρίνοντας τα τρέχοντα hash με τα αποθηκευμένα hash
                hashMD5=hashlib.md5(readFile).hexdigest()
                print(f"Το τρέχον MD5 hash του {giveFile} είναι:{hashMD5}")
                hash_integrityCheck(file_md5,hashMD5)

                hashSHA256=hashlib.sha256(readFile).hexdigest()
                print(f"Το τρέχον SHA256 hash του {giveFile} είναι:{hashSHA256}")
                hash_integrityCheck(file_sha256,hashSHA256)

                hashSHA3=hashlib.sha3_256(readFile).hexdigest()
                print(f"Το τρέχον SHA3 hash του {giveFile} είναι:{hashSHA3}")
                hash_integrityCheck(file_sha3,hashSHA3) 

                hashSHA256=hashlib.sha256(readFile).hexdigest()
                hashSHA256double=hashlib.sha256(hashSHA256.encode()).hexdigest()
                print(f"Το τρέχον διπλό SHA256 hash του {giveFile} είναι:{hashSHA256double}")
                hash_integrityCheck(file_sha256double,hashSHA256double)

            #Ελεγχος για μη έγκυρη επιλογή αλγορίθμου
            else:

                print("Μη έγκυρη επιλογή, δοκίμασε ξανά.")
                hashFileSelect=input()
                
        else:
            print("Δεν υπάρχουν αρχεία hash για έλεγχο ακεραιότητας, υπολόγισε πρώτα ένα hash.")
            continue
    
    #Επιλογή έξοδος από το πρόγραμμα
    elif epilogi==5:
        print("Έξοδος από το πρόγραμμα.")
        break

    #Ελεγχος για μη έγκυρη επιλογή στο menu
    else:
        print("Μη έγκυρη επιλογή, δοκίμασε ξανά.")
        continue
       

 