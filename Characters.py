import random
class Players:
    def __init__(self):
        self.names = []

    def add_names(self, *names):
        self.names.extend(names)

    def get_random_name(self):
        return random.choice(self.names)
    
    def scorer_names(self):
        scorers.add_names("Raheem Sterling", "Heung-min Son", "Jamie Vardy", "Marcus Rashford", "Riyad Mahrez", 
                           "Pierre-Emerick Aubameyang", "Jack Grealish", "Wilfried Zaha", "Lionel Messi" , "Cristiano Ronaldo", 
                           "Neymar Jr", "Kylian Mbappe", "Robert Lewandowski", "Luis Suarez", "Karim Benzema", "Erling Haaland", 
                           "Sergio Aguero", "Memphis Depay", "Ansu Fati"

)
        return scorers.get_random_name()
        
    def defenders_names(self):
        defenders.add_names("Joao Cancelo", "Trent Alexander Arnold",  
                           "Sergio Ramos", "Virgil van Dijk", "Giorgio Chiellini", "Kalidou Koulibaly", "Dayot Upamecano", 
                           "Raphael Varane", "Marquinhos", "Mats Hummels", "Leonardo Bonucci", "David Alaba", "Andrew Robertson", 
                           "Lucas Hernandez", "Lucas Digne", "Jordi Alba", "Jose Gaya", "Achraf Hakimi"
)
        return defenders.get_random_name()
        
    def goalkeepers_names(self):
        goalkeepers.add_names( "Jan Oblak","Alisson Becker","Manuel Neuer","Marc-André ter Stegen","Ederson","Thibaut Courtois",
                            "Keylor Navas","Gianluigi Donnarumma","Hugo Lloris","David de Gea","Wojciech Szczesny",
                            "Samir Handanovic","André Onana","Rui Patricio","Lukasz Fabianski","Peter Gulacsi","Alex Meret",
                        "Emiliano Martinez","Yann Sommer","Kasper Schmeichel","Neto","Mike Maignan","Jasper Cillessen",
)
        return goalkeepers.get_random_name()


scorers = Players()
defenders= Players()
goalkeepers = Players()
# print(name)  
