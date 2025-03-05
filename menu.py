import pygame
import sys
import os
import json
import random
from player import *
from manage_pokedex import *

# Pygame start
pygame.init()
pygame.font.init()


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ways to files
IMAGE_DIR = os.path.join(BASE_DIR, "images")
SOUND_DIR = os.path.join(BASE_DIR, "sounds")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

# Screen size
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600

# Colors used
BLACK = (0, 0, 0)
YELLOW = (255, 223, 0)
WHITE = (255, 255, 255)
DARK_BLUE = (0, 0, 128)
RED = (250, 0, 0)
try:
    MUSIC_SCREEN = {
                "main_menu" : pygame.mixer.music.load(os.path.join(SOUND_DIR, "LugiaSong.wav")),
                "battle" : [
                    pygame.mixer.music.load(os.path.join(SOUND_DIR, "FrontierBrain.wav")),
                    
                    pygame.mixer.music.load(os.path.join(SOUND_DIR, "TheManwiththeMachineGun.wav"))
                            ],
                "score" : pygame.mixer.music.load(os.path.join(SOUND_DIR, "VictoryFanfare.wav"))
                }
except FileNotFoundError as e:
    print(f"we didn't find your music file {e}")

try:
    SCREEN_BACKGROUND = {
        "main_menu": pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_DIR, "background.png")), (SCREEN_WIDTH, SCREEN_HEIGHT)),
        "battle": [
            pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_DIR, "background.png")), (SCREEN_WIDTH, SCREEN_HEIGHT)),
            pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_DIR, "background2.jpg")), (SCREEN_WIDTH, SCREEN_HEIGHT)),
                    ],
        "score": pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_DIR, "tokyo.png")), (SCREEN_WIDTH, SCREEN_HEIGHT))
                }
except FileNotFoundError as e:
    print(f"nous n'avons pas trouver les images {e}")

BUTTON_WIDTH = 60
BUTTON_HEIGHT = 60
BUTTON_MARGIN = 10
keyboard_rows = 3
keyboard_cols = 9

letter = "abcdefghijklmnopqrstuvwxyz"


try:
    ubuntu_font = pygame.font.Font(os.path.join("Ubuntu-Regular.ttf"), 36)
except FileNotFoundError:
    print("La police n'a pas été trouvée. Utilisation de la police par défaut.")
    ubuntu_font = pygame.font.Font(None, 36)



