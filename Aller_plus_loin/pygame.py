import pygame
import os
import random

# Initialisation de pygame
pygame.init()

# Répertoire contenant vos fichiers audio
audio_directory = "/chemin/vers/votre/repertoire/audio"

# Liste des fichiers audio dans le répertoire
audio_files = [f for f in os.listdir(audio_directory) if f.endswith(('.mp3', '.wav'))]

# Initialisation du lecteur audio
pygame.mixer.init()

# Charger le premier fichier audio
current_track = 0
pygame.mixer.music.load(os.path.join(audio_directory, audio_files[current_track]))

# Fonction pour jouer la piste suivante
def play_next():
    global current_track
    current_track = (current_track + 1) % len(audio_files)
    pygame.mixer.music.load(os.path.join(audio_directory, audio_files[current_track]))
    pygame.mixer.music.play()

# Fonction pour jouer une piste aléatoire
def play_random():
    global current_track
    current_track = random.randint(0, len(audio_files) - 1)
    pygame.mixer.music.load(os.path.join(audio_directory, audio_files[current_track]))
    pygame.mixer.music.play()

# Charger la première piste
pygame.mixer.music.play()

# Boucle principale
while True:
    user_input = input("Entrez 'n' pour piste suivante, 'r' pour lecture aléatoire, ou 'q' pour quitter: ")
    
    if user_input == 'n':
        play_next()
    elif user_input == 'r':
        play_random()
    elif user_input == 'q':
        pygame.mixer.music.stop()
        pygame.quit()
        break
