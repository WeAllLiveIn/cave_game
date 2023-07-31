from random import *

class Room:
    def __init__(self, xy: tuple) -> None:
        self.xy = xy

    def get_random_atributes(self) -> None:
        pass

    def __repr__(self):
        return 'Комната'

    def __str__(self):
        return 'Комната'


class WorldMap:
    def __init__(self, player_id: int) -> None:
        self.player_id: int = player_id
        self.map: list = []
        self.rooms_list: list = []
        self.mapsize = 0

    def generate_square(self, lenght: int = 3) -> None:
        self.map: list = [[0 for i in range(lenght)] for i in range(lenght)]
        self.mapsize: int = lenght

    def generate_obstruction(self, obstructions: int = None) -> None:
        if obstructions == None:
            obstructions = int(mapsize * 0.1)
        for _ in range(obstructions):
            x, y = randrange(0, self.mapsize), randrange(0, self.mapsize)
            self.map[x][y] = 1

    def choose_first_room(self) -> None:
        x, y = randrange(0, self.mapsize), randrange(0, self.mapsize)
        self.map[x][y]: Room = Room((x, y))
        self.rooms_list += [self.map[x][y]]

    def get_random_xy(self) -> tuple:
        x, y = choice(self.rooms_list).xy
        xy = tuple(filter(lambda m: 0 <= m[0] < self.mapsize and 0 <= m[1] < self.mapsize and self.map[m[0]][m[1]] == 0,
                          [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]))
        return xy

    def generate_new_worldmap(self, mapsize: int = 3, rooms_limit: int = 3, blocks: int = None) -> None:
        added_rooms_counter: int = 0
        self.generate_square(mapsize)
        self.generate_obstruction(blocks)
        self.choose_first_room()
        was: List[tuple] = []
        i: int = 0
        while i != rooms_limit - 1:
            xy = self.get_random_xy()
            if xy and xy not in was:
                was.append(xy)
                x, y = choice(xy)
                self.map[x][y] = Room((x, y))
                self.rooms_list.append(self.map[x][y])
                i += 1


    def __repr__(self) -> str:
        s = ''
        for i in range(self.mapsize):
            for j in range(self.mapsize):
                if self.map[i][j] == 0: s += "■ "
                elif self.map[i][j] == 1: s += "x "
                else: s += "□ "
            s += "\n"
        return s