import googletrans
from googletrans import Translator
languages=[["English","en"],["Kannada","kn"],["Hindi","hi"],["Tamil","ta"],["Telugu","te"]]

for language in languages:
    translated = Translator().translate(language[0]+" is chosen\n", src='en', dest=language[1])
    print(f" {translated.text} ")
