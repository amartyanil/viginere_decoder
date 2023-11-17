def determine_key_character_dictionary_xor(key_index,key_length,cipher_string): #this finds a character of the key if the encoding had been done using XOR-ing
        occurences = [0] * 256

        for i in range(key_index,len(cipher_string),2*key_length):
                hex_value = int(cipher_string[i:i+2],10)
                occurences[hex_value-1] += 1

        most_occuring_character_ciphertext = occurences.index(max(occurences)) + 1

        return chr(most_occuring_character_ciphertext ^ 101)



def determine_key_character_dictionary_adding(key_index,key_length,cipher_string): #this finds a character of the key if the encoding had been done using adding the character values
        occurences = [0] * 256

        for i in range(key_index,len(cipher_string),2*key_length):
                hex_value = int(cipher_string[i:i+2],10)
                occurences[hex_value-1] += 1

        most_occuring_character_ciphertext = occurences.index(max(occurences)) + 1

        return chr(most_occuring_character_ciphertext - 101)
                      

def determine_key_dictionary(key_length, cipher_string):
        decode_type = input("Enter 1 if the encoding of the plaintext had been done using XOR-ing. Enter 2 if the encoding of plaintext had been done using adding the character values: ")

        key = ""

        if decode_type == 1:
                for i in range(0,key_length):
                        key = key + determine_key_character_dictionary_xor(i,key_length,cipher_string)
        elif decode_type == 2:
                for i in range(0,key_length):
                        key = key + determine_key_character_dictionary_adding(i,key_length,cipher_string)
        return key                        