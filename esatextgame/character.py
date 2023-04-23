from .gamemap import GameMap as _GameMap
from .vision import Vision as _Vision
from .colors import colors as _colors

class Character:
    "角色类"
    def __init__(self, gamemap: _GameMap, vision: _Vision):
        self.gamemap = gamemap
        self.vision = vision

        self.vision_x, self.vision_y = vision.birth_place
        self.map_x, self.map_y = gamemap.birth_place

    def move(self, dx, dy):
        new_map_x = self.map_x + dx
        new_map_y = self.map_y + dy
        
        # 离开地图范围则失败
        if new_map_x < 0 or new_map_x >= self.gamemap.width:
            return
        if new_map_y < 0 or new_map_y >= self.gamemap.height:
            return
        # 是墙则失败
        if self.gamemap.matrix[new_map_y][new_map_x] == "w":
            return
        # 是目的地则胜利
        if self.gamemap.matrix[new_map_y][new_map_x] == "d":
            self.achieve()
            return
        
        # 否则先在地图上把角色移动了
        self.gamemap.matrix[self.map_y][self.map_x] = "s"
        self.gamemap.matrix[new_map_y][new_map_x] = "c"
        self.map_x = new_map_x
        self.map_y = new_map_y
        
        # 接下来计算视野随角色移动
        vision_dx = 0
        vision_dy = 0
        new_vision_x = self.vision_x + dx
        new_vision_y = self.vision_y + dy
        if new_vision_x < 2:
            vision_dx -= 2 - new_vision_x
            if self.vision.x + vision_dx < 0:
                vision_dx += -self.vision.x - vision_dx
        elif new_vision_x > self.vision.width - 3:
            vision_dx += new_vision_x - self.vision.width + 3
            if self.vision.x + self.vision.width + vision_dx > self.gamemap.width:
                vision_dx -= self.vision.x + self.vision.width + vision_dx - self.gamemap.width
        if new_vision_y < 2:
            vision_dy -= 2 - new_vision_y
            if self.vision.y + vision_dy < 0:
                vision_dy += -self.vision.y - vision_dy
        elif new_vision_y > self.vision.height - 3:
            vision_dy += new_vision_y - self.vision.height + 3
            if self.vision.y + self.vision.height + vision_dy > self.gamemap.height:
                vision_dy -= self.vision.y + self.vision.height + vision_dy - self.gamemap.height
        # 如果需要移动视野则调用vision.move()，之后它会自动改变文字颜色
        if vision_dx != 0 or vision_dy != 0:
            self.vision.move(vision_dx, vision_dy)
            new_vision_x -= vision_dx
            new_vision_y -= vision_dy
        # 否则需要自己更改视野中文字的颜色，实现角色移动
        else:
            self.vision.change_one_color(self.vision_x, self.vision_y, _colors["s"])
            self.vision.change_one_color(new_vision_x, new_vision_y, _colors["c"])
        # 更改character里记录的其在视野中的坐标
        self.vision_x = new_vision_x
        self.vision_y = new_vision_y
        
    def move_left(self):
        self.move(-1, 0)

    def move_right(self):
        self.move(1, 0)
    
    def move_up(self):
        self.move(0, -1)

    def move_down(self):
        self.move(0, 1)

    def achieve(self):
        print("胜利了！")
        exit(0)