from datetime import datetime
PRICE_PER_SONG = 3


class Song:
    """Modèle représentant un son."""
    
    def __init__(self, name, artist, genre, artwork):
        """Initialise les détails relatifs au son."""
        self.name = name
        self.artist = artist
        self.genre = genre
        self.artwork = artwork
        
        
class Library:
    """Modèle qui stocke les sons."""
    
    def __init__(self):
        """Initialise une liste de sons"""
        self.songs = []
 
class ServiceInfo:
     """Modèle qui gère la maintenance de la jukebox."""
     def __init__(self, status, engineer_name):
        self.service_date = datetime.now()
        self.status = status
        self.engineer_name = engineer_name    
        
