import pygame
import os
import json

class Pokemon:
    def __init__(self, name, lifePoint, level, XP, giveXP, limitXP, attack, defence, type1, type2, next_evolution):
        self.name = name
        self.lifePoint = lifePoint
        self.level = level
        self.experience = experience
        self.giveXp = giveXP
        self.limitXP = limitXP
        self.attack = attack
        self.defence = defence
        self.type1 = type1
        self.type2 = type2
        self.KO = False
        self.link_image = "images"
        self.statut = "normal"
        self.next_evolution = next_evolution
        self.pokemon_list = []

    def evolve(self, pokemon):
        if pokemon:
            self.name = pokemon.name
            self.lifePoint = pokemon.lifePoint
            self.level = pokemon.level
            self.experience = pokemon.experience
            self.giveXp =  pokemon.giveXp
            self.limitXP = pokemon.limitXP
            self.attack = pokemon.attack
            self.defence = pokemon.defence
            self.type1 = pokemon.type1
            self.type2 = pokemon.type2
            self.next_evolution = pokemon.next_evolution

    def attacks(self):
        return (self.attack, self.defence)

    def display_pokemon(self):
        try:
            image = os.path.join(self.link_image + f"{self.name}.png")
        except FileNotFoundError:
            image = os.path.join(self.link_image + "default.png")
        try:
            pokemon = pygame.image.load(image)
            print("Image loaded successfully!")
        except pygame.error as e:
            print(f"Error loading image: {e}")
        return image

    def is_ko(self):
        return self.lifePoint <= 0
    
#########################################################################################################################
    def record_pokemon(self):
        pokemon_dict_list = [pokemon.to_dict() for pokemon in self.pokemon_list]
        with open('pokemon.json', 'w') as fichier:
            json.dump(pokemon_dict_list, fichier,indent=4)

    def get_pokemon_list(self):
            try:
                with open('pokemon.json', 'r') as fichier:
                    pokemon_list = json.load(fichier)
            except FileNotFoundError:
                    pokemon_list = []
            return pokemon_list

    #  Build the list updated
    def add_to_list(self, new_pokemon):

            new_pokemon_dict = new_pokemon

            # Vérifie si le Pokémon existe déjà dans la liste
            if new_pokemon_dict not in self.pokemon_list:
                self.pokemon_list.append(new_pokemon_dict)
                self.record_pokemon()  # Enregistre la liste mise à jour
            else:
                print('this pokemon is already in your pokedex')

    #name, lifePoint, level, XP, evolution, giveXP, limitXP,  attack, defence, type1, type2,
        
    def add_pokemon(self):
            name = input("Nom du Pokémon : ")
            pv = int(input("Points de vie : "))
            type = input("Type : ")
            attack = int(input("Attaque : "))
            defense = int(input("Défense : "))
            giveXP = int(input("Rapporte combien de points d'XP ? :"))

            new_pokemon = {"name": name, "lifePoint": pv, "level" : 1, "XP" : 0,"evolution" : False, 
                        "giveXP" : giveXP, "limitXP" :60, "attack": attack, "defense": defense, "type1": type, 
                        "type2": None, "next_evolution" : self.next_evolution}
            self.add_to_list(new_pokemon)
            print(f"{name} a été ajouté !") 

