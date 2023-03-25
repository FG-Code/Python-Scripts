from googletrans import Translator, constants
from pprint import pprint
translator = Translator()
translation = translator.translate("Wie gehts", dest="en")
print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
pprint(translation.extra_data)
