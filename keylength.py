def determine_key_length(cipher_string):
    
    frequency_sum = [0]*len(cipher_string)

    for i in range(1,len(cipher_string)+1,2): #scour throught each of the possible lengths of the key
        frequencies = [0] * 256
        average = 0
        for j in range (0,len(cipher_string),2*i):
            hex_value = int(cipher_string[j:j+2],10)
            frequencies[hex_value] += 1
        for frequency in frequencies:
            average += (frequencies[hex_value]**2)/(256**2)
            frequency_sum[i] = average
    return frequency_sum.index(max(frequency_sum))
    