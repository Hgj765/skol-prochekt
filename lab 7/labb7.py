#Daniel Wickleus, Djivan Grigoryan
#2025-10-06

#koden tar en input på vilka recept du vill tilaga, ser vilka ingridienser den sparade filen påstår att
#recepten behöver och sparar sen de sammanlagda ingridiencerna på inköpslista.txt

from Recept import *
from Vara import *
from Inkopslista import *

def skapa_vara(text):
  """Delar upp en strängen på formatet namn; mängd enhet och skapar ett Vara-objekt:
  parametrar: text (formatet namn; mängd enhet)
  returnerar: Vara-objekt (Vara)"""
  delar = text.split(';')
  namn = delar[0].strip()
  mängd_enhet = delar[1].strip().split(' ')
  mängd = int(mängd_enhet[0])
  enhet = mängd_enhet[1]
  return Vara(namn, mängd, enhet)

def läs_in_recept(filnamn):
  """Läser in maträtter och deras ingredienser från fil till en lista
  parametrar: filnamn (str)
  returnerar: receptlista (list<Recept>)"""
  receptlista = []

  with open(filnamn, 'r', encoding='utf-8') as fil:
    for rad in fil:
      rad = rad.strip()
      maträtt, alla_varor = rad.split(':')
      maträtt = maträtt.strip()
      ingredienser = alla_varor.split(',')
      varor = []
      for vara in ingredienser:
        ingrediens = skapa_vara(vara.strip())
        varor.append(ingrediens)
      receptlista.append(Recept(maträtt, varor))
  return receptlista


def välj_recept(receptlista):
    """Ber användaren välja recept, lägger den valda recept-objekten i en ny lista som returneras
    parametrar: receptlista (list<Recept>)
    returnerar: valda_recept (list<Recept>)"""
    valda_recept_lista = []
    #recept= input("vilket resept vill du ha (om du vill ha flera måste du skilja dem med ,)")
    recept = "spaghetti, pannkakor"#debug grej
    valda_recept = recept.split(', ')
    for valt_recept in valda_recept:

        for recept in receptlista:
            if valt_recept == (recept.maträtt):
                valda_recept_lista.append(recept)

    return valda_recept_lista




  
def skapa_inköpslista(valda_recept):
    """Skapar en inköpslista efter de valda recepten, skriver ut inköpslistan på skärmen och returnerar den
    parametrar: valda_recept (list<Recept>)
    returnerar: inköpslista (Inköpslista<Recept>)"""
    namn_varor = []
    recept_dict ={}
    for recept in valda_recept:
        for ingridiencer in recept.ingredienser:
            if ingridiencer.namn not in recept_dict:
                recept_dict[ingridiencer.namn] = [0, ""]
                recept_dict[ingridiencer.namn][1] = ingridiencer.enhet

            recept_dict[ingridiencer.namn][0]+=ingridiencer.mängd

    for i in recept_dict.keys():
        namn_varor.append(i+" "+ str(recept_dict[i][0])+" "+ str(recept_dict[i][1]))




    inköpslista = Inköpslista(namn_varor) #Vårt Inköpslista-objekt som ska fyllas på med Vara-objekt och returneras.
    #print(inköpslista)
    return inköpslista
    #namn_varor = [] #Hjälp-lista där vi bara lägger in namnen på nya varor, så vi enklare kan kontrollera om en ingrediensen redan finns på inköpslistan.


    #Tips: Vi behöver kontrollera om ingrediensen redan finns i inköpslistan innan vi lägger till den.
    # Använd namn_varor för att kolla detta.
    #Om den finns ska vi anropa metoden .lägg_till_mängd för det Vara-objektet.
    # Använd namn_varor.index(x), där x är ingrediensens namn för att ta redan på vilket index den ingrediensen har i inköpslistan.
    #Annars ska vi lägga in ingrediensens namn i listan namn_varor och Vara-objektet på inköpslistan.


def skriv_till_fil(filnamn, inköpslista):
    with open(filnamn, 'w', encoding='utf-8') as fil:
        fil.write(str(inköpslista))

def main():
    recept_lista = läs_in_recept("matratter.txt")
    valda_recept= välj_recept(recept_lista)
    inköpslista =skapa_inköpslista(valda_recept)
    print((inköpslista))
    skriv_till_fil("inköpslista.txt", inköpslista)

if __name__ == '__main__':
    main()

