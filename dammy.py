
greek_dict = {
    "hello": "geia sas",
    "goodbye": "antio",
    "please": "parakalo",
    "thank you": "efharisto",
    "yes": "nai",
    "no": "ochi",
    "how are you?": "pos eisai?",
    "fine": "kala",
    "home": "spiti",
    "friend": "filos",
    "king": "vasilias",
    "eat": "troo",
    "book": "vivlio",
    "here": "edo",
    "there": "ekei",
    "name": "onoma",
    "water": "nero",
    "school": "scholeio",
    "love": "agapi",
    "day": "imera"
}

def search_english_to_greek(word):
    translation = greek_dict.get(word.lower())
    return translation if translation else "Word not found in the Greek dictionary."


print("Greek Dictionary is now available.")
search_term = input("Enter an English word to translate to Greek: ")


result = search_english_to_greek(search_term)
print(f"Translation: {result}")

