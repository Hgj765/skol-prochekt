class Inköpslista(list):
  """En klass som beskriver en inköpslista, ärver från klassen list"""
  
  def __str__(self):#en super metod som kallas str som de den returnar är de som printas nät class obiectet printas
    sträng = ""#dehär är en tom sträng
    for vara in self:#för varge element i self för class obiectet
      sträng += " * " + str(vara)  + "\n"#lägg till i sträng strengen en stierna, vilken vara som är i class obiectet samt en ny rad
    return sträng#returnar strengen
  __repr__ = __str__
    
if __name__ == "__main__":#om filen körs från en annan fill kommer inte desa funktioner att köras då __name__ inte är __main__
  lista = Inköpslista(["ägg", "mjölk", "vetemjöl"])#en lista med ingrididienser som blir ett class obiect
  print(lista)#printar listan som presis blev defenierad
  