class Menu:
    def __init__(self):

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.font = ubuntu_font
        self.caption = pygame.display.set_caption("Pokemon")
        self.rect1 = pygame.Rect(400,300, 400, 50)
        self.rect2 = pygame.Rect(400, 400, 400, 50)
        self.rect3 = pygame.Rect(400, 500, 400, 50)
        self.rect4 = pygame.Rect(100,100, 1000, 400)
        self.rect5 = pygame.Rect(500,0, 200, 50)
        self.rect6 = pygame.Rect(200, 25,800, 250)
        self.rect7 = pygame.Rect(500,500,100,100)
        self.color = (32, 78, 246)
        self.running = True
        self.state = "main menu"
        self.background = SCREEN_BACKGROUND
        self.clock = pygame.time.Clock()
        self.text = [
            "New game",
            "pokedex",
            "Exit",
            "main menu",
            "enter your name : ",
            "choose your pokemon : "
        ]
        self.buttons = self.create_keyboard()
        self.sound = MUSIC_SCREEN
        self.logo = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_DIR, "logo.png")), (800, 250))
        self.username = ""
        self.pokemon = 0
        self.player = Player(self.username)

    def create_keyboard(self):
        buttons = []
        #diisplay the keyboard on the cennter of the screen
        total_keyboard_width = (keyboard_cols * BUTTON_WIDTH) + ((keyboard_cols - 1) * BUTTON_MARGIN)
        start_x = (SCREEN_WIDTH - total_keyboard_width) // 2

        #create the keyboard with the letter
        for row in range(keyboard_rows):
            for col in range(keyboard_cols):
                x = start_x + col * (BUTTON_WIDTH + BUTTON_MARGIN)
                y = 400 + row * (BUTTON_HEIGHT + BUTTON_MARGIN)
                letter_index = row * keyboard_cols + col
                if letter_index < len(letter):
                    char = letter[letter_index]
                    button_rect = pygame.Rect(x, y, BUTTON_WIDTH, BUTTON_HEIGHT)
                    buttons.append((char, button_rect))
        return buttons
    
    def draw_keyboard(self):
        for char, button in self.buttons:
            pygame.draw.rect(self.screen, self.color, button)
            text = self.font.render(char, True, BLACK)
            self.screen.blit(text, text.get_rect(center=button.center))

    def screen_main_menu(self):
        pygame.draw.rect(self.screen, self.color, self.rect1, 5)
        pygame.draw.rect(self.screen, self.color, self.rect2, 5)
        pygame.draw.rect(self.screen, self.color, self.rect3, 5)
        pygame.draw.rect(self.screen, self.color, self.rect6,1)

        text1 = self.font.render(self.text[0], True, (0, 0, 0))
        text2 = self.font.render(self.text[1], True, (0, 0, 0))
        text3 = self.font.render(self.text[2], True, (0, 0, 0))

        self.screen.blit(text1, text1.get_rect(center=self.rect1.center))
        self.screen.blit(text2, text2.get_rect(center=self.rect2.center))
        self.screen.blit(text3, text3.get_rect(center=self.rect3.center))
        self.screen.blit(self.logo, self.rect6)

    def screen_enter_player(self):
        vertical_pos =self.rect4.top + 20

        pygame.draw.rect(self.screen, self.color, self.rect5)
        pygame.draw.rect(self.screen, self.color, self.rect2)
        pygame.draw.rect(self.screen, self.color, self.rect1)

        text1 = self.font.render(self.text[3], True, (0, 0, 0))
        text2 = self.font.render(self.text[4], True, (0, 0, 0))
        text3 = self.font.render(self.username,True,(0, 0, 0))

        self.screen.blit(text1, text1.get_rect(center=self.rect5.center))
        self.screen.blit(text2, text2.get_rect(midtop=(self.rect4.centerx, vertical_pos)))
        self.screen.blit(text3,text3.get_rect(center=self.rect1.center))
        
        self.draw_keyboard()
        self.player.player_exists()
    
    def screen_pokemon(self):
        pokelist = self.display_pokemon()
        pygame.draw.rect(self.screen, self.color, self.rect5)

        text1 = self.font.render(self.text[5], True, (0, 0, 0))
        for text, rect in pokelist:
                pygame.draw.rect(self.screen, YELLOW, rect, border_radius=5)
                text_surface = self.font.render(text, True, BLACK)
                self.screen.blit(text_surface, text_surface.get_rect(center =rect.center))
        self.screen.blit(text1, text1.get_rect(center=self.rect5.center))
        self.state = "battle"

    def display_pokemon(self):
        pokelist = []
        vertical_pos =self.rect4.top + 20
        with open('pokemon\pokemon.json', 'r') as file:
            pokelistJson = json.load(file)
            for i, poke in enumerate(pokelistJson):
                text = f'{i + 1}. {poke["name"]}'
                rect = pygame.Rect(self.rect4.left + 20, vertical_pos, self.rect4.width - 40, 30)
                pokelist.append((text, rect))
                vertical_pos += 40        
        return pokelist

    def screen_game_battle(self):
        print("hello")

    def screen_pokedex(self):
        pokedex = Pokedex(self.username)
        pokedex.display_title()
        pokedex.displayBlackButton()
        pokedex.displayPokedex()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for char, button in self.buttons:
                    if button.collidepoint(event.pos):
                        self.username += char
                        print(self.username)
                if self.state == "main menu":
                    if self.rect1.collidepoint(event.pos):
                        self.state = "player"
                    elif self.rect2.collidepoint(event.pos):
                        self.state = "pokedex"
                    elif self.rect3.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()
                if self.state == "pokemon":
                    list = self.display_pokemon()
                    for pokemon, button in list:
                        if button.collidepoint(event.pos):
                            self.pokemon = pokemon[0]
                            self.player.choose_pokemon(self.pokemon)
                            self.player.save_to_file(self.username)             
                if self.state == "player":
                    if self.rect5.collidepoint(event.pos):
                        self.state = "main menu"
                elif self.state == "score":
                    if self.rect5.collidepoint(event.pos):
                        self.state = "main menu"
            if event.type == pygame.KEYDOWN:
                if self.state == "player":
                    if event.key == pygame.K_SPACE:
                        self.player.player_exists()
                        self.state = "pokemon"
                    elif event.key == pygame.K_BACKSPACE:
                            self.username = self.username[:-1]
                            print(self.username)


    def screen_transition(self):
        if self.state == "main menu":
            self.background = SCREEN_BACKGROUND["main_menu"]
            self.screen.blit(self.background, (0,0))
            self.screen_main_menu()

        elif self.state == "player":
            self.background = SCREEN_BACKGROUND["main_menu"]
            self.screen.blit(self.background, (0,0))
            self.screen_enter_player()

        elif self.state == "pokemon":
            self.background = SCREEN_BACKGROUND["main_menu"]
            self.screen.blit(self.background, (0,0))
            self.screen_pokemon()

        elif self.state == "battle":
            
            self.background = random.choice(SCREEN_BACKGROUND["battle"])
            self.screen.blit(self.background, (0,0))
            self.screen_game_battle()

        elif self.state == "pokedex":
            self.background = SCREEN_BACKGROUND["score"]
            self.screen.blit(self.background, (0,0))
            
        pygame.display.flip()

    def display(self):
        self.screen_transition()
        
