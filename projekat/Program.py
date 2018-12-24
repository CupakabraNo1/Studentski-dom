'''
Created on Dec 23, 2018

@author: Vladimir
'''
import random


def main():
    print("Dobrodosli u program studenskog centra za raspodelu domova")
    ispisiMeni()
    operacija=input("Molimo Vas da odaberete slovo koje reprezentuje zeljenu opciju:").strip()
    while operacija != 'k':
        if operacija=='a' or operacija=='b'or operacija=='c'or operacija=='d':
            uradi(operacija)
            ispisiMeni()
            operacija=input("Sledace: ")
        else:
            ispisiMeni() 
            operacija=input("Pogresna komanda. Pokusajte ponovo: ").strip()
    
    print("Hvala na koriscenju naseg programa.")
def uradi(operacija):
    if operacija=='a':
        prijava()
    elif operacija=='b':
        pretraga()
    elif operacija=='c':
        rangLista()
    elif operacija=='d':
        brojaSlMesta()
    else :
        print()

def ispisiMeni():
    print("Moguce opcije su:")
    print("a) Prijava kandidata za studentski dom.")
    print("b) Pretraga trenutno rasporedjenih kandidata.")
    print("c) Ispis rang liste odredjenog doma.")
    print("d) Broj preostalih slobodnih mesta u domovima.")
    print("Za zavrsetak rada unesite k")
    print()
    
def prijava():
    print("Dobro dosli u meni za prijavu studenta za dom.")
    print("Uneti potrebne podatke za prijavu: ")
    
    ime=input("Ime: ")
    prezime=input("Prezime: ")
    datumr=input("Datum rodjenja formata (dd.mm.gggg): ")
    fakultet=input("Fakultet: ")
    godina=input("Godina studija: ")
    prosek=input("Prosek ostvaren u prethodnoj godini: ")
    brbodova=input("Broj ESPB ostvaren u prethodnoj godini: ")
    primanje=input("Primanje na mesecnom nivou: ")
    zelja=input("Oznaka zeljenog doma: ")
    #projekat.Domovi.prijava(ime, prezime, datumr, fakultet, godina, prosek, brbodova, primanje, zelja)
    print()
    
    korisnickoime=ime[:4]+prezime[:3]
    dr=datumr.split('.')
    a='';
    for i in dr:
        a+=str(i)
    sifra=ime[:1]+prezime[:1]+fakultet[:-3]+a+str(random.randint(0, 100))
    print("Vase korisnicko ime je: "+korisnickoime)
    print(",a lozinka: "+sifra)
    print()

def pretraga():
    return
def rangLista():
    return
def brojaSlMesta():           
    return

print(__name__)
if __name__ == '__main__':
    main()