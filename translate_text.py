#!/usr/bin/python3

"""
Translate Text.
"""

from translate import Translator
# pip install translate

translator = Translator(from_lang='Spanish', to_lang='english')
result = translator.translate('Te amo')  # Enter text to translate
print(result)