########################################################################################################################


    def to_dict(self):
        return {
            'name': self.name,
            'lifePoint': self.lifePoint,
            'level': self.level,
            'experience': self.experience,
            'giveXp': self.giveXp,
            'limitXP': self.limitXP,
            'attack': self.attack,
            'defence': self.defence,
            'type1': self.type1,
            'type2': self.type2,
            'KO': self.KO,
            'link_image': self.link_image,
            'statut': self.statut,
            'next_evolution': self.next_evolution.to_dict() if isinstance(self.next_evolution, Pokemon) else None
        }

    def level_up(self, opponent):
        self.experience += opponent.giveXp
        if self.experience >= self.limitXP:
            print(f"le pokemon a level up :{self.name} ")
            self.level +=1
            self.limitXP *= 3
            self.experience = self.experience - self.limitXP
            self.giveXp +=20
            self.lifePoint  += 100
            self.attack     += 25
            self.defence    += 10
        elif self.experience < self.limitXP:
            self.experience += opponent.giveXp

        if self.level == 5:
            self.evolve(self.next_evolution)
    
    def __str__(self):
            dictio =  f"""
                name : {self.name}
                lifePoint : {self.lifePoint}
                level : {self.level}
                xp : {self.experience}
                giveXp : {self.giveXp}
                limitXp : {self.limitXP}
                attack : {self.attack}
                defence : {self.defence}
                type1 : {self.type1}
                type2 : {self.type2}
                next_evolution : {self.next_evolution}
                """
            return dictio

raichu = Pokemon("raichu", 250, 1, 0, 100, 120, 30,25, "electric", None, None)
pikachu = Pokemon("pikachu", 100, 1, 0, 10, 20,10, 8, "electric", None, raichu)
tortank = Pokemon("tortank", 250, 1, 0, 100, 120, 30,25, "eau", None, None)
carabaffe = Pokemon("carabaffe", 175, 1, 0, 60, 120, 30, 25, "eau", None, tortank)
carapuce = Pokemon("carapuce", 120, 1, 0,60, 120, 30, 25, "eau",None, carabaffe)
dracaufeu = Pokemon("dracaufeu", 250, 1, 0, 100, 120, 30,25, "feu", None, None)
reptincelle = Pokemon("reptincelle", 175, 1, 0, 60, 120, 30, 25, "feu", "terre",dracaufeu)
salameche = Pokemon("salameche", 100, 1, 0,60, 120, 30, 25, "feu", "terre",reptincelle)
florizarre = Pokemon("florizarre", 250, 1, 0,100, 120, 30,25, "plante", "terre", None)
herbizarre = Pokemon("herbizarre", 175, 1,0,  60, 120, 30, 25, "plante", "terre",florizarre)
bulbizarre = Pokemon("bulbizarre", 100, 1, 0, 60, 120, 20, 25, "plante", "terre",herbizarre)
lugia = Pokemon("lugia", 175, 1,0, 100, 120, 30, 20,"vol", None, None)
artikodin = Pokemon("artikodin", 175, 1, 0, 60, 120, 30, 25, "vol", "glace", None)
triopiqueur = Pokemon("triopiqueur",250,1, 0, 60,120,30,25, "terre", None, None)
taupiqueur = Pokemon("triopiqueur", 100, 1,0, 60, 120, 30, 25, "terre", None,triopiqueur )
grodoudou = Pokemon("grodoudou", 250, 1, 0, 60, 120, 30, 25, "normal", None,None)
rondoudou = Pokemon("rondoudou", 60, 1, 0, 60, 120, 50, 25, "normal", None,grodoudou)
grotadmorv = Pokemon("grotadmorv", 175, 1,0, 100, 120, 30, 20,"poison", None, None)
tadmorv = Pokemon("tadmorv", 120, 1,0, 100, 120, 30, 20,"poison", None, grotadmorv)
ronflex = Pokemon("ronflex",250,1, 0, 60,120,30,25, "terre", None, None)
hoho = Pokemon("hoho", 200, 1,0, 100, 120, 30, 20,"vol", "feu", None)

pikachu.add_to_list(pikachu)
pikachu.add_to_list(carapuce)
pikachu.add_to_list(salameche)
pikachu.add_to_list(bulbizarre)
pikachu.add_to_list(lugia)
pikachu.add_to_list(artikodin)
pikachu.add_to_list(taupiqueur)
pikachu.add_to_list(rondoudou)
pikachu.add_to_list(tadmorv)
pikachu.add_to_list(ronflex)
pikachu.add_to_list(hoho)


listing = pikachu.get_pokemon_list()

