"""when input any name the program will take every letter of the name and translate it to phonetic alphabet"""
import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
letter_code = {row.letter: row.code for (index, row) in data.iterrows()}
def phonetic_alphabet():
    text = input("Enter a word: ").upper()
    try:
        phonetic_list = [letter_code[letter] for letter in text]

    except KeyError:
        print("Sorry, only letters are allowed")
        phonetic_alphabet()
    else:
        print(phonetic_list)
phonetic_alphabet()
