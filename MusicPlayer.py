from tkinter import filedialog
from tkinter import *
import pygame, os

root = Tk()
root.title("My mp3")
root.geometry("500x300")



pygame.mixer.init()

menubar = Menu(root)
root.config(menu=menubar)

Songs = []
current_song = ' '
paused = False


def load_music():
    global current_song

    root.directory = filedialog.askdirectory()

    for song in os.listdir(root.directory):
        name, ext = os.path.splitext(song)
        if ext == ".mp3":
            Songs.append(song)

    for song in Songs:
        songlist.insert("end", song)

    songlist.selection_set(0)
    current_sonng = Songs[songlist.curselection()[0]]


def play_music():
    global current_song, paused

    if not paused:
        pygame.mixer.music.load(os.path.join(root.directory, current_song))
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()
        paused = False


def pause_music():
    global pause
    pygame.mixer.music.pause()
    pause = True


def next_music():
    global current_song, puased

    try:
        songlist.selection_clear(0, END)
        songlist.selection_set(Songs.index(current_song) + 1)
        current_song = Songs[songlist.curselection()[0]]
        play_music()
    except:
        pass


def prev_music():
    global current_song, puased

    try:
        songlist.selection_clear(0, END)
        songlist.selection_set(Songs.index(current_song) - 1)
        current_song = Songs[songlist.curselection()[0]]
        play_music()
    except:
        pass


orgm = Menu(menubar, tearoff=False)
orgm.add_command(label="Select songs", command=load_music)

menubar.add_cascade(label="Menu", menu=orgm)

songlist = Listbox(root, bg=("cyan"), fg="black", width="100", height="15")
songlist.pack()

im_play = PhotoImage(file="play.png")
im_pause = PhotoImage(file="pause.png")
im_next = PhotoImage(file="next.png")
im_prev = PhotoImage(file="previous.png")

marco_crrtl = Frame(root, bg="white")
marco_crrtl.pack()

playb = Button(marco_crrtl, image=im_play, borderwidth=0, command=play_music)
pauseb = Button(marco_crrtl, image=im_pause, borderwidth=0, command=pause_music)
nextb = Button(marco_crrtl, image=im_next, borderwidth=0, command=next_music)
prevb = Button(marco_crrtl, image=im_prev, borderwidth=0, command=prev_music)

prevb.grid(row=0, column=0, padx=7, pady=10)
playb.grid(row=0, column=1, padx=7, pady=10)
pauseb.grid(row=0, column=2, padx=7, pady=10)
nextb.grid(row=0, column=3, padx=7, pady=10)

root.mainloop()