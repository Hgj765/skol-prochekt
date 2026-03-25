# Titel: Periodiska systemet
# Uppgifts nr. 178
# Författare: Elina Ejner
# Datum: 2025-11-17
# Kurskod: DD1310


# Det här är ett träningsprogram för periodiska systemet.
# Programmet hämtar atomdatan från en fil med namnet "aviktE.txt"
# Programmet hämtar rad- och kolumndatan från en fil med namnet "rad_och_kolumn.txt"


# Grundämne-objekten lagras i en lista grundämne_lista

# En klass som beskriver ett Grundämne:
#    atombeteckning: atombeteckning (sträng)
#    atomnummer: atomnumret  (integer)
#    atomnamn: namnet på grundämnet (sträng) 
#    atomvikt: vikten på atomen/grundämnet (float)
#    rad: rad i periodiska systemet    (sträng)
#    kolumn: kolumn i periodiska systemet    (sträng)

#   På alternativ 6 saknas några ämnen i periodiska systemet eftersom given fil inte hade
#   med alla ämnen. Den kompletta ramen är utritad för att underlätta tillägget av fler ämnen.

#   Egna anteckningar:
#   ALLMÄNNA FRÅGOR:
#   -

#   ATT GÖRA:
#   -DU ANVÄNDER CAMELCASE OCH SNAKECASE!!!!! OLAGLIGT , kanske åtgärdat INTE
#
import random

class Grundämne:
    def __init__(self, atombeteckning,atomnummer,atomnamn,atomvikt,rad,kolumn):
        """Skapar ett nytt Grundämne-objekt.
        Inparametrar: self, atombeteckning (str),atomnummer(int),atomnamn(str),atomvikt(float),rad(str),kolumn(str)"""
        self.atombeteckning = atombeteckning
        self.atomnummer = int(atomnummer)
        self.atomnamn = atomnamn
        self.atomvikt = float(atomvikt)
        self.rad = rad
        self.kolumn = kolumn
        
    def __str__(self):
        """Returnerar en sträng med info om grundämnet.
        Inparametrar: Inga
        Utparametrar: en sträng med info om grundämnet (str)""" 
        return str(self.atomnummer) + " " + self.atomnamn

    def __lt__ (self, other):
        """Sorterar alla grundämneobjekt efter atomnummer.
        Inparametrar: other
        Returnerar: booleanskt värde: True/False"""
        if self.atomnummer < other.atomnummer:
            return True
        else:
            return False

#------Funktioner------#

def läs_in(filnamn1,filnamn2):
    """läser från två olika filer och skapar en lista med grundämne-objekt.
    Inparameter: filnamn1(innehåller atombeteckning,atomnummer,atomnamn,atomvikt och atomnumme)(str), filnamn2(innehåller rad och kolumn för varje ämne)(str)
    Returnerar: grundämne_lista (Grundämne-objekt) """
    with open(filnamn1, "r", encoding = 'utf-8') as atominfo_fil:
        with open (filnamn2, "r", encoding = 'utf-8') as position_i_Psys_fil:
            grundämne_lista = []
            rad_info = atominfo_fil.readline().strip()
            rad_position = position_i_Psys_fil.readline().strip("\t")
            while rad_info != "":                                         #behöver bara ha ena då de är lika långa      
                rad_info = rad_info.split()
                rad_position = rad_position.split()
                
                grundämne = Grundämne(rad_info[0],rad_info[1],rad_info[2],rad_info[3],rad_position[0],rad_position[1])     
                grundämne_lista.append(grundämne)
                
                rad_info = atominfo_fil.readline().strip()
                rad_position = position_i_Psys_fil.readline().strip()
                
    return grundämne_lista


def huvudmeny(lista): 
    """Skriver ut menyn.
    Inparameter: ingenting
    Returnerar: ingenting """
    val = ""
    print("Välkommen till Periodiska Systemet-Spelet\n")
    while val != "7":
        print("-----------------HUVUDMENY-----------------")   
        print("Vad vill du göra? Välj 1-7 nedan:")
        print('''1. Skriv ut alla grundämnen \n2. Träna atomnummer \n3. Träna atombeteckningar\n4. Träna atomnamn\n5. Träna atomvikt\n6. Träna rader och kolumner\n7. Avsluta''')
        print("-------------------------------------------\n")
        val = input("Vad väljer du?")

        if val == "1":
            print("Du valde 1: Lista på grundämnen:")
            skriv_ut_grundämnen(lista)
        elif val in {"2", "3", "4"}:
            spela_atomnummer_beteckning_och_atomnamn(val, lista)
        elif val == "5":
            spela_atomvikt(lista)
        elif val == "6":
            spela_rad_och_kolumn(lista)
        elif val == "7":
            print("Du valde 7, programmet avslutas.")
        else:
            print("Ogiltigt menyval. Försök igen")

        
