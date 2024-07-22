# Allow user to input single-byte XOR cipher
    # If not, use default
def single_byte_XOR(hex):
    if (hex == ""):
        hex = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

    import matplotlib.pylab as plt
    import pandas as pd
    import sys
    sys.path.append('Mods') # adds the folder with the functions to the files checked
    sys.path.append('Set1') # adds the folder with the functions to the files checked
    from Variables import base64, base64_English_Freq
    from Challenge1 import hex_to_base64
# Hex to base64
    base64_from_hex = hex_to_base64(hex)

# Frequency table of characters
    freq = dict()
    for char in base64[:-2]:
        char = char.lower()
        freq[char] = freq.get(char, 0)
    for char in base64_from_hex:
        if char in freq:
            freq[char] = freq.get(char) + 1
    freq_series = pd.Series(freq) / pd.Series(freq).sum()
    # print(freq_series)
    # print("\n\n\n",freq_series.sum())
    base64_English_Freq_series = pd.Series(base64_English_Freq)
    # print(base64_English_Freq_series)
    df = pd.DataFrame({"Given Hex (Red)":freq_series,"English Fingerprint (Blue)":base64_English_Freq_series})
    ax = df.plot.bar(color=["Red","Blue"], rot=0, title="When ready, press any button to enter a guess to move the red RIGHT\nPress <ENTER> to quite\n<<Answer will show here>>")
    ax.set_xlabel("Character")
    ax.set_ylabel("Frequency")
    letter = ''

    print(freq_series.shift(1))

    while True:
        plt.draw()
        if (plt.waitforbuttonpress(0) == True):
            plt.close()
        while (not letter.isdigit()):
            letter = input("Enter number:")
            if (letter == '\n'):
                break
        shift = int(letter)
        temp = freq_series[(0-shift):][0]
        freq_series = freq_series.shift(shift)
        freq_series[0] = temp



# Show frequency table to user
    # Show base64_English_Freq to user
    # Matplotlib or some data visualization? Show fingerprints against each other


# Allow user to select a shift key


# Display the base64 encoded string
# Display the base64 decoded string
# Display the hex decoded string

# Ask them if they want to try another shift key

if (__name__ == '__main__'):
    print("Note: Default value will be the string provided on the website if the string is empty")
    print(single_byte_XOR(input("Please provide the hex value: ")))
