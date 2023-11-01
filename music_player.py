import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

pygame.mixer.init()

playlist = []

def browse_music():
    directory = askdirectory()
    os.chdir(directory)
    
    for file in os.listdir(directory):
        if file.endswith(".mp3"):
            playlist.append(file)
    
    play_music()

def play_music():
    try:
        song = playlist.pop(0)
        var.set("Now playing: " + song)
        pygame.mixer.music.load(song)
        pygame.mixer.music.play()
    except IndexError:
        var.set("No more songs in the playlist")

def stop_music():
    pygame.mixer.music.stop()
    var.set("Music stopped")

def pause_music():
    pygame.mixer.music.pause()
    var.set("Music paused")

def unpause_music():
    pygame.mixer.music.unpause()
    var.set("Music resumed")

def next_song():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()
    play_music()


root = tkr.Tk()
root.title("Music Player")

var = tkr.StringVar()
var.set("")

root.geometry("400x300")
root.configure(bg="lightgray")

frame = tkr.Frame(root, bg="lightgray")
frame.pack(pady=20)

label = tkr.Label(frame, textvariable=var, bg="lightgray")
label.pack(pady=10)

play_button = tkr.Button(frame, text="Play", command=play_music, bg="green", fg="white")
stop_button = tkr.Button(frame, text="Stop", command=stop_music, bg="red", fg="white")
pause_button = tkr.Button(frame, text="Pause", command=pause_music, bg="orange", fg="white")
unpause_button = tkr.Button(frame, text="Unpause", command=unpause_music, bg="blue", fg="white")
next_button = tkr.Button(frame, text="Next", command=next_song, bg="purple", fg="white")
browse_button = tkr.Button(frame, text="Browse", command=browse_music, bg="teal", fg="white")

play_button.pack(side="left", padx=10)
stop_button.pack(side="left", padx=10)
pause_button.pack(side="left", padx=10)
unpause_button.pack(side="left", padx=10)
next_button.pack(side="left", padx=10)
browse_button.pack(side="left", padx=10)

root.mainloop()