def välja_spelstruktur(val,lista):
    """Startar rätt sorts frågespel genom att anropa rätt metod beroende på användarens svar.
    Inparametrar: val (str),lista (lista med Grundämne-objekt)
    Returparametrar: Inga"""
    pass


def spela_atomnummer_beteckning_och_atomnamn(val,lista): 
    """Kör frågesporterna för atomnummer, atombeteckning och atomnamn tills använadren vill gå tillbaka till huvudmenyn.
    Inparametrar: val (str), lista (lista med Grundämne-objekt)
    Utparametrar: Inga"""
    if val == "2":
        spelord = "atomnummer"
        gramatik = "vilket"
    elif val == "3":
        spelord = "atombeteckning"
        gramatik = "vilken"
    elif val == "4":
        spelord = "atomnamn"

    print("Du valde " + val + ": Träna på " + spelord + ".")  
    print("Svara 'avsluta' för att gå tillbaka till huvudmenyn.")
    if val == "3":
        print("Var nogrann med stora och små bokstäver.")
    svar = ""
    while svar.lower() != "avsluta":
        tom_lista = []         #obligatorisk parameter till slumpa_fram_grundämne() men har ingen effekt här (än)
        a_beteckning, a_nummer, a_namn, a_vikt, a_rad, a_kolumn = slumpa_fram_grundämne(lista,tom_lista)
        if val == "2":
            spelvariabel = a_nummer
        elif val == "3":
            spelvariabel = a_beteckning
        elif val == "4":
            spelvariabel = a_namn
        print(f"({a_beteckning} {str(a_nummer)} {a_namn} {str(a_vikt)} \n") # Testing och felsökning
        if val == "4":
            svar = input("\nVilket namn har grundämnet med atomnummer " + str(a_nummer) + "?\nSvara med stor bokstav i början:")
        else:
            svar = input("\n" + gramatik[0].upper()+ gramatik[1:] + " " + spelord + " " + "har " + a_namn + "?")  
    
        tre_försök(spelvariabel,svar)

                
def tre_försök(spelvariabel,svar):
    """Frågar om atomnummer/atombeteckning/atomnamn tills användaren antingen svarar rätt, väljer att avsluta eller har svarat tre gånger. Då visas svaret.
    Inparametrar: spelvariabel(str), svar(str)
    Utparametrar: Inga"""
    antal_försök = 0     
    while antal_försök < 3 and svar.lower() != "avsluta":
        antal_försök += 1
        if svar == str(spelvariabel):               
            print("Rätt svar!")
            break
        elif svar.lower() == "avsluta":
            print("Svaret var: " + str(spelvariabel) + ".\n")
            break
        elif antal_försök == 3:
            print("Fel svar,du har slut på chanser, svaret var: " + str(spelvariabel) + ".") #lite här är inte obligatoriskt
        else:
            svar = input("Fel svar, försök igen. Du har " + str(3 - antal_försök) + " försök kvar.")  

def spela_atomvikt(lista):
    """kör quizet för atomvikten tills användaren vill gå tillbaka till huvudmenyn.
    Inparametrar: lista (lista med Grundämne-objekt)
    Utparametrar: Inga"""

    print("Du valde 5: Träna på atomvikt.")  
    print("Svara 'avsluta' för att gå tillbaka till huvudmenyn.\n")

    svar = ""
    while svar.lower() != "avsluta":
        tom_lista = []
        a_beteckning,a_nummer,a_namn,a_vikt,a_rad,a_kolumn = slumpa_fram_grundämne(lista,tom_lista)
        
        rätt_svar = a_vikt
        heltal_och_decimaler = str(rätt_svar).split(".")
        antal_decimaler = len(heltal_och_decimaler[1])
        intervall_nedre = abs(int(a_vikt - float(10)))
        intervall_övre = int(a_vikt + float(10))
        
        fel_svar_1 = float(random.randint(intervall_nedre,intervall_övre)) + random.randint(1,10 ** antal_decimaler-1)/(10 ** antal_decimaler)  
        fel_svar_2 = random.randint(intervall_nedre,intervall_övre)+ random.randint(1,10 ** antal_decimaler-1)/(10 ** antal_decimaler)
        lista_med_alternativ = [rätt_svar, fel_svar_1, fel_svar_2]
        random.shuffle(lista_med_alternativ)

        #print("Rätt",str(rätt_svar), str(fel_svar_1), str(fel_svar_2))  ###FÖR FELSÖKNING


        svar = input("Vilken atomvikt har " + a_namn + "? Svara något av de nedanstående alternativen:\n" + str(lista_med_alternativ[0]) + "\t " + str(lista_med_alternativ[1]) + "\t " + str(lista_med_alternativ[2])+"\n")
        if svar.lower() == str(rätt_svar):
            print("Rätt svar!")
        elif svar.lower() == "avsluta":
            break
        else:
            print("Fel, svaret var:" + str(rätt_svar) + "\n")


