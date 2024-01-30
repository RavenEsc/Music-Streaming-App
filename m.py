import pygame
from tkinter import *

root = Tk()
root.title("Simple MP3 Player")
root.geometry("500x200")

pygame.mixer.init()

def play_music():
    pygame.mixer.music.load("OutofAsh.mp3")  # specify the location of your file
    pygame.mixer.music.play(loops=0)

def stop_music():
    pygame.mixer.music.stop()

def pause_music():
    pygame.mixer.music.pause()

def unpause_music():
    pygame.mixer.music.unpause()

play_button = Button(root, text="Play Song", command=play_music)
play_button.pack()

stop_button = Button(root, text="Stop Song", command=stop_music)
stop_button.pack()

pause_button = Button(root, text="Pause Song", command=pause_music)
pause_button.pack()

unpause_button = Button(root, text="Unpause Song", command=unpause_music)
unpause_button.pack()

root.mainloop()