website_url = "" # Replace later with portfolio website when finished. 
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def printIntro():
    print("Caesar Cipher Hacker, by Nithin Rajesh " + website_url + "\n")

def decrypt_message(message, key):
    # Got it from my Caesar Cipher Project.
    decrypted_message = ""
    for letter in message:
        letter = letter.upper()
        if(letter not in alphabet):
            decrypted_message += letter
            continue
        if(alphabet.index(letter) - key < 0):
            letter = alphabet[len(alphabet) - alphabet.index(letter)]
        else:
            letter = alphabet[alphabet.index(letter) - key]
        decrypted_message += letter
    return decrypted_message