def spela_rad_och_kolumn(lista):
    """Sköter spelloopen för alternativ 6 tills användaren väljer att gå tillbaka till huvudmenyn.
    Inparametrar: lista (lista med alla Grundämne-objekt)
    Utparametrar: Inga"""
    
    print("Du valde 6: Rader och kolumner:")
    print("Din uppgift är att fylla i detta periodiska system genom\n att svara rätt på vilken rad och kolumn alla ämnen tillhör.")
    print("Svara 'avsluta' för att gå tillbaka till huvudmenyn.\n")

    matris_fullt_periodiskt_system, spel_matris = skapa_periodiska_system_matriser()
    rita_upp_periodiska_systemet(lista,matris_fullt_periodiskt_system,spel_matris)
    print("Lycka till!\n")
    lista_med__rätta_svar = []
    svar_rad = ""
    svar_kolumn = ""
    while (svar_rad.lower() != "avsluta" and svar_kolumn.lower() != "avsluta") and matris_fullt_periodiskt_system != spel_matris:
        a_beteckning,a_nummer,a_namn,a_vikt,a_rad,a_kolumn = slumpa_fram_grundämne(lista,lista_med__rätta_svar)
        print("\nFusk: rad " ,a_rad,a_kolumn , " kolumn\n")###FÖR FELSÖKNING
        print("Vilken rad och kolumn tillhör " + a_namn + "?")
        svar_rad = input("Vilken rad?")
        if svar_rad.lower() == "avsluta":
            break
        svar_kolumn = input("Vilken kolumn?")
        if svar_kolumn.lower() == "avsluta":
            break
        elif (svar_rad == a_rad and svar_kolumn == a_kolumn):
            print("Rätt svar!")

            spel_matris[int(a_rad)-1][int(a_kolumn)-1] =  matris_fullt_periodiskt_system[int(a_rad)-1][int(a_kolumn)-1]
            lista_med__rätta_svar.append(a_nummer-1)
            rita_upp_periodiska_systemet(lista,matris_fullt_periodiskt_system,spel_matris)

        else:
            print("Fel. Rätt svar var: " , a_rad, a_kolumn)
            
        if matris_fullt_periodiskt_system == spel_matris:
            print("Du lyckades fylla hela periodiska systemet! Bra jobbat!!!")



def rita_upp_periodiska_systemet(grundämne_lista,progress_matris,matris_periodiskt_system):
    """Ritar upp ett periodiskt system med alla rätta gissningar hittils.
    Inparametrar: grundämne_lista (lista med alla Grundämne-objekt),progreess_lista (matris med alla rätta gissingar, är tom från början),
                  matris_periodiskt_system (matris med alla atombeteckningar)
    Utparametrar: Inga"""

    
    print("       Kolumn:")
    print("       1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18")
    print("Rad: ┌───┐                                                               ┌───┐")     
    rad_räknare = 0
    for rad in matris_periodiskt_system:
        rad_räknare += 1
        if (1 <= rad_räknare and rad_räknare <= 9):
            if rad_räknare == 2:
                print("     ├───┼───┐                                       ┌───┬───┬───┬───┬───┼───┤")
            elif rad_räknare == 3:
                print("     ├───┼───┤                                       ├───┼───┼───┼───┼───┼───┤")
            elif rad_räknare == 4:
                print("     ├───┼───┼───┬───┬───┬───┬───┬───┬───┬───┬───┬───┼───┼───┼───┼───┼───┼───┤")
            elif rad_räknare == 5:
                print("     ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤")
            elif rad_räknare == 6:
                print("     ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤")
            elif rad_räknare == 7:
                print("     ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤")
            elif rad_räknare == 8:   
                print("             ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐")
            elif rad_räknare == 9:   
                print("             ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤")
            if rad_räknare >= 8:
                print(" ", rad_räknare, end = "  ")
            else:
                print(" ", rad_räknare, end = "  ")
            skriva_ut_rader_i_periodiska_systemet(rad,rad_räknare,matris_periodiskt_system)
        if rad_räknare == 7:
            print("     └───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘")
    print("             └───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘")
