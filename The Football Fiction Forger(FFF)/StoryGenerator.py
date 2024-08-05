import requests
import random
import json
from Teams import Teams
from Characters import Players
from NarrativeSchemas import Schemas

class StoryGenerator:
    def __init__(self, filename, api_key=None):
        self.api_key = "dfe19029-67fc-46ec-aa00-184537c19f71" 
        self.used_words = []
        self.club_name = None
        self.club_name2 = None
        self.scorer_name = None
        self.defender_name = None
        self.goalkeeper_name = None
        self.filename = filename
        
    
    def _get_word_data(self, word):
        url = f"https://www.dictionaryapi.com/api/v3/references/thesaurus/json/{word}"
        if self.api_key:
            url += f"?key={self.api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if isinstance(data, list) and isinstance(data[0], dict) and 'meta' in data[0]:
                available_synonyms = [s for d in data for s in d.get('meta', {}).get('syns', [])]
                available_synonyms = [syn for syn_list in available_synonyms for syn in syn_list if syn != word ]
                if available_synonyms:
                    relevant_synonyms = sorted(available_synonyms, key=lambda syn: available_synonyms.count(syn), reverse=True)
                    top_five_synonyms = list(set(relevant_synonyms[:3]))
                    new_word = random.choice(top_five_synonyms)
                    self.used_words.append(new_word)
                    return new_word
        return word

    def replace_words(self, text):
        words_to_replace = ['progressed','ravenous','difference', 'change','boss','believe', 'makeshift','crazed','intense','tension','major','noticeable','determined','success','first', 'competitions','freedom', 'confidence','distinguished','confidence', 'slump','win','lately','opponents','coveted','proving', 'creativity', 'afraid', 'reputation', 'frustrated', 'struggling', 'reliable','amazing', 'diificult', 'enthusiasm', 'fearless', 'succeed', 'intense', 'fortunes','tense', 'team', 'certainty','intensity','reputation','change', 'stunning','connect', 'defeats', 'hero', 'united', 'electric','triumph', 'impressive','praised', 'loomed','perfect', 'influence','sensed','instantly','setback','interception', 'crucial', 'test', 'rivals', 'toughest', 'race', 'purpose', 'trust', 'events', 'debilitating','motivational', 'unrivaled','prove','hailed','hero','competitors','challenges','impressed','speeches', 'arranged', 'humble','diligent','transformed', 'declared', 'experienced', 'battling','good', 'outcomes', 'disappointing', 'ease', 'impressive', 'fierce', 'searching', 'evident','careers','motivated', 'gain', 'create', 'end', 'powerful', 'unwavering', 'example', 'prime', 'great', 'emerged', 'fanatics','border','victory', 'talent', 'performance', 'exceptional', 'determination', 'final','championship','persistence', 'accurate', 'maneuvering', 'performance','opportunities', 'contagious', 'commitment', 'pride', 'Skill', 'dedication', 'accomplished', 'admired', 'feared', 'natural', 'unmatched', 'strong', 'dedicated',  'tireless', 'former', 'proud', 'best', 'infectious', 'fought', 'erupted', 'mobbed', 'dominated', 'celebrated', 'atmosphere', 'swarmed','tension', 'skilful', 'incredible', 'confident', 'determined', 'coveted', 'entire', 'triumph', 'star player', 'bittersweet','mastery', 'passion', 'coordination', 'opponent', 'unstoppable', 'impeccable', 'significant', 'critical', 'competent', 'grueling', 'deserving', 'spectacular', 'achievement','relentless', 'unshakable', 'bittersweet', 'unbreakable', 'numerous', 'agility', 'winning', 'hope', 'perseverance', 'opponents', 'adversity', 'finals', 'difficult', 'battle', 'talented', 'inspiring', 'fantastic', 'tough', 'thrilling', 'supersonic', 'big']        
        words = text.split()
        new_words = []
        for i, word in enumerate(words):
            if word == "[Club_Name]":
                if not self.club_name:
                    self.club_name = teams.club_names()
                new_words.append(self.club_name)
            elif word == "[Player_Name]":
                if "[Player_Name]" in word:
                    if not self.scorer_name:
                        self.scorer_name = scorers.scorer_names()
                    new_words.append(word.replace("[Player_Name]", self.scorer_name))
            elif word == "[Player_Name2]":
                if "[Player_Name2]" in word:
                    if not self.defender_name:
                        self.defender_name = defenders.defenders_names()
                    new_words.append(word.replace("[Player_Name2]", self.defender_name))
            elif word == "[Goalkeeper]":
                if "[Goalkeeper]" in word:
                    if not self.goalkeeper_name:
                        self.goalkeeper_name = goalkeepers.goalkeepers_names()
                    new_words.append(word.replace("[Goalkeeper]", self.goalkeeper_name))
            elif word == "[Club_Name2]":
                if "[Club_Name2]" in word:
                    if not self.club_name2:
                        self.club_name2 = teams.club_names2()
                    new_words.append(word.replace("[Club_Name2]", self.club_name2))
            elif word in words_to_replace:
                new_word = self._get_word_data(word)
                new_words.append(new_word)
            else:
                new_words.append(word)
        return ' '.join(new_words)
    
    def load_used_names(self):
        try:
            with open(self.filename) as f:
                self.used_names = json.load(f)
        except FileNotFoundError:
            pass
        
    def save_used_names(self):
        with open(self.filename, 'w') as f:
            json.dump(self.used_names, f)

    def generate_story(self):
        text = schemas.get_random_name()
        new_text = replacer.replace_words(text)
        return new_text


