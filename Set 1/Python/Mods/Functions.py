def hex_to_bin(hexv):
    import sys
    try:
        intv = int(hexv, 16) #Changes hex to decimal
    except:
        sys.exit("Not a valid hex value")
    binary = bin(intv) #Changes decimal to binary
    binary = binary[2:] #Cuts off the '0b'
    while (len(binary)%16 != 0): #If the code is 1 short it will add a 0 to the front
        binary = "0" + binary #otherwise bin() will cut off leading 0s
    return binary

def bin_to_hex(binv):
    import sys
    try:
        intv = int(binv, 2) #Changes binary to decimal
    except:
        sys.exit("Not a valid binary value")
    hexv = hex(intv) #Changes decimal to hex
    hexv = hexv[2:] #Cuts off the '0x'
    return hexv

def hex_to_ASCII(hexv):
    try:
        return bytearray.fromhex(hexv).decode()
    except:
        sys.exit('Not a valid hex value')
