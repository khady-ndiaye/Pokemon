import json
import os

class PlayerManager:
    def __init__(self, players_filepath):
        self.players_filepath = players_filepath
        self.players = self.load_players()

    def load_players(self):
        if os.path.exists(self.players_filepath):
            try:
                with open(self.players_filepath, 'r') as file:
                    return json.load(file)
            except json.JSONDecodeError:
                return []
        return []

    def save_players(self):
        with open(self.players_filepath, 'w') as file:
            json.dump(self.players, file, indent=4)

    def add_player(self, name, pokemon):
        player_data = {
            "name": name,
            "pokemon": [pokemon],
            "score": 0
        }
        self.players.append(player_data)
        self.save_players()

    def add_pokemon_to_player(self, name, new_pokemon):
        for player in self.players:
            if player['name'] == name:
                player['pokemon'].append(new_pokemon)
                self.save_players()
                return
        print(f"Le joueur {name} n'existe pas.")

    def update_score(self, name, score):
        for player in self.players:
            if player['name'] == name:
                player['score'] += score
                self.save_players()
                return
        print(f"Le joueur {name} n'existe pas.")

if __name__ == "__main__":
    manager = PlayerManager('C:/Users/kylli/Desktop/Spe_ia/pokemon/players.json')
    
    #-------------------------------------------------------------------------------------------------------------------------------------------  
    # Exemple d'ajout d'un nouveau joueur
    manager.add_player("ky", {
        "name": "pikachu",
        "lifePoint": 100,
        "level": 1,
        "experience": 0,
        "giveXp": 10,
        "limitXP": 20,
        "attack": 10,
        "defence": 8,
        "type1": "electric",
        "type2": None,
        "KO": False,
        "link_image": "images",
        "statut": "normal",
        "next_evolution": {
            "name": "raichu",
            "lifePoint": 250,
            "level": 1,
            "experience": 0,
            "giveXp": 100,
            "limitXP": 120,
            "attack": 30,
            "defence": 25,
            "type1": "electric",
            "type2": None,
            "KO": False,
            "link_image": "images",
            "statut": "normal",
            "next_evolution": None
        }
    })

    # Exemple d'ajout d'un Pokémon gagné
    manager.add_pokemon_to_player("ky", {
        "name": "bulbizarre",
        "lifePoint": 100,
        "level": 1,
        "experience": 0,
        "giveXp": 60,
        "limitXP": 120,
        "attack": 20,
        "defence": 25,
        "type1": "plante",
        "type2": "terre",
        "KO": False,
        "link_image": "images",
        "statut": "normal",
        "next_evolution": {
            "name": "herbizarre",
            "lifePoint": 200,
            "level": 1,
            "experience": 0,
            "giveXp": 100,
            "limitXP": 150,
            "attack": 40,
            "defence": 35,
            "type1": "plante",
            "type2": "terre",
            "KO": False,
            "link_image": "images",
            "statut": "normal",
            "next_evolution": None
        }
    })

    # Exemple de mise à jour du score
    manager.update_score("ky", 50)