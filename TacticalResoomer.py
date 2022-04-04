import wikipedia
from colorama import Back, Fore
from translate import Translator
import os

os.system("figlet WikiPedia-Resoomer")

def riassumi():
	input0 = input("Wikipedia topic to summarize >")
	try:
		riassunto = wikipedia.summary(input0)
		print(riassunto)
		print("--------------------------------------")
	except:
		print(Back.RED, Fore.WHITE, "Error: Topic NOT FOUND (404)")
		print(Style.RESET_ALL)
	print("Select from_lang (Language to translate) to to_lang (Language of translation) \nDefault: from_lang: en; to_lang: it")
	input1 = input("From Lang (Default: En) >  ")
	input2 = input("To Lang (Default: it) > ")
	default_from_lang = "en"
	default_to_lang = "it"
	try:
		traduttore = Translator(from_lang = input1, to_lang = input2)
	except:
		traduttore = Translator(from_lang = default_from_lang, to_lang = default_to_lang)
	riassunto_tradotto = traduttore.translate(riassunto)
	print(riassunto_tradotto)
riassumi()
while True:
	input3 = input("Want to summarize other Wikipedia topics? [Y/N] > ")
	if input3 == "yes" or "YES" or "Y" or "y":
		riassumi()
	else:
		exit()

