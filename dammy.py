
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle


greek_dict = {
    'house': 'spiti',
    'car': 'aftokinito',
    'book': 'vivlio',
    'water': 'nero',
    'food': 'fagito',
    'friend': 'filos',
    'love': 'agapi',
    'sun': 'ilios',
    'moon': 'fengari',
    'tree': 'dentro',
    'sky': 'ouranos',
    'flower': 'louloudi',
    'mountain': 'vouno',
    'river': 'potami',
    'city': 'poli',
    'dog': 'skylos',
    'cat': 'gata',
    'music': 'mousiki',
    'family': 'oikogeneia',
    'dream': 'oneiro'
}

italian_dict = {
    'house': 'casa',
    'car': 'auto',
    'book': 'libro',
    'water': 'acqua',
    'food': 'cibo',
    'friend': 'amico',
    'love': 'amore',
    'sun': 'sole',
    'moon': 'luna',
    'tree': 'albero',
    'sky': 'cielo',
    'flower': 'fiore',
    'mountain': 'montagna',
    'river': 'fiume',
    'city': 'citta',
    'dog': 'cane',
    'cat': 'gatto',
    'music': 'musica',
    'family': 'famiglia',
    'dream': 'sogno'
}

spanish_dict = {
    'house': 'casa',
    'car': 'coche',
    'book': 'libro',
    'water': 'agua',
    'food': 'comida',
    'friend': 'amigo',
    'love': 'amor',
    'sun': 'sol',
    'moon': 'luna',
    'tree': 'árbol',
    'sky': 'cielo',
    'flower': 'flor',
    'mountain': 'montaña',
    'river': 'río',
    'city': 'ciudad',
    'dog': 'perro',
    'cat': 'gato',
    'music': 'música',
    'family': 'familia',
    'dream': 'sueño'
}

german_dict = {
    'house': 'haus',
    'car': 'auto',
    'book': 'buch',
    'water': 'wasser',
    'food': 'essen',
    'friend': 'freund',
    'love': 'liebe',
    'sun': 'sonne',
    'moon': 'mond',
    'tree': 'baum',
    'sky': 'himmel',
    'flower': 'blume',
    'mountain': 'berg',
    'river': 'fluss',
    'city': 'stadt',
    'dog': 'hund',
    'cat': 'katze',
    'music': 'musik',
    'family': 'familie',
    'dream': 'traum'
}

french_dict = {
    'house': 'maison',
    'car': 'voiture',
    'book': 'livre',
    'water': 'eau',
    'food': 'nourriture',
    'friend': 'ami',
    'love': 'amour',
    'sun': 'soleil',
    'moon': 'lune',
    'tree': 'arbre',
    'sky': 'ciel',
    'flower': 'fleur',
    'mountain': 'montagne',
    'river': 'rivière',
    'city': 'ville',
    'dog': 'chien',
    'cat': 'chat',
    'music': 'musique',
    'family': 'famille',
    'dream': 'rêve'
}


def search_translation(dictionary, word):
    return dictionary.get(word.lower(), "Word not found in the dictionary.")

class LanguageSelectionScreen(BoxLayout):
    def __init__(self, switch_to_translation, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.padding = [20, 20, 20, 20]
        self.spacing = 20
        self.size_hint = (1, 1)


        with self.canvas.before:
            Color(0.2, 0.3, 0.5, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.add_widget(Label(text="Select a Language", font_size=36, bold=True, color=(1, 1, 1, 1), size_hint=(1, 0.2)))


        for language in ['Greek', 'Italian', 'Spanish', 'German', 'French']:
            button = Button(text=language, font_size=24, size_hint=(1, 0.15), background_normal='', background_color=(0.1, 0.8, 0.3, 1))
            button.bind(on_press=lambda instance, lang=language.lower(): switch_to_translation(lang))
            self.add_widget(button)


            button.bind(on_press=self.animate_button)

    def animate_button(self, instance):

        anim = Animation(size_hint=(0.95, 0.95), duration=0.1) + Animation(size_hint=(1, 1), duration=0.1)
        anim.start(instance)

class TranslationScreen(BoxLayout):
    def __init__(self, language, switch_to_language_selection, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        self.language = language
        self.add_widget(Label(text=f"Enter a word to translate to {language.capitalize()}:", font_size=20))

        self.word_input = TextInput(hint_text="Word", multiline=False)
        self.add_widget(self.word_input)

        self.translate_button = Button(text="Translate", font_size=18, size_hint=(1, 0.2))
        self.translate_button.bind(on_press=self.translate_word)
        self.add_widget(self.translate_button)

        self.result_label = Label(text="", font_size=20)
        self.add_widget(self.result_label)

        self.back_button = Button(text="Back", font_size=18, size_hint=(1, 0.2))
        self.back_button.bind(on_press=lambda instance: switch_to_language_selection())
        self.add_widget(self.back_button)

    def translate_word(self, instance):
        word = self.word_input.text.strip()
        if self.language == 'greek':
            translation = search_translation(greek_dict, word)
        elif self.language == 'italian':
            translation = search_translation(italian_dict, word)
        elif self.language == 'spanish':
            translation = search_translation(spanish_dict, word)
        elif self.language == 'german':
            translation = search_translation(german_dict, word)
        elif self.language == 'french':
            translation = search_translation(french_dict, word)
        else:
            translation = "Invalid language."

        self.result_label.text = f"Translation: {translation}"

class LanguageDictionaryApp(App):
    def build(self):
        self.sm = ScreenManager()

        self.language_selection_screen = Screen(name="language_selection")
        self.translation_screen = Screen(name="translation")

        self.sm.add_widget(self.language_selection_screen)
        self.sm.add_widget(self.translation_screen)

        self.show_language_selection()
        return self.sm

    def show_language_selection(self):
        layout = LanguageSelectionScreen(self.switch_to_translation)
        self.language_selection_screen.clear_widgets()
        self.language_selection_screen.add_widget(layout)
        self.sm.current = "language_selection"

    def switch_to_translation(self, language):
        layout = TranslationScreen(language, self.show_language_selection)
        self.translation_screen.clear_widgets()
        self.translation_screen.add_widget(layout)
        self.sm.current = "translation"

if __name__ == '__main__':
    Window.size = (600, 800)
    Window.clearcolor = (0.1, 0.1, 0.1, 1)  
    LanguageDictionaryApp().run
