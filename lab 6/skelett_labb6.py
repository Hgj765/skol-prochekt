# Daniel wickleus,Yousif Rasool
# 20/09/2025
# Det här programmet håller koll på influencers. Läser in dessa från fil, kan göra inlägg etc för att ändra sina siffror och allt sparas på fil innan programmet avslutas.

from datetime import *  # datetime används för datumhantering
from symtable import Class

# Klassdefinition
"""En klass som beskriver en influencer. Ett objekt av klassen har attributen användarnamn(str), antal_föjare(int), datum_senaste_inlägg(date), intäkter(float)"""


class Influencer:
    def __init__(self, användarnamn, antal_föjare, datum_senaste_inlägg,
                 intäkter):  # skapa klass influencer och de fyra attributer
        self.användarnamn = str(användarnamn)
        self.följare = int(antal_föjare)
        self.date = (datum_senaste_inlägg)
        self.intäkter = float(intäkter)

    def __str__(self):
        return f"{self.användarnamn} har {self.följare} kämer {self.intäkter}"

    def __lt__(self, other):
        return self.intäkter < other.intäkter

    def gör_inlägg(self):
        print(f"""{self.användarnamn} har postat om sin dag med en bild på sin katt
{self.användarnamn}s senaste inläg var {self.date} och de har {self.följare} antal följare
senaste inlägg updateras till dagens datum:{datetime.now().strftime("%Y-%m-%d")} och {self.användarnamn} har nu {self.följare + 100} följare""")
        self.följare += 100
        self.date = datetime.now().strftime("%Y-%m-%d")

    def gör_reklam(self):

        if self.följare >= 50:
            print(f"{self.användarnamn}s inkomst gick presis upp med 100 men förlorade 50 följare")
            print(
                f'senaste inlägg:{datetime.now().strftime("%Y-%m-%d")} och {self.användarnamn} har nu {self.följare + 100} följare och {self.intäkter}sek inkomst')
            self.intäkter += 100
            self.följare -= 50
        elif self.följare <= 50:
            print(f"{self.användarnamn} har för få följare, kanche borde göra fler inläg först")

    # konstruktor def

    # str-metod

    # lt-metod

    # gör_inlägg-metod

    # gör_reklam-metod

    def vald_influencer(self):  # hjälpmetod för utskrift, låt den vara kvar i klassen
        """Skriver ut att influencern valts.
        Parameter: self
        Returvärde: inget"""
        print("Hittade " + self.användarnamn + " profil, vad ska jag göra nu?")


def läs_influencers(filnamn):
    """Funktion för att läsa in alla influencers som finns i filen och utifrån det skapa objekt av klassen ovan.
       Inparameter: filnamn - namn på filen som innehåller datat om alla influencers (str).
       Returvärde: influencerlista - alla influencerssobjket (lista)"""
    infil = open(filnamn, "r", encoding="utf-8")
    influencerlista = []
    for rad in infil:
        rad = rad.strip()
        delar = rad.split(" ")
        influencer = Influencer(delar[0], int(delar[1]), date.fromisoformat(delar[2]), float(delar[3]))
        influencerlista.append(influencer)
    return influencerlista


def välj_aktivitet():
    """Funktion för att välja aktivitet som influencern ska utföra under menyval 2.
    Parameter: Ingen
    Returvärde: valet som användaren matar in (int)"""
    val = int(input("\n\t1. Be influencern att göra inlägg \
                     \n\t2. Be influencern göra reklam \
                     \n\t3. Återgå till huvudmenyn \
                     \n\tVad väljer du? "))
    return val


def utför_aktivitet(namn_influencer, influencerlista):
    """Funktion för att utföra aktivitet som användaren valt.
    Inparameter: namn_influencer - namn som användaren valt att leta upp (str), influencerLista - alla influencers (lista)
    Returvärde: Inget, funktionen anropar antingen metoden gör_inlägg() eller gör_reklam() samt funktionen välja_aktivitet() beroende på vad användaren matat in."""
    for i in range(len(influencerlista)):
        if influencerlista[i].användarnamn == namn_influencer:
            influencer = influencerlista[i]
            val = välj_aktivitet()
            while val != 3:
                if val == 1:
                    influencer.gör_inlägg()
                elif val == 2:
                    influencer.gör_reklam()
                else:
                    print("Du har inte angett en siffra mellan 1-3, vänligen försök igen")
                val = välj_aktivitet()


def spara(filnamn, influencerlista):
    """Funktion för att spara status på alla influencers
    Inparameter: filnamn på filen (str), influencerlista) (lista med Influencer-objekt)
    Returvärde: inget returvärde då filen sparas i funktionen"""
    with open(filnamn, "w") as fil:
        for rows in influencerlista:
            print(rows)
            fil.write(f"{rows.användarnamn} {rows.följare} {rows.date} {rows.intäkter}\n")


def huvudfunktion():
    """Funktion som hälsar välkommen samt visar huvudmenyn"""

    filnamn = "influencers.txt"
    lista = läs_influencers(filnamn)
    lista.sort()
    val = 0
    print("Välkommen till Influenceramera! Vad kan jag stå till tjänst med?")
    while val != 3:
        print("\n Du har följande alternativ: \
              \n\t1. Lista alla influencers och deras status\
              \n\t2. Leta upp en influencers profil\
              \n\t3. Spara och avsluta\
              \n\tVad väljer du? ", end="")
        try:
            val = int(input())
        except ValueError:
            print("Det där var tyvärr inte ett giltigt menyval, försök igen")
            continue
        if val == 1:
            lista.sort()
            print()
            for influencer in lista:
                print(influencer)
        elif val == 2:
            profil = input("\nVilken profil vill du att jag letar upp?: ")
            utför_aktivitet(profil, lista)
        elif val == 3:
            print("Programmet avslutas. Tack för att du använder Influenceramera!")
        else:
            print("Du har inte angett en siffra mellan 1-3, försök igen.")

    spara(filnamn, lista)


huvudfunktion()