def skriva_ut_rader_i_periodiska_systemet(rad,rad_räknare,matris_periodiskt_system):
    """Skriver ut en rad i periodiska systemet. Genom att anropa den fles gånger skrivs alla rader ut.
    Inparametrar: rad(lista med alla element(str) på respektive rad),rad_räknare(int),matris_periodiskt_system (matris med alla atombeteckningar)
    Utparametrar: Inga"""
    
    ämne_räknare = 0
    for ämne in rad:  
        ämne_räknare += 1   

        if ämne != "  ": 
            print("│", end = "")
        elif ((rad_räknare <= 3 or rad_räknare >= 1) and ämne_räknare == 5):
            print(end = "") #Jag la till en karaktär i nästnästa if-sats, därför behöver jag ta bort en för jämn utskrift. Detta behövs i rad 1,2 och 3
        else:
            print(end = " ")
        print(ämne, end=" ")
        if (ämne_räknare == 18) or (rad_räknare >= 8 and ämne_räknare == 17):
            break
        elif (matris_periodiskt_system[rad_räknare -1][ämne_räknare] == "  " and ämne != "  "):#om nästa är tom och nuvarande har innehåll

            print("│", end="")
    print("│")

def skapa_periodiska_system_matriser():
    """Skapar en matris där innehållet i varje ruta motsvarar innehållet i Periodiska systemet och en matris med samma
       format fast alla beteckningar är ersatta med ett frågetecken.
    Inparametrar: Inga
    Utparametrar: matris_fullt_periodiskt_system (matris), tom_matris (matris)"""
    #Fullt Periodiskt systemsys:  
    rad_1 = [" H","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","He"]
    rad_2 = ["Li","Be","  ","  ","  ","  ","  ","  ","  ","  ","  ","  "," B"," C"," N"," O"," F","Ne"]
    rad_3 = ["Na","Mg","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","Al","Si"," P","S ","Cl","Ar"]
    rad_4 = [" K","Ca","Sc","Ti"," V","Cr","Mn","Fe","Co","Ni","Cu","Zn","Ga","Ge","As","Se","Br","Kr"]
    rad_5 = ["Rb","Sr"," Y","Zr","Nb","Mo","Tc","Ru","Rh","Pd","Ag","Cd","In","Sn","Sb","Te"," I","Xe"]
    rad_6 = ["Cs","Ba"," *","Hf","Ta"," W","Re","Os","Ir","Pt","Au","Hg","Tl","Pb","Bi","Po","At","Rn"]
    rad_7 = ["Fr","Ra","**"," -"," -"," -"," -"," -"," -"," -"," -"," -"," -"," -"," -"," -"," -"," -"]
    rad_8 = ["  ","  ","La","Ce","Pr","Nd","Pm","Sm","Eu","Gd","Tb","Dy","Ho","Er","Tm","Yb","Lu"]
    rad_9 = ["  ","  ","Ac","Th","Pa"," U","Np","Pu","Am","Cm","Bk","Cf","Es","Fm","Md","No","Lr"]

    matris_fullt_periodiskt_system = [rad_1, rad_2, rad_3, rad_4, rad_5, rad_6, rad_7, rad_8, rad_9]
    
    #Tomt Psys: 
    tom_rad_1 = [" ?","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  "," ?"]
    tom_rad_2 = [" ?"," ?","  ","  ","  ","  ","  ","  ","  ","  ","  ","  "," ?"," ?"," ?"," ?"," ?"," ?"]
    tom_rad_3 = [" ?"," ?","  ","  ","  ","  ","  ","  ","  ","  ","  ","  "," ?"," ?"," ?"," ?"," ?"," ?"] #2 och 3 är samma
    tom_rad_4 = [" ?"," ?"," ?"," ?"," ?"," ?"," ?"," ?"," ?"," ?"," ?"," ?"," ?"," ?"," ?"," ?"," ?"," ?"]
    tom_rad_5 = [" ?"," ?"," ?"," ?"," ?"," ?"," ?"," ?"," ?"," ?"," ?"," ?"," ?"," ?"," ?"," ?"," ?"," ?"] #3 och 4 är samma
    tom_rad_6 = [" ?"," ?"," *"," ?"," ?"," ?"," ?"," ?"," ?"," ?"," ?"," ?"," ?"," ?"," ?"," ?"," ?"," ?"]
    tom_rad_7 = [" ?"," ?","**"," -"," -"," -"," -"," -"," -"," -"," -"," -"," -"," -"," -"," -"," -"," -"]
    tom_rad_8 = ["  ","  "," ?"," ?"," ?"," ?"," ?"," ?"," ?"," ?"," ?"," ?"," ?"," ?"," ?"," ?"," ?"]
    tom_rad_9 = ["  ","  "," ?"," ?"," ?"," ?"," ?"," ?"," ?"," ?"," ?"," ?"," ?"," ?"," ?"," ?"," ?"]
    
    tom_matris = [tom_rad_1, tom_rad_2, tom_rad_3, tom_rad_4, tom_rad_5, tom_rad_6, tom_rad_7,tom_rad_8,tom_rad_9]

    return matris_fullt_periodiskt_system, tom_matris

    
