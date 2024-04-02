def decrypt(ciphertext, key):
    # Step 1: Get the matrix from the ciphertext in zigzag order
    matrix = []
    index = 0
    while index < len(ciphertext):
        if len(matrix) % 2 == 0:
            matrix.append(ciphertext[index:index+3])
        else:
            matrix.append(ciphertext[index:index+3][::-1])
        index += 3
    
    # Step 2: Reverse the matrix
    matrix = matrix[::-1]
    print("Reversed Matrix:")
    for row in matrix:
        print(row)
    
    # Step 3: Extract the reversed text from the matrix
    reversed_text = ""
    for row in matrix:
        reversed_text += row
    print("Reversed Text:", reversed_text)
    
    # Step 4: Reverse the concatenated string
    reversed_text = reversed_text[::-1]
    print("Reversed Text After Reversal:", reversed_text)
    
    # Step 5: Shift the reversed text back to PTEXT
    PTEXT = ""
    for char in reversed_text:
        PTEXT += chr((ord(char) - 33 - key)  + 65)
        # if char.isalpha():
        #     PTEXT += chr((ord(char) - 33 - key)  + 65)
        # elif char == "@":
        #     PTEXT += " "
        # else:
        #     PTEXT += char
    print("PTEXT:", PTEXT)
    return PTEXT

ciphertext = "&35.)\"-617*"
key = 1

PTEXT = decrypt(ciphertext, key)



#&35.)"-617*