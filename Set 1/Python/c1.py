def hex_to_base64(hexv):
    if (hexv == ""): #Default value from the website
        hexv = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

    import sys
    sys.path.append('Mods') #adds the folder with the functions to the files checked
    from Functions import hex_to_bin #imports custom function
    from Variables import base64 #Made the base64 list since messing around and learning new stuff took too much time

    binary = hex_to_bin(hexv) #Hex to binary with custom function

    try:
        text = ""
        num = ""
        i = 0
        for x in range(len(binary)//6): #Base64 uses 6 bytes, so //6
            num = binary[i:(i+6)] #Takes sections of 6 bytes
            i += 6 #Takes sections of 6 bytes
            num = int(num, 2) #Takes the 6-byte section and converts to binary
            text = text + base64[num] #Converts the number to corresponding base64 and adds it to text
    except:
        sys.exit('Hex value is not proper length')

    return text

if (__name__ == '__main__'):
    print("Note: Default value will be the string provided on the website if the string is empty")
    print(hex_to_base64(input("Please provide the hex value: ")))