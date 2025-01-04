# team-collab
#a project for different language
# french dictionary
french_dict = {
    "bonjour": "hello",
    "au revoir": "goodbye",
    "s'il vous plaît": "please",
    "merci": "thank you",
    "oui": "yes",
    "non": "no",
    "comment ça va?": "how are you?",
    "ça va bien": "fine",
    "maison": "home",
    "ami": "friend",
    "roi": "king",
    "manger": "eat",
    "livre": "book",
    "ici": "here",
    "là-bas": "there",
    "nom": "name",
    "eau": "water",
    "école": "school",
    "amour": "love",
    "jour": "day"
}


def search_french(word):
    translation = french_dict.get(word)
    return translation if translation else "Word not found in the French dictionary."


print("French Dictionary is now available.")
search_term = input("Enter a French word to translate to English: ")


result = search_french(search_term)
print(f"Translation: {result}")
