

class Touchscreen:
    """Vue qui gère l'interface de la jukebox."""
    
    def select_song(self):
        """Selectionne un son."""
        pass
    
    def prompt_for_next_song(self, songs):
        """Demande un nouveau son."""
        for song in songs:
            print(song)
        return "Dark Chest of Wonders"
    
    
class Speakers:
    """Vue qui gère le son."""
    
    def __init__(self):
        """Initialise le volume."""
        self.volume = 5
        
    def get_louder(self):
        """Augmente le volume."""
        self.volume += 1
        
    def get_quieter(self):
        """Baisse le volume."""
        self.volume -= 1
        
    def play_song(self):
        """Joue la musique."""
        pass
    
class CoinBox:
    """Vue qui gère la réception de l'argent."""
    
    def __init__(self, amount):
        """Initialise le montant."""
        
        self.amount = amount
        
    def request_money(self, amount):
        """Attend un montant de l'utilisateur."""
        
        self.amount += amount
        return True