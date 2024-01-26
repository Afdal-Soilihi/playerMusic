import os
import tkinter as tk
from tkinter import filedialog
import pygame

class LecteurAudio:
    def __init__(self, root):
        self.root = root
        self.root.title("Lecteur Audio")

        self.current_track = None
        self.playing = False
        self.looping = False

        # Interface
        self.label = tk.Label(root, text="Aucune piste sélectionnée")
        self.label.pack(pady=10)

        self.browse_button = tk.Button(root, text="Choisir une piste", command=self.choose_track)
        self.browse_button.pack(pady=10)

        self.play_button = tk.Button(root, text="Lancer la lecture", command=self.play_pause)
        self.play_button.pack(pady=10)

        self.stop_button = tk.Button(root, text="Arrêter la lecture", command=self.stop)
        self.stop_button.pack(pady=10)

        self.volume_scale = tk.Scale(root, from_=0, to=1, resolution=0.1, orient=tk.HORIZONTAL, label="Volume", command=self.set_volume)
        self.volume_scale.set(0.5)
        self.volume_scale.pack(pady=10)

        self.loop_button = tk.Button(root, text="Lecture en boucle", command=self.toggle_loop)
        self.loop_button.pack(pady=10)

    def choose_track(self):
        file_path = filedialog.askopenfilename(filetypes=[("Fichiers audio", "*.mp3;*.wav")])
        if file_path:
            self.current_track = file_path
            self.label.config(text=os.path.basename(file_path))
            pygame.mixer.init()
            pygame.mixer.music.load(file_path)

    def play_pause(self):
        if self.current_track:
            if self.playing:
                pygame.mixer.music.pause()
            else:
                pygame.mixer.music.unpause()
                if not pygame.mixer.music.get_busy():
                    pygame.mixer.music.play()
            self.playing = not self.playing

    def stop(self):
        if self.current_track:
            pygame.mixer.music.stop()
            self.playing = False

    def set_volume(self, volume):
        if self.current_track:
            pygame.mixer.music.set_volume(float(volume))

    def toggle_loop(self):
        if self.current_track:
            self.looping = not self.looping
            pygame.mixer.music.set_endevent(pygame.USEREVENT)
            if self.looping:
                pygame.mixer.music.play(-1)
            else:
                pygame.mixer.music.play()

if __name__ == "__main__":
    root = tk.Tk()
    lecteur_audio = LecteurAudio(root)
    root.mainloop()