#to implement ceaser cipher
import string
def encrypt(message,key):  #encryption of data
  encrypted_message=""
  for char in message:
    if char.isalpha():
      shift=ord(char)+key
      if char.isupper():
        if shift>ord('Z'):
          shift-=26
        elif shift<ord('A'):
          shift+=26
      elif char.islower():
        if shift>ord('z'):
          shift-=26
        elif shift<ord('a'):
          shift+=26
      encypted_message+=chr(shift)
    else:
      encypted_message+=char
  return encrypted_message

def decrypt(message,kry):  #decryption of data
  decrypted_message=""
  for char in message:
    if char.isalpha():
      shift=ord(char)-key
      if char.isupper():
        if shift>ord('Z'):
          shift-=26
        elif shift<ord('A'):
          shift+=26
      elif char.islower():
        if shift>ord('z'):
          shift-=26
        elif shift<ord('a'):
          shift+=26
      decrypted_message+=chr(shift)
    else:
      decrypted_message+=char
  return decrypted_message

def main():  #main function
  message=input("Enter your message to encrypt or decrypt: ")
  key=int(input("Enter a key (a number between 1 and 25): "))
  while key<1 or key>25:
    key=int(input("Invalid key. Enter a key (a number between 1 and 25): "))
  encrypted_message=encrypt(message,key)
  print("Encrypted message:",encrypted_message)
  decrypted_message=decrypt(encrypted_message,key)
  print("Decrypted message:",decrypted_message)

if __name__=="__main__":
  main()
