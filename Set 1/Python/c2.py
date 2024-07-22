import sys
sys.path.append('Mods') # adds the folder with the functions to the files checked
from Functions import bin_to_hex # imports custom function

def hex_XOR(hex1, hex2):
    if (hex1 == ""): # Default Value
        hex1 = "1c0111001f010100061a024b53535009181c"
    if (hex2 == ""): # Default Value
        hex2 = "686974207468652062756c6c277320657965"

    if ( len(hex1) != len(hex2) ): # Compares to verify inputs are equal
        sys.exit("The two values are not the same length")

    try:
        intv1 = int(hex1, 16) # Changes hex to decimal
        intv2 = int(hex2, 16)
    except:
        sys.exit("Not a valid hex value")

    XOR = intv1 ^ intv2 # Takes XOR of the two decimal numbers
    XOR = bin(XOR) # Changes decimal to binary
    XOR = XOR[2:] # Cuts off the '0b'
    while (len(XOR)%16 != 0): # If the code is 1 short it will add a 0 to the front
        XOR = "0" + XOR # sometimes bin() will cut off leading 0s

    XOR_hex = bin_to_hex(XOR) # Binary back to hex with custom function

    return(XOR_hex)

if (__name__ == '__main__'):
    print("Note: Default value will be the strings provided on the website if the strings are empty")
    print(hex_XOR(input('Please provide the first hex value: '),input('Please provide the second hex value: ')))
