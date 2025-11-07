from Vara import *
class Recept():
  """En klass som beskriver ett recept"""
  def __init__(self, maträtt, ingredienser):

      self.maträtt = maträtt
      self.ingredienser = ingredienser


  
    
  def __str__(self):
    """Returnerar en strängreprsenation av ett Recept-objekt
    parametrar: -
    returnerar: sträng(str)"""
    sträng = "Maträtt: " + self.maträtt + "\n"
    for vara in self.ingredienser:
      sträng += "  - " + vara.namn + ": " + str(vara.mängd) + " " + vara.enhet + "\n"
    return sträng
    
if __name__ == "__main__":
  recept = Recept("grillad lax", [Vara("laxfilé", 600, "g"), Vara("potatis", 800, "g"), Vara("dill", 1, "knippe"), Vara("citron", 1, "st"), Vara("smör", 50, "g")])
  print(recept)