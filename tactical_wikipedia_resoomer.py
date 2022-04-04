import wikipedia
from progress.bar import IncrementalBar
import time
from colorama import Back, Fore
from translate import Translator

loading = IncrementalBar("Caricamento...", max=50)

for i in range(50):
	time.sleep(0.1)
	loading.next()
loading.finish()
def riassumi():
	input0 = input("Dannatissimo argomento da riassumere >")
	try:
		riassunto = wikipedia.summary(input0)
		print(riassunto)
		print("--------------------------------------")
	except:
		print(Back.RED, Fore.WHITE, "Errore: Argomento Inesistente (404)")
		print(Style.RESET_ALL)
	another_barraofcaricamento = IncrementalBar("Traducendo...", max=50)
	print("Seleziona from_lang (Lingua da tradurre) a to_lang (Lingua della traduzione)")
	input1 = input("From Lang (Default: En) >  ")
	input2 = input("To Lang (Default: it) > ")
	default_from_lang = "en"
	default_to_lang = "it"
	for i in range(50):
		time.sleep(0.1)
		another_barraofcaricamento.next()
	another_barraofcaricamento.finish()
	try:
		traduttore = Translator(from_lang = input1, to_lang = input2)
	except:
		traduttore = Translator(from_lang = default_from_lang, to_lang = default_to_lang)
	riassunto_tradotto = traduttore.translate(riassunto)
	print(riassunto_tradotto)
riassumi()
while True:
	input3 = input("Vuoi riassumere altri argomenti di Wikipedia? [Y/N] > ")
	if input3 == "yes" or "YES" or "Y" or "y":
		riassumi()
	else:
		exit()

