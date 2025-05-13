from spel import Spel
from spel import Spelbibliotheek

# Maak enkele Spel objecten aan
spel1 = Spel("The Legend of Zelda", "Actie-Avontuur", "Nintendo Switch", 59.99)
spel2 = Spel("Minecraft", "Sandbox", "Meerdere platforms", 29.99)
spel3 = Spel("Fortnite", "Battle Royale", "Meerdere platforms", 0.00)

# Maak een SpelBibliotheek object aan
bibliotheek = Spelbibliotheek()

# Voeg spellen toe aan de bibliotheek
bibliotheek.voeg_spel_toe(spel1)
bibliotheek.voeg_spel_toe(spel2)
bibliotheek.voeg_spel_toe(spel3)
bibliotheek.verwijder_spel(spel1)

# Toon de spellen in de bibliotheek
bibliotheek.toon_spellen()
bibliotheek.toon_details("Minecraft")