import json
import pygame
import os
import random

# Pygame start
pygame.init()
pygame.font.init()
# Screen size
BASE_DIR = r"C:\Users\alexc\Desktop\laplateforme\projet\annee1\pokemon"

# ways to files
IMAGE_DIR = os.path.join(BASE_DIR, "images")
SOUND_DIR = os.path.join(BASE_DIR, "sounds")



# Screen size
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600

# background
background_image = pygame.image.load(os.path.join(IMAGE_DIR, 'tokyo.png')) 
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Colors used
BLACK = (0, 0, 0)
YELLOW = (255, 223, 0)
WHITE = (255, 255, 255)
DARK_BLUE = (0, 0, 128)
RED = (250, 0, 0)


font_path = os.path.join(BASE_DIR, "Audiowide-Regular.ttf")

class Pokedex:
    
    def __init__(self, name):
        
        self.name = name
        self.pokemon_list = []
        self.pokedex_list = []
        self.pokemon_met = []
        pygame.font.init()  # calls and manage fonts
        self.title_font = pygame.font.Font(font_path, 70)
        self.poke_font = pygame.font.Font(font_path, 36)
       
        # Calls screen
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Pokemon")
        
        self.back_button_rect = None  # Initialisation back button
# Display the score booard rectangle   


    def displayPokedex(self):
        # Création du rectangle semi-transparent
        scoreSurface = pygame.Surface((1000, 440), pygame.SRCALPHA)
        scoreRect = scoreSurface.get_rect(center=(SCREEN_WIDTH//2, 310))
        pygame.draw.rect(scoreSurface, (0, 0, 0, 180), (0, 0, 1000, 440), border_radius=15)
        
        # Chargement de la liste du Pokédex
        self.get_pokedex_list()
        
        # Définition de la police
        font = pygame.font.Font(None, 30)  # Police par défaut, taille 30
        text_color = YELLOW # Blanc

        # Position de départ pour afficher le texte
        start_x = 10  # Décalage du bord gauche
        start_y = 10
        line_spacing = 50 

        header_text = "Nom          Niv.       Type         Def/Att    PV     Nb"
        header_surface = self.poke_font.render(header_text, True, text_color)
        scoreSurface.blit(header_surface, (start_x, start_y))  

        start_y += line_spacing
        
        if self.name:  # Assure-toi que self.player_name contient bien le nom du joueur    
            for entry in self.pokedex_list:
                    if self.name in entry:
                        pokemon_list = entry[self.name]
                        
                        for index, pokemon in enumerate(pokemon_list):
                                pokedex_text = f'{pokemon['name']}       {pokemon['level']}   {pokemon['type1']}/{pokemon['type2']}   {pokemon['defence']}/{pokemon['attack']}      {pokemon['lifePoint']}       '
                                text_surface = self.poke_font.render(pokedex_text, True, text_color)
                                scoreSurface.blit(text_surface, (start_x, start_y + index * line_spacing))  # 30 pixels entre chaque ligne

            # Affichage du rectangle sur l'écran
            self.screen.blit(scoreSurface, scoreRect.topleft)

    
    def display_title(self):
        title_text = self.title_font.render("Pokedex", True, RED)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, 40))
        self.screen.blit(title_text, title_rect)

    # Create the "Back to Menu" button
    def displayBlackButton(self):   
        button_width = 220
        button_height = 40
        self.back_button_rect = pygame.Rect(10, self.screen.get_height() - button_height - 10, button_width, button_height)
        pygame.draw.rect(self.screen, YELLOW, self.back_button_rect, border_radius=15)

        # Button text
        back_button_text = self.poke_font.render("<<< Menu", True, DARK_BLUE)
        back_button_text_rect = back_button_text.get_rect(center=self.back_button_rect.center)
        self.screen.blit(back_button_text, back_button_text_rect)
        return self.back_button_rect
    
    def choose_pokemon_random(self):
        with open('pokemon.json', 'r') as file:#load all pokemons from pokemon.json
            self.pokemon_list = json.load(file)
       
        pokemon_sample = random.sample(self.pokemon_list, 4) # Randomly chooses 1 element from pokemon_list
        return pokemon_sample

# Build a deck randomly
    def deck_building(self):
        new_deck = self.choose_pokemon_random() # Calls the sample function
        return new_deck
    
     # Get pokedex from podex.json   
    def get_pokedex_list(self):
        try:
            with open('poke.json', 'r', encoding='utf-8') as fichier:
                contenu = fichier.read().strip()
                if not contenu:
                    raise ValueError("Le fichier est vide")
                self.pokedex_list = json.loads(contenu)
        except (FileNotFoundError, ValueError, json.JSONDecodeError):
            print("Le fichier poke.json est vide ou invalide. Réinitialisation...")
            self.pokedex_list = []
            with open('poke.json', 'w', encoding='utf-8') as fichier:
                json.dump(self.pokedex_list, fichier, indent=4)
        
        return self.pokedex_list

    

    


    def record_pokedex(self):
        self.get_pokedex_list()  
        
        if not self.name:  
            return  

        player_found = False

        for entry in self.pokedex_list:
            if self.name in entry:
                pokemon_dict = entry[self.name]

                
                if isinstance(pokemon_dict, list):  
                    pokemon_dict = {poke: 1 for poke in pokemon_dict}  

                
                if self.pokemon_met in pokemon_dict:
                    pokemon_dict[self.pokemon_met] += 1
                else:
                    pokemon_dict[self.pokemon_met] = 1
                
                entry[self.name] = pokemon_dict 
                player_found = True
                break  

        if not player_found:  
            self.pokedex_list.append({self.name: {self.pokemon_met: 1}})

        # Sauvegarde le fichier JSON
        with open('poke.json', 'w') as fichier:
            json.dump(self.pokedex_list, fichier, indent=4)

    """        
    def run(self):
            print("Méthode run() appelée")
            running = True
            
            self.back_button_rect = self.displayBlackButton()

            while running:

                self.screen.blit(background_image, (0, 0))  # Background
                
                # Display elements
                self.display_title()
                self.displayBlackButton()
                self.displayPokedex()
                
                pygame.display.flip()  # Update screen
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if self.back_button_rect.collidepoint(mouse_pos):# return to menu
                            from menu import Menu 
                            menu = Menu()
                            menu.run()  
                            running = False  # close window    
            self.displayPokedex()                 
            pygame.quit()  
        """

