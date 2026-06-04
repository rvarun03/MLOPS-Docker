from deep_translator import GoogleTranslator

def translate_text(text: str, target_language: str):
    translated=GoogleTranslator(
        source='auto',
        target=target_language
    ).translate(text)
    return {
        "original_text": text,
        "target_language": target_language,
        "translated_text": translated 
    }