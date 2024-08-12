import os

from dotenv import load_dotenv
from simpleaitranslator.translator import set_openai_api_key, get_text_language, translate


load_dotenv()
set_openai_api_key(os.getenv("OPENAI_API_KEY"))

# Detect language
print(get_text_language("Czesc jak sie masz"))  # Output: 'pol'

# Translate text
print(translate("Cześć jak się masz? Meu nome é Adam", "eng"))  # Output: "Hello how are you? My name is Adam"