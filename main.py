import keydet
import keylength

def main():
    ciphertext = open("ciphertext.txt","w")
    cipher_string = input("Enter the cipher: ")
    ciphertext.write(cipher_string)
    ciphertext.close()
    key_length = keylength.determine_key_length(cipher_string)
    plainstring = keydet.determine_key_dictionary(keylength,cipher_string)

    plaintext = open("plaintext.txt","w")
    plaintext.write(plainstring)
    plaintext.close()
