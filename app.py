import pickle
import os
from googletrans import Translator, constants
from pprint import pprint

from flask import Flask, request, jsonify

app = Flask(__name__)

try:
    translator = Translator()
    print('Translator initialized successfully')
except Exception as e:
    print(str(e))


@app.route('/LanguageTranslatorEngine', methods=['POST'])
def languagetranslatorengine():
    str_input = request.json['str_inputvalue']
    dest_Language = request.json['str_destLang']
    TranslatedText = translator.translate(str_input,dest=dest_Language)
    return jsonify({'results': TranslatedText.text})


if __name__ == "__main__":
    app.run()
