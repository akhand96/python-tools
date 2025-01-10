# installing required libraries
# pip install textblob

# importing required libraries
from textblob import TextBlob

# defining the function for spell correction
def spellCorrector(input_text):
    words = input_text.split()  # Split the input text into a list of words
    corrected_words = [TextBlob(word).correct() for word in words]  # Correct each word
    return corrected_words

# take input from the user
ip = input("Enter a word or sentence: ")

# get the corrected words
op = spellCorrector(ip)

# display the results
print("Given text: ", ip)
print("Corrected text: ", " ".join(str(word) for word in op))
