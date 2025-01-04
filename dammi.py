french_to_english = {
    "chat": "cat",
    "chien": "dog",
    "maison": "house",
    "voiture": "car",
    "arbre": "tree",
    "ami": "friend",
    "amour": "love",
    "école": "school",
    "fleur": "flower",
    "livre": "book",
    "porte": "door",
    "fenêtre": "window",
    "soleil": "sun",
    "lune": "moon",
    "mer": "sea",
    "montagne": "mountain",
    "ville": "city",
    "rue": "street",
    "temps": "weather",
    "pomme": "apple"
}
def get_translation(word):
    if word in french_to_english:
        return f"The translation of '{word}' is: {french_to_english[word]}"
    else:
        return f"Sorry, the word '{word}' is not in the dictionary."

word_to_lookup = input("Enter a french word to get its English translation: ")
print(get_translation(word_to_lookup.lower()))