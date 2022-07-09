from googletrans import Translator
import googletrans
translator=Translator()
#print(googletrans.LANGUAGES)
user_input=input("Enter the text you prefer to translate:")
pref_lang=input("Language you prefer:")
trans_tamil=""
trans_telugu=""
trans_hindi=""
if(pref_lang=="Tamil" or pref_lang=="tamil"):
   trans_tamil = (translator.translate(user_input,dest='ta').text)
   print(trans_tamil)
elif(pref_lang=="Telugu" or pref_lang=="telugu"):
   trans_telugu = (translator.translate(user_input,dest='te').text)
   print(trans_telugu)
elif(pref_lang=="Hindi" or pref_lang=="hindi"):
   trans_hindi = (translator.translate(user_input,dest='hi').text)
   print(trans_hindi)




