import datetime

date = datetime.datetime.now()

print(f"Ciao dal container gruppo 2, per noi oggi è{date}")
segno = ["Scimmia","Gallo","Cane","Maiale","Topo","Bue","Tigre"\
,"Coniglio","Drago","Serpente","Cavallo","Capra"]

i = int(input("Inserisci un anno:\n"))
n = i%12
print(F"Sei del {segno[n]}\n")
