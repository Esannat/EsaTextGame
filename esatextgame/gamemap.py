import json as _json

class GameMap:
    "用来存放游戏中的地图"
    def __init__(self, mapfile):
        # 从json文件构建地图
        with open(mapfile, encoding="utf-8") as f:
            obj = _json.load(f)
        matrix = []
        for i in range(obj["height"]):
            lst = []
            matrix.append(lst)
            for j in range(obj["width"]):
                letter = obj["seq"][i*obj["width"]+j]
                if letter == "c":
                    self.birth_place = (j, i)
                lst.append(letter)
        self.matrix = matrix
        self.width = obj["width"]
        self.height = obj["height"]