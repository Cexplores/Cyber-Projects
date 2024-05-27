
import sys

#Basic Encryption
#Are you encrypting or decrypting

print("1:Encryption \ 2:Decrypt")
Does_user_want_to_encrypt_or_decrypt = input()

if Does_user_want_to_encrypt_or_decrypt == "Encrypt":
#Take in txt file named "Text to be encrypted")
  print("What is the name of the file")
  File_to_be_encrypted = "test.txt" #sys.argv[1] #Get file name from system
  FTBE = open(File_to_be_encrypted,'r+')
  key =  input("Please enter an integer key")
  #take file and apply algorithm
    #Take FTBE and get the integer counts for each character
  while 1:
        
        Char = FTBE.read(1)
        with open("Encrypted_file.txt",w) as file:
            #Get INT of Char and +5 i
            
            
        
        if not char:
            break
      



#elif Does_user_want_to_encrypt_or_decrypt == "Decrypt":
else : 
   # print("Command invalid, Please check command and try again")


#Encrypting 
#Take txt file from cmd line
#Apply the function to the txt file
#Print file named encrypted file