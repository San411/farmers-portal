import googletrans
from googletrans import Translator
translated = Translator().translate('hindi.', src='en', dest='hin')
print(translated.text)