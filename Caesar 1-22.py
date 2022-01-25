def encrypt(mix_all,s):
    result = ''

    for i in range(len(mix_all)): 
        char = mix_all[i]
        
        # Filter
        if (char.isupper()): 
            result += chr((ord(char) + s - 65) % 26 + 65)

        elif (char.isnumeric()): 
            result += chr((ord(char) + s - 48) % 10 + 48)
        
        elif (ord(char) >= 33 and ord(char) <= 47): 
            result += chr((ord(char) + s - 33) % 14 + 33)

        elif (char.isspace()):
            result += chr((ord(char) + s - 32) % 1 + 32)

        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result

    
print("\n ========= Encrypt =========")
text = input(" Text Encryption Chyper : ")
s = int(input(" Pergeseran             : "))

print("\n ========== Hasil ==========")
print (" Plain Text    : " + text)
print (" Shift pattern : " + str(s))
print (" Cipher        : " + encrypt(text,s))

# ========= Encrypt =========
#  Text Encryption Chyper : UraqebFbrzneab     
#  Pergeseran             : 13

#  ========== Hasil ==========
#  Plain Text    : UraqebFbrzneab
#  Shift pattern : 13
#  Cipher        : HendroSoemarno