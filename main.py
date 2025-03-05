from menu import *

def main():
    try:
        running = True
        menu = Menu()
        while running:
            menu.event()
            menu.display()
    except Exception as e:
        print(f"il y a une erreur {e}")
        

main()