replacer = StoryGenerator('used_names.json')   
teams = Teams()
defenders = Players()
scorers = Players()
goalkeepers = Players()
schemas = Schemas('used_names.json')
schemas.add_schemas(        
                            "[Club_Name] was having a difficult season . The players were struggling on both sides of the ball and it seemed like every game was a battle . But that all changed when [Player_Name] , the talented forward , stepped up and took control . With his inspiring leadership and exceptional skill , [Player_Name] led the team to victory after victory . But it wasn't just [Player_Name] who was making a difference . The defenders on the team were also stepping up and contributing in big ways . Whether it was [Player_Name2] making a crucial interception or [Goalkeeper] making a fantastic save , everyone was doing their part to help the team win . As the season progressed , [Club_Name] grew stronger and more confident . They faced tough opponents and overcame adversity , showing the world what they were made of. And in the end , it all paid off. [Club_Name] made it to the thrilling finals, and the entire city rallied behind them. They were more than just a team - they were a symbol of hope and perseverance , a shining example of what can be accomplished when you never give up. But the finals would not be easy. They faced their toughest opponents yet - the talented [Club_Name2] . It was a back-and-forth battle , with both teams putting everything on the line . But once again, [Player_Name] rose to the occasion . With his incredible footwork and lightning-fast agility , [Player_Name] scored the winning goal in the final minutes of the game.",
                            "As the season progressed , the unstoppable juggernaut continued to dominate their opponents , exhibiting their impeccable agility and unparalleled coordination . Fans worldwide were in awe of their mastery and passion , and many predicted that they would make it all the way to the prestigious championship . However , as the playoffs loomed , the team faced a significant setback . Their star player and captain , [Player_Name] , suffered a debilitating injury during a critical match . It seemed like all hope was lost , and many fans feared that the team's championship aspirations were over . But the squad refused to give up . They rallied around their injured captain , pledging to fight on and secure the championship in his honour . With the help of some competent substitutes and under the guidance of [Player_Name2] , they made it to the final . The championship game was a grueling battle , with both teams giving their all . Nevertheless , in the end , it was the deserving champions who emerged victorious , thanks to a spectacular goal by [Player_Name2] . The stadium erupted in cheers as the champions lifted the trophy high , a testament to their relentless hard work , commitment , and unshakable spirit . For [Player_Name] , it was a bittersweet moment . Though he could not be on the field with his teammates , he was proud to have played a role in their triumph . As he watched them celebrate , he knew that his injury had brought them even closer together , forging an unbreakable bond that would carry them through numerous triumphs in the future."
                            "The Champions League Final was the biggest game of the year, and [Club_Name] had fought hard to get there. They had faced some tough opponents along the way, but now they were just one game away from glory. The stadium was packed with fans, all of them cheering for their team. The atmosphere was electric , and you could feel the tension in the air . As the game got underway , it was clear that both teams were evenly matched . They battled back and forth , each one trying to gain an advantage . But then , in the second half , something amazing happened. [Player_Name] , the skilful striker for [Club_Name] , scored an incredible goal . The crowd erupted in cheers , and [Player_Name] was mobbed by his teammates . From that moment on , [Club_Name] dominated the game . They played with a confidence and determination that the other team just couldn't match . And when the final whistle blew , it was [Club_Name] who emerged victorious . They had won the coveted Cup, and the entire city celebrated their triumph .",
                            "The world of football is full of talented players , but [Player_Name] stood out from the group . He had a natural ability , with a skill for the game that was unequaled . Fans around the world appreciated his technique , and opponents dreaded his presence on the field . But [Player Name] was more than just a good player. He was a person who inspired his teammates to be their best . His commitment and hard work were contagious , and his teammates looked up to him for direction and inspiration . Together , they formed a strong and unified team . They faced many difficulties along the way , but they never gave up . They worked tirelessly to enhance their skills , and they always supported each other . And in the end , their hard work paid off . They won the championship , a moment that [Player_Name] would never forget . He was named the player of the tournament , an award that he shared with his teammates . It was a moment of victory , and they knew that they had accomplished something great together . Years later , [Player_Name] and his former teammates would look back on that championship victory with pride . They would recall the hard work and dedication that went into it , and they would be grateful for the bond that they had formed . They had accomplished something great together , and they would always be remembered as champions .",                         
                            "The season was in full swing , and [Club_Name] was determined to come out on top . They had an distinguished squad , with players who were skilled , fast , and determined to win . But they also faced tough opponents , teams that were just as ravenous for victory . The games were intense , with both sides fighting hard for every point . As the season progressed , it became clear that the race for the championship was going to be a close one . Every game was crucial , and every goal could make the difference between winning and losing . And then , in the final game of the season , it all came down to [Club_Name] and their unrivaled competitors . The tension was noticeable , and the fanatics were on the border of their seats . The game was a battle from start to finish . Both teams played with everything they had , and the score remained tied until the very end . But then , in the final moments of the game , [Player_Name] stepped up and scored the winning goal . The fanatics went crazed , and [Club_Name] had secured the championship . It was a moment that would be remembered for years to come , and [Player_Name] was hailed as a hero . [Club_Name] had proven that they were the best , and they had the trophy to prove it .",
                            "The football field was a battlefield , and [Player_Name] was the fierce fighter leading the attack . He was a powerful presence , with a strong shot and impressive speed . But [Player_Name] was also a team player . He worked hard to create opportunities for his teammates , always searching for ways to gain possession and score a goal . His leadership skills were unparalleled, and he motivated his teammates to give their best on the field . Throughout the game , [Player_Name] displayed his impressive abilities , maneuvering past defenders with ease and making accurate passes to create scoring opportunities . His dedication and persistence were evident as he fought for every ball and never gave up on a play . As the game neared its end , [Player_Name] remained a driving force for his team , leading the attack with his unwavering determination. He delivered an exceptional performance , showcasing his talent and leading his team to a hard-earned victory . In the end , [Player_Name] emerged as a true hero on the field , a fearless fighter , and an exceptional teammate . His performance will be remembered for years to come as a prime example of what it means to be a great football player ." ,                          
                            "[Club_Name] was a team with a long history of success , but they had been in a slump lately . They had lost their last three games , and morale was low . But then , [Player_Name] , the reliable striker , stepped up and changed everything . He scored a hat trick in their next game , leading the team to a stunning victory . His goals were incredible , with each one more impressive than the last . The fans went wild , and his teammates couldn't believe what they had just witnessed . But it wasn't just his goals that impressed them . It was his attitude . [Player_Name] was humble and hardworking , always pushing himself to be better . He stayed after practice to work on his finishing , and he never gave up in a game . His dedication inspired his teammates , and they started to play with more confidence and determination . They won game after game , and before long , they were in the running for the championship . In the final game of the season , they faced their toughest opponents yet - the league leaders . It was a tense and intense game , with both teams putting everything on the line . But [Player_Name] was the difference-maker once again . He scored a stunning goal in the first half , and then assisted on another in the second half . The fans were on their feet , and his teammates swarmed him in celebration . They went on to win the game , and the championship , and [Player_Name] was named the player of the tournament . He had taken [Club_Name] from the bottom of the table to the top , with his incredible skill , work ethic , and determination . It was a truly remarkable achievement .",
                            "[Club_Name] was a team in change . They had a new boss and many makeshift players , and it was taking time for them to connect . They had some good outcomes , but they also had some disappointing defeats . But then , [Player_Name2], the experienced defender , took action and transformed everything . He arranged team bonding events , remained after training to work on set pieces , and gave motivational speeches before each game . His leadership was just what the team needed , and they started to play with more trust and purpose . They won game after game , and before long , they were in the race for the championship . In the final game of the season , they faced their toughest opponent yet - [Club_Name2] . It was an intense game , with both teams trying their best . But then , [Player_Name2] made a crucial interception and played a perfect pass to [Player_Name] , who scored the winning goal. The fanatics went crazed , and [Player_Name2] was hailed as a hero . He had united the team , motivated his teammates , and led them to triumph .",
                            "[Club_Name] was a group with a lot of talent , but they just couldn't seem to succeed in the major games . They had lost in the semi-finals of the last two competitions , and confidence was low . But then , [Player_Name] the talented foward, rose to the occasion and transformed everything . He was fearless on the field , taking on defenders and scoring impressive goals . His energy and enthusiasm were contagious , and the group began to play with more certainty and intensity . They won game after game , and soon they were once again in the finals . This time , they faced their most difficult adversaries yet - the reigning champions . It was a back-and-forth game , with both teams creating opportunities. But then , [Player_Name] scored an amazing goal from outside the box , and the fanatics went crazed . The team held on for the triumph , and [Player_Name] was declared the player of the tournament. He had encouraged his teammates , led by example , and won the most significant game of their careers .",
                            "[Club_Name] was a team that had always been known for its defensive ability . They had some of the best defenders in the league , and they were hard to defeat . But this season , their attack was struggling . They just couldn't seem to score , and they were drawing too many games . The fans were getting frustrated , and the boss knew that he had to make a change . He decided to bring in [Player_Name] , the new signing to change their fortunes . [Player_Name] was a player with a reputation for scoring , and the coach hoped that he could be the missing piece of the puzzle . And he was right . [Player_Name] influence was instantly sensed , scoring in his first game and then in his second . His goals gave the team confidence , and they started to play with more freedom and creativity . They were no longer afraid to take challenges and push forward . And the results showed . They won game after game , and before long , they were battling for the championship . In the final game of the season , they faced their toughest opponents yet - the team that had been the league leaders for most of the year . But [Player_Name] was ready . He scored the opening goal in the first half , and then assisted on two more in the second half . The fans were going crazed , and the other players on the team couldn't believe what they were seeing . They had finally found their missing piece , and it was [Player_Name] . They won the game 3-1 , and the celebrations lasted long into the night . [Player_Name] had brought the team together and had led them to glory , proving once again that sometimes all it takes is one player to make a difference ."
                            )

text = schemas.get_random_name()
new_text = replacer.replace_words(text)
schemas.add_schemas(new_text)
print(new_text)
# print(schemas.used_schemas)