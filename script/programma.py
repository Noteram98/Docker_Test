import datetime

date = datetime.datetime.now()

print(f"Ciao dal container gruppo 2, per noi oggi è {date}")

print("Vuoi sapere il tuo segno zodiacale cinese? ")
segno = ["🙊 Scimmia 🙊","🐓 Gallo 🐓","🐕 Cane 🐕","🐖 Maiale 🐖","🐁Topo🐁","🐂 Bue 🐂","🐅 Tigre 🐅"\
,"🐇 Coniglio 🐇","🐲 Drago 🐲","🐍 Serpente 🐍","🐎 Cavallo 🐎","🐐 Capra 🐐"]

i = int(input("Inserisci il tuo anno di nascita:\n"))
n = i%12

segno2 = segno[n]

if segno2 == "🙊 Scimmia 🙊" or "🐅 Tigre 🐅" or "🐐 Capra 🐐":
    print(f"Sei della {segno2}")
else:
    print(F"Sei del {segno[n]}!\n")

n2 = segno[2024%12]

print(f"Invece chi nasce quest'anno sarà del {n2} !")
