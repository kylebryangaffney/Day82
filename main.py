morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
    'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.',
    '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
}

def convert_char(char):
    if char in morse_code_dict:
        return morse_code_dict[char]
    else:
        return ""
    
def convert_to_morse(input_string):
    morse_words = []
    for word in input_string.split():
        next_word = " ".join(convert_char(char) for char in word)
        morse_words.append(next_word)
    return "   ".join(morse_words)


print("Welcome to the Morse Code Maker 666, patent pending")
print("Type 'Quit' to close program")
while True:
    input_string = input("Please enter the string you would like to convert to morse code:\n").upper()
    if input_string == "QUIT":
        print("Thank you for using The Morse Code Maker 666")
        break

    if not input_string.strip():
        print("Please enter a valid string")

    output_string = convert_to_morse(input_string)

    print(f"Looks like:\n {output_string}")
    