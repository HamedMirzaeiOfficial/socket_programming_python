from googletrans import Translator

def translator(text):
    translator_object = Translator()

    # Use a try-except block to handle potential translation errors
    try:
        # Detect the language of the input text
        lang = translator_object.detect(text).lang
        
        # If the detected language is Persian, translate to English
        if lang == 'fa':
            translation = translator_object.translate(text, src='fa', dest='en')
            
            # Check if the translation result is not None
            if translation.text:
                return translation.text
            else:
                return "Translation not available."
        elif lang == 'en':
            translation = translator_object.translate(text, src='en', dest='fa')
            
            # Check if the translation result is not None
            if translation.text:
                return translation.text
            else:
                return "Translation not available."      
        else:
            return "Input text is not in Persian."
        
    except Exception as e:
        # Print the exception for debugging purposes
        print(f"Translation error: {e}")
        return "Translation error occurred."



ANSWERS = {"Hello": "hello, how are you?", 
           "How're you": "fine, thanks", 
           "Bye": "Good bye to you", 
           "Help me": "How can i help you?",
           }
