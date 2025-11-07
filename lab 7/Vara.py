class Vara:
  """En klass som beskriver en vara"""
  
  def __init__(self, namn, mängd, enhet):
    """Kontruktorn, attributen namn, mängd och enhet
    parametrar: namn(str), mängd(int), enhet(str)
    returnerar: -"""
    self.namn = namn
    self.mängd=mängd
    self.enhet=enhet

    
  def __str__(self):
    """Returnerar en strängreprsenation av ett vara-objekt
    parametrar: -
    returnerar: sträng(str)"""
    return str(self.namn)+ " "+str(self.mängd)+ " "+str(self.enhet)
    
    
  def lägg_till_mängd(self, tillägg):
    """Lägger till inskickad mängd till varans attribut mängd.
    parametrar: tillägg (int)
    returnerar: -"""
    self.mängd+=tillägg
    
if __name__ == "__main__":
  vara = Vara("mjölk", 5, "dl")
  vara.lägg_till_mängd(3)
  print(vara)
