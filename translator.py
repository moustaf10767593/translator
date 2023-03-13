import requests

def translate_text(text, target_language):
    api_key = 'your_api_key' # замените на ваш ключ API
    url = f'https://translation.googleapis.com/language/translate/v2?key={api_key}'
    payload = {'q': text, 'target': target_language}
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        data = response.json()['data']
        translations = data['translations']
        translated_text = translations[0]['translatedText']
        return translated_text
    else:
        return 'Error: Could not translate text.'

if __name__ == '__main__':
    text = input('Enter text to translate: ')
    target_language = input('Enter target language (e.g. en for English, es for Spanish): ')
    print(translate_text(text, target_language))
