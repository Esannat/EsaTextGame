import tkinter as _tk
from .gamemap import GameMap as _GameMap
from .vision import Vision as _Vision
from .character import Character as _Character


class EsaTextGame:
    def __init__(self, mapfile):
        root = _tk.Tk()
        root.geometry("+20+20")
        canvas = _tk.Canvas(root, width=840, height=540, background="black")
        canvas.pack()

        gamemap = _GameMap(mapfile)
        vision = _Vision("./source/texts/baixuege_fanti", canvas, gamemap, 0, 0, 14, 9)
        character = _Character(gamemap, vision)
        character.move(0, 0)

        root.bind("<Left>", lambda e: character.move_left())
        root.bind("<Right>", lambda e: character.move_right())
        root.bind("<Up>", lambda e: character.move_up())
        root.bind("<Down>", lambda e: character.move_down())

        root.mainloop()