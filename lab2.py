#tilåter andvendaren att velga en enhet
#som ska konverteras och sen konverterar och printar
while True:
    print("welcome, välja en av följande")
    val=(input("1: konvertera celsius till fahrenhiet \n 2: km till amerikanska mil \n 3: pounds till kilogram \n 4: avsluta \n"))
    try:
        if 1<= int(val) <=3:
            val=int(val)
            konvertering =float(input("hur mycket ska konverteras"))
            if val == 1:
                print(konvertering*1.8+32,"Fahrenheit\n\n")
            elif val == 2:
                print(konvertering/1.6093, "mil\n\n")
            elif val == 3:
                print(konvertering*2.2046,"kg\n\n")
        elif int(val) == 4:
            break
        else:
            print("Inte ett alternativ")
    except:
        print("Inte ett alternativ")