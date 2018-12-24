'''
Created on Dec 23, 2018

@author: Vladimir
'''

def ucitajStudente():
    for linija in open("trenutniKandidati.txt", "r"):
        student=stringUStudenta(linija)
        studenti.append(student)

def stringUStudenta(linija):
    if linija[-1]=="\n":
        linija=linija[:-1]
    korisnickoi,sifra,ime,prezime,datum,fakultet,godina,prosek,brbodova,ekstatus,zelja=linija.split("|")
    student={
        "korisnicko_ime":korisnickoi,
        "sifra":sifra,
        "ime":ime,
        "prezime":prezime,
        "datum_rodjenja":datum,
        "fakultet":fakultet,
        "godina":godina,
        "prosek":prosek,
        "broj_espb":brbodova,
        "mesecno_primanje":ekstatus,
        "zelja":zelja,
        "bodovi":0
    }
    return student    
    
def racunanjeBodova(student):
    rezultat=(float(student["prosek"])*8)+((int(student["broj_espb"])/int(student["godina"]))*0.8)
    if float(student["mesecno_primanje"])<=15000:
        rezultat+=1
    return rezultat
            
    
print(__name__)
studenti=[]  
ucitajStudente();