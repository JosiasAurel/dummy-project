from cryptography.fernet import Fernet

# this function creates my key to encrypt
def create_key():
    my_key = Fernet.generate_key()
    with open("my_key.key", "wb") as my_key_file:
         my_key_file.write(my_key)

# a function to load my key
def load_key():
    
    return open("my_key.key", "rb").read()

def load_and_encrypt(filename, key):
    fernet = Fernet(key)

    with open(filename, "rb") as file:
         file_data = file.read()
         #encrypt the data
         encrypted = fernet.encrypt(file_data)

         with open(filename, "wb") as file:
              file.write(encrypted)


def load_and_decrypt(filename, key):
    fernet = Fernet(key)
    with open(filename, "rb") as file:
         encrypted = file.read()
         decrypted = fernet.decrypt(encrypted)
         with open(filename, "wb") as file:
              file.write(decrypted)

  
create_key()

my_key = load_key()

while True:

      what_to_do = input("What do you want to do? => \n Hint:\n 0 : Encrypt\n 1 : Decrypt")


      file = input("Enter the name of the file to work with => ")

      if what_to_do == 0:
         load_and_encrypt(file, my_key)
      elif what_to_do == 1: 
         load_and_decrypt(file, my_key)
   

#test_msg = "hello, ill be encrypted".encode()

#fer = Fernet(my_key)
#encrypted_msg = fer.encrypt(test_msg)

#print(encrypted_msg)

#dec = fer.decrypt(encrypted_msg)
#print(dec)
