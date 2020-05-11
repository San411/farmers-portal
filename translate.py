from googletrans import Translator
translator = Translator()
def trans(array, source, destination):
    sample = []
    result = []
    for i in range(0,len(array)):
        sample.append(array[i].lower())
    result = translator.translate(sample, src=source, dest=destination)
    return result
