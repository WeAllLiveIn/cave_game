from world_gen_test import WorldMap, Room


class Player:
    def __init__(self, player_id: int) -> None:
        self.player_id: int = player_id
        self.in_game: bool = False
        self.map: WorldMap = WorldMap()
        self.xy: tuple = ()

    def start_game(self) -> None:
        self.in_game = True
        self.map.generate_new_worldmap()
        self.xy = self.map.start_room_xy

    def move(self) -> None:
        if self.in_game is False:
            return None
        x, y = self.xy
        acceptable_ways = tuple(filter(lambda m: 0 <= m[0] < len(self.map) and 0 <= m[1] \
                                                 < len(self.map) and type(self.map[(m[1], m[0])]) == Room,
                                       [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]))
        if not acceptable_ways:
            print('No')
            return None
        print(*acceptable_ways)
        x, y = acceptable_ways[int(input())]
        # This print() and input() is a test for moving with a console
        # will change into arg
        self.xy = (x, y)
