from tkinter import Canvas as _Canvas
from tkinter.font import Font as _Font
from .gamemap import GameMap as _GameMap
from .colors import colors as _colors

class Vision:
    "游戏中的视野"
    def __init__(self, textfile: str, canvas: _Canvas, gamemap: _GameMap, x, y, width, height):
        self.gamemap = gamemap
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.grids = []
        self.canvas = canvas
        self._font = _Font(family="方正舒体", size=-60)
        # 通过gamemap中的出生点位置计算vision中的出生点位置
        self.birth_place = (gamemap.birth_place[0] - x, gamemap.birth_place[1] - y)
        

        # 构造grids矩阵
        with open(textfile, encoding="utf-8") as f:
            text = f.read().replace("\n", "")
        len_text = len(text)
        for i in range(height):
            line = []
            self.grids.append(line)
            for j in range(width):
                pos = i * width + j
                letter = text[pos] if pos < len_text else "〇"
                line.append(canvas.create_text(j*60+30, i*60+30, anchor="center", text=letter, font=self._font))
        self.change_grids_colors()

    def change_grids_colors(self):
        "根据gamemap设置视野内grids的文字颜色"
        x, y, width, height = self.x, self.y, self.width, self.height
        map_width, map_height, map_matrix = self.gamemap.width, self.gamemap.height, self.gamemap.matrix
        for i in range(height):
            for j in range(width):
                if x < 0 or x + j >= map_width or y < 0 or y + i >= map_height:
                    color = _colors["default"]
                else:
                    color = _colors[map_matrix[y+i][x+j]]
                self.canvas.itemconfig(self.grids[i][j], {"fill": color})
    
    def change_one_color(self, x, y, color):
        "设置一个grid内文字颜色"
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return
        else:
            self.canvas.itemconfig(self.grids[y][x], {"fill": color})
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.change_grids_colors()