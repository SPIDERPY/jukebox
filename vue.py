import re


class Touchscreen:
    """vue qui gère l'interface de la jukebox."""
    
    def select_songs(self):
        """Selectionne un son."""
        for song in songs:
            # affiche les sons
            pass
        return "Dark Chest of Wonders"
    
class Speakers:
    """Vue qui gère le son."""
    
    def __init__(self):
        """Initialise le volume."""
        self.volume = 5
        
    def get_mouder(self):
        """Augmente le volume."""
        self.volume += 1
        
    def get_quieter(self):
        """Baiise le song."""
        self.volume -= 1
        
    def play_song(self, song):
        """Joue la musique."""
        pass
    
class CoinSlot:
    """Vue qui gère la reception de l'argent."""
    
    def __init__(self, amount):
        """initialise le montant"""
        self.amount = amount
        
        
    def request_money(self, amount):
        """Attend un montant de l'utilisateur."""
        # attend l'argent
        # donne le change
        self.amount += amount
        return True
    