class Spel:
    def __init__(self,titel,genre,platform,prijs):
        self.titel = titel
        self.genre = genre
        self.platform = platform
        self.prijs = prijs

class Spelbibliotheek:
    def __init__(self):
        self.spelen = []


    def voeg_spel_toe(self,spel):
        self.spelen.append(spel)

    def verwijder_spel(self,spel):
        if spel in self.spelen:
            self.spelen.remove(spel)

    def toon_spellen(self):
        print("\nDIY STEAM:")
        for spel in self.spelen:
            print(spel.titel)

    def toon_details(self, spel_titel):
        gevonden_spel = None
        for spel in self.spelen:
            if spel.titel == spel_titel:
                gevonden_spel = spel
                break

        if gevonden_spel:
            print("\nSpel Details:")
            print("Titel:", gevonden_spel.titel)
            print("Genre:", gevonden_spel.genre)
            print("Platform:", gevonden_spel.platform)
            print("Prijs:", gevonden_spel.prijs)
        else:
            print("\nSpel niet gevonden in de bibliotheek.")