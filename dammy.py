greek_dict = {
    "geia sas": "hello",
    "antio": "goodbye",
    "parakalo": "please",
    "efharisto": "thank you",
    "nai": "yes",
    "ochi": "no",
    "pos eisai?": "how are you?",
    "kala": "fine",
    "spiti": "home",
    "filos": "friend",
    "vasilias": "king",
    "troo": "eat",
    "vivlio": "book",
    "edo": "here",
    "ekei": "there",
    "onoma": "name",
    "nero": "water",
    "scholeio": "school",
    "agapi": "love",
    "imera": "day"
}

def search_greek(word):
    translation = greek_dict.get(word.lower())
    return translation if translation else "Word not found in the Greek-to-English dictionary."

search_term = input("Enter a Greek word (in English letters) to translate to English: ")

result = search_greek(search_term)
print(f"Translation: {result}")