def slumpa_fram_grundämne(grundämne_lista,exkluderade_ämnen_lista):#######################################################################################################
    """Slumpar fram ett grundämne och returnerar alla dess attrubut.
    Inparameterar: grundämne_lista (lista med alla Grundämne-objekt), exkluderade_ämnen_lista (lista med ämnen som inte
                   ska kunna slumpas fram, används i nuläget bara till alternativ 6, annars är listan tom)
    Utparametrar: slumpat_atombeteckning (str), slumpat_atomnummer(int), slumpat_atomnamn(str), slumpat_atomvikt(float),
                  slumpad_rad(str),slumpad_kolumn(str) """
    grundämne_lista.sort()
    exluderade_ämnen_set = set(exkluderade_ämnen_lista)
    orginal_intervall = set(range(0,103))  
    ämnen_som_är_kvar = set(range(0,103)) - set(exkluderade_ämnen_lista)
    print(exluderade_ämnen_set)
    print(ämnen_som_är_kvar)

    
    slumpat_tal = random.choice(list(ämnen_som_är_kvar))
    slumpat_grundämneobjekt = grundämne_lista[slumpat_tal]
    for i in grundämne_lista:
        print(str(i),end=" ")
    print("")
    print(slumpat_tal,slumpat_grundämneobjekt.atomnamn)

    slumpat_atombeteckning = slumpat_grundämneobjekt.atombeteckning
    slumpat_atomnummer = int(slumpat_grundämneobjekt.atomnummer)
    slumpat_atomnamn = slumpat_grundämneobjekt.atomnamn
    slumpat_atomvikt = float(slumpat_grundämneobjekt.atomvikt)
    slumpad_rad = slumpat_grundämneobjekt.rad
    slumpad_kolumn = slumpat_grundämneobjekt.kolumn
    
    return slumpat_atombeteckning, slumpat_atomnummer, slumpat_atomnamn, slumpat_atomvikt, slumpad_rad, slumpad_kolumn


def skriv_ut_grundämnen(lista):
    """Skriver ut listan på grundämnen ordnade efter atomnummer
    Inparametrar: grundämne_lista
    Returnerar: ingenting"""
    lista.sort()
    for ämne in lista:
        print(ämne)


def huvudprogram():
    """Kör programmet och läser från filen"""
    filnamn1 = "aviktE.txt"
    filnamn2 = "rad_och_kolumn.txt"
    lista = läs_in(filnamn1,filnamn2)
    huvudmeny(lista)
    
    #kan jag ta bort detta?
    """Algoritm:   ej helt sann längre
    1. Läser in filen med alla grundämnen och dess data och skapar grundämne-objekt som sen sparas i en lista.
    2. Skriver ut en meny
    3. Låter användaren göra välja någon övning eller avsluta
    4. Utför valt quiz om användaren inte väljer att avsluta
    5. Upprepar steg 3-5, tills det att användaren väljer att avsluta
    6. Sparar till fil???? nej
    7. Avslutar programmet
    """

huvudprogram()






  
