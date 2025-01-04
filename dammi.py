italian_to_english = {
    "ciao": "hello",
    "amore": "love",
    "casa": "house",
    "famiglia": "family",
    "libro": "book",
    "gatto": "cat",
    "cane": "dog",
    "scuola": "school",
    "macchina": "car",
    "albero": "tree",
    "sole": "sun",
    "luna": "moon",
    "acqua": "water",
    "pane": "bread",
    "formaggio": "cheese",
    "vino": "wine",
    "pizza": "pizza",
    "salve": "hello (formal)",
    "scendere": "to go down",
    "salire": "to go up"
}
def get_translation(word):
    if word in italian_to_english:
        return f"The translation of '{word}' is: {italian_to_english[word]}"
    else:
        return f"Sorry, the word '{word}' is not in the dictionary."

word_to_lookup = input("Enter a italy word to get its English translation: ")
print(get_translation(word_to_lookup.lower()))