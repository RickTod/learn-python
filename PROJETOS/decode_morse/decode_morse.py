'''
O script tem a finalidade de decifrar uma mensagem em código morse e exibir em texto claro.
'''
import sys
from config import dict_morse

def decode_morse(msg):
    '''
    input : mensagem em código morse com as letras separadas por espaços e palavras por dois espaços
    output : texto em claro com letras e algarismos
    '''
    words = msg.split("  ")  
    decoded_words = []
    
    for word in words:
        letters = word.split(" ")
        decoded_word = "".join([dict_morse.get(letter, '') for letter in letters])
        decoded_words.append(decoded_word)
     
    return " ".join(decoded_words)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Por favor, forneça a mensagem em código morse como argumento.")
        sys.exit(1)
    
    morse_msg = sys.argv[1]
    msg_claro = decode_morse(morse_msg)
    print("Mensagem decifrada:", msg_claro)
