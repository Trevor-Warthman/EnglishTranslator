#English Translation Script

#Must install python3 and ibm watson to run

#Imports
import json
from ibm_watson import TextToSpeechV1
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


#Authenticaton
authenticator_speech = IAMAuthenticator('gNN7MbSRMDKK_GS1H62B9U4btaZUVkde82I1S25e8A-8')
text_to_speech = TextToSpeechV1(
    authenticator=authenticator_speech
)

authenticator_language = IAMAuthenticator('gpFQBkIpWtSB2EgmixnJ7EPdoGHzSmhZG2D6_q7CQV6s')
language_translator = LanguageTranslatorV3(
    version = '2018-05-01',
    authenticator=authenticator_language
)


#Service URLs
language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com/instances/89f116a6-8cf2-4934-9d4c-3431dea5d0eb')
text_to_speech.set_service_url('https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/4620d5ba-e67e-49d7-95d6-47ffb2f99f9a')


#Voice Dictionary

voiceDictionary = {
    "Arabic" : "ar-AR_OmarVoice",
    "German" : "de-DE_BirgitVoice",
    "English" : "en-GB_CharlotteV3Voice",
    "Spanish" : "es-US_SofiaVoice",
    "French" : "fr-FR_NicolasV3Voice",
    "Italian" : "it-IT_FrancescaVoice",
    "Japanese" : "ja-JP_EmiVoice",
    "Korean" : "ko-KR_YoungmiVoice",
    "Dutch" : "nl-NL_EmmaVoice",
    "Portuguese" : "pt-BR_IsabelaVoice",
    "Chinese" : "zh-CN_WangWeiVoice"
}

#Generate JSON Array of all supported voices
#list_voices(self, **kwargs)
#voices = text_to_speech.list_voices().get_result()
#print(json.dumps(voices, indent=2))

translationDictionary = {
    "Arabic" : "en-ar",
    "German" : "en-de",
    "Spanish" : "en-es",
    "French" : "en-fr",
    "Italian" : "en-it",
    "Japanese" : "en-ja",
    "Korean" : "en-ko",
    "Dutch" : "en-nl",
    "Portuguese" : "en-pt",
    "Chinese" : "en-zh",
}


################################################################################################

#Inputs
languagePrompt = "Input a language to translate to (Arabic, Chinese, Dutch, French, German, Italian, Japanese, Korean, Spanish):\n"
user_input = input("Enter input text in English: ")
language_input = input(languagePrompt)

#Translate to required language
translation_dict = language_translator.translate(
    text=user_input,
    model_id=translationDictionary.get(language_input)).get_result()
translation = translation_dict["translations"][0]["translation"]

print("\'" + user_input + "\' is \'" + translation + "\' in " + language_input)

#Convert to audio
with open('output.wav', 'wb') as audio_file:
    audio_file.write(
        text_to_speech.synthesize(
            translation,
            voice=voiceDictionary.get(language_input),
            accept='audio/wav'
        ).get_result().content)
