from vue import Speakers, Touchscreen
from vue import CoinBox
from card import PRICE_PER_SONG, Library


class Controller:
    """Contrôleur principal."""
    
    def __init__(self):
        """Initialise les modèles et les vues."""
        
        self.bank = CoinBox()
        self.library = Library()
        self.service_history = []
        
        self.ui = Touchscreen()
        self.audio_output = Speakers()
        
    def play_next_song(self):
        """Joue le prochain son."""
        songs_to_suggest = []
        for song in self.library:
            # filter logic
            songs_to_suggest.append(song)
            
        chosen_song = self.ui.prompt_for_next_song(songs_to_suggest)
        CoinBox.request_money(PRICE_PER_SONG)
        self.audio_output.play_song(chosen_song)