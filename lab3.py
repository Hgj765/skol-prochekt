#Daniel wickleus, Douglas Casteel 2025-09-09
#basic meny program som låter dig printa medlemar, legga till och ta bort medlemar
#samt se orförande för gruperna
print("Välkommen till programmet som håller koll på dina grupper!")
# Här behövs en konstant
grupper = {}
ANTAL_GRUPPER = 3

ständig_medlem = input("Vad heter du? ")
for i in range(ANTAL_GRUPPER):  # skriv klart for-satsen
    gruppnamn = input("Vad heter grupp nr " + str(i + 1) + "? ")
    grupper[gruppnamn] = [ständig_medlem]
#printar alla gruper och medlemar i gruperna
def grupprint():
    for i in grupper:
        print(i)
        for n in grupper[i]:
            print("\t", n)


val = 0
while val != 5:
    print("Huvudmeny\n1. Se alla grupper och dess medlemmar\
  \n2. Lägg till medlem i en grupp\
  \n3. Ta bort en medlem ur en grupp\
  \n4. Se vem som är ordförande i varje grupp\
  \n5. Avsluta")
    val = int(input("Vad vill du göra? "))

    if val == 1:
        grupprint()


    elif val == 2:
        grupp= str(input("vilken grup vill du legga till i"))
        if grupp in grupper:
            person=input("vem vill du legga till i grupen")
            if person in grupper[grupp]:
                print("\n")
                print(f"{person} fins redan i grupen")
                print("\n")
            elif person not in grupper[grupp]:
                grupper[grupp].append(person)
                grupprint()

        elif grupp not in grupper:
            print("\n")
            print("gruppen fins inte")
            print("\n")
    elif val == 3:
        grupp = str(input("vilken grup vill du ta bort från"))
        if grupp in grupper:
            person = str(input("vem vill du ta bort"))
            if person  not in grupper[grupp]:
                print(f"{person} fins inte")
            elif person in grupper[grupp]:
                if person == grupper[grupp][0]:
                    print("\n")
                    print("du får inte ta bort ordförande i grupen")
                    print("\n")
                elif person != grupper[grupp][0]:
                    grupper[grupp].remove(person)
                    grupprint()


        elif grupp not in grupper:
            print("\n")
            print("gruppen fins inte")
            print("\n")


    elif val == 4:
        for grupp in grupper:
            ordförande =grupper[grupp][0]
            for i in grupper[grupp]:
                if len(i) > len(ordförande):
                    ordförande = i


            print("\n")
            print(f"{grupp}s ordförande är {ordförande}")
            print("\n")

    elif val == 5:
        print("\n")
        print("Programmet avslutas")
        print("\n")

    else:
        print("\n")
        print("inte ett alternativ")
        print("\n")