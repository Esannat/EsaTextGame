from esatextgame import EsaTextGame
from sys import argv
from os import path

# 根据命令行参数来决定使用哪张地图，默认是0号图
for arg in argv:
    if isinstance(arg, str) and arg.isnumeric():
        mapfile = f"./source/maps/labyrinth{arg}.json"
        if path.isfile(mapfile):
            break
else:
    mapfile = "./source/maps/labyrinth0.json"

game = EsaTextGame(mapfile)