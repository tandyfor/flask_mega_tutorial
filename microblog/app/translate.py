import requests
from flask import current_app
from flask_babel import _


def translate(text, source_language, dest_language):
    if not current_app.config['YANDEX_CLOUD_TRANSLATOR_API_KEY'] or not current_app.config['YANDEX_CLOUD_TRANSLATOR_CATALOG_ID']:
        return _('Error: the translation service is not configured.')
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Api-Key {0}".format(current_app.config['YANDEX_CLOUD_TRANSLATOR_API_KEY']),
        }
    body = {
        "targetLanguageCode": dest_language,
        "texts": text,
        "folderId": current_app.config['YANDEX_CLOUD_TRANSLATOR_CATALOG_ID'],
        "sourceLanguageCode": source_language
        }
    response = requests.post(
        "https://translate.api.cloud.yandex.net/translate/v2/translate",
        json=body,
        headers=headers,
    )
    if response.status_code != 200:
        return _('Error: the translation service failed.')
    return response.json()['translations'][0]['text']