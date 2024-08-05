import random
class Teams:
    def __init__(self):
        self.names = []

    def add_names(self, *names):
        self.names.extend(names)

    def get_random_name(self, prev_team=None):
        choices = [name for name in self.names if name != prev_team]
        return random.choice(choices) if choices else None
    
    def club_names(Self):
        teams1.add_names("Arsenal", "Aston Villa", "Brentford", "Brighton & Hove Albion", "Burnley", "Chelsea", "Crystal Palace", "Everton", "Leeds United", "Leicester City", "Liverpool", "Manchester City", "Manchester United", "Newcastle United", "Norwich City", "Southampton", "Tottenham Hotspur", "Watford", "West Ham United", "Wolverhampton Wanderers",
"Ajax", "Atalanta", "Athletic Bilbao", "Atletico Madrid", "Barcelona", "Benfica", "Borussia Dortmund", "Celtic", "Club Brugge", "Dynamo Kyiv", "Eintracht Frankfurt", "Fiorentina", "Galatasaray", "Genk", "Gladbach", "Hoffenheim", "Inter Milan", "Juventus", "Lazio", "Lille", "Lyon", "Marseille", "Milan", "Monaco", "Napoli", "PSG", "Porto", "Real Betis", 
"Real Madrid", "Real Sociedad", "Red Bull Leipzig", "Roma", "Sevilla", "Shakhtar Donetsk", "Slavia Prague", "Sporting CP", "SSC Napoli", "Stade Rennais", "Standard Liege", "Valencia", "Villarreal", "Werder Bremen", "Wolfsburg", "Zenit Saint Petersburg", "ACF Fiorentina", "AS Monaco", "AS Roma", "FC Porto", "SSC Napoli"
)
        return teams1.get_random_name()
    
    def club_names2(Self):
        teams2.add_names("Arsenal", "Aston Villa", "Brentford", "Brighton & Hove Albion", "Burnley", "Chelsea", "Crystal Palace", "Everton", "Leeds United", "Leicester City", "Liverpool", "Manchester City", "Manchester United", "Newcastle United", "Norwich City", "Southampton", "Tottenham Hotspur", "Watford", "West Ham United", "Wolverhampton Wanderers",
"Ajax", "Atalanta", "Athletic Bilbao", "Atletico Madrid", "Barcelona", "Benfica", "Borussia Dortmund", "Celtic", "Club Brugge", "Dynamo Kyiv", "Eintracht Frankfurt", "Fiorentina", "Galatasaray", "Genk", "Gladbach", "Hoffenheim", "Inter Milan", "Juventus", "Lazio", "Lille", "Lyon", "Marseille", "Milan", "Monaco", "Napoli", "PSG", "Porto", "Real Betis", 
"Real Madrid", "Real Sociedad", "Red Bull Leipzig", "Roma", "Sevilla", "Shakhtar Donetsk", "Slavia Prague", "Sporting CP", "SSC Napoli", "Stade Rennais", "Standard Liege", "Valencia", "Villarreal", "Werder Bremen", "Wolfsburg", "Zenit Saint Petersburg", "ACF Fiorentina", "AS Monaco", "AS Roma", "FC Porto", "SSC Napoli"
)
        return teams2.get_random_name()


teams1  = Teams()
teams2 = Teams()
team1 = teams1.get_random_name()
team2 = teams2.get_random_name(prev_team=team1)

# name_list.add_names("Arsenal", "Aston Villa", "Brentford", "Brighton & Hove Albion", "Burnley", "Chelsea", "Crystal Palace", "Everton", "Leeds United", "Leicester City", "Liverpool", "Manchester City", "Manchester United", "Newcastle United", "Norwich City", "Southampton", "Tottenham Hotspur", "Watford", "West Ham United", "Wolverhampton Wanderers",
# "Ajax", "Atalanta", "Athletic Bilbao", "Atletico Madrid", "Barcelona", "Benfica", "Borussia Dortmund", "Celtic", "Club Brugge", "Dynamo Kyiv", "Eintracht Frankfurt", "Fiorentina", "Galatasaray", "Genk", "Gladbach", "Hoffenheim", "Inter Milan", "Juventus", "Lazio", "Lille", "Lyon", "Marseille", "Milan", "Monaco", "Napoli", "PSG", "Porto", "Real Betis", 
# "Real Madrid", "Real Sociedad", "Red Bull Leipzig", "Roma", "Sevilla", "Shakhtar Donetsk", "Slavia Prague", "Sporting CP", "SSC Napoli", "Stade Rennais", "Standard Liege", "Valencia", "Villarreal", "Werder Bremen", "Wolfsburg", "Zenit Saint Petersburg", "ACF Fiorentina", "AS Monaco", "AS Roma", "FC Porto", "SSC Napoli"
# )
# name = teams.club_names()
# print(name)  # Output: ["Alice", "Bob", "Charlie"]