from dataclasses import dataclass

@dataclass(order=True)
class RGB:
    red: int = 0
    green: int = 0
    blue: int = 0

    def __str__(self):
        return f"RGB({self.red}, {self.green}, {self.blue})"


class Game:
    BALLS = RGB(12, 13, 14)

    def __init__(self, game_info):
        self.game_id = int(game_info.split(':')[0].split(' ')[1])
        self.draws: list[RGB] = []
        self.parse_draws(game_info)

    def parse_draws(self, game_info):
        for draw in game_info.split(':')[1].split(";"):
            draw = draw.strip()
            self.draws.append(self.parse_draw(draw))

    def validate(self):
        for draw in self.draws:
            if not (
                draw.red <= Game.BALLS.red
                and draw.green <= Game.BALLS.green
                and draw.blue <= Game.BALLS.blue
            ):
                return False
        return True

    def find_power(self):
        POWER = RGB()
        for draw in self.draws:
            POWER.red = max(POWER.red, draw.red)
            POWER.blue = max(POWER.blue, draw.blue)
            POWER.green = max(POWER.green, draw.green)
        return POWER.red * POWER.green * POWER.blue

    def parse_draw(self, draw_info):
        draws = [d.strip() for d in draw_info.split(",")]
        draw = RGB()
        for turn in draws:
            ball_count, color = turn.split(" ")
            if color == "green":
                draw.green = int(ball_count)
            elif color == "red":
                draw.red = int(ball_count)
            elif color == 'blue':
                draw.blue = int(ball_count)
        return draw

    def __repr__(self):
        repr = f"Game ID: {self.game_id}\n"
        for draw in self.draws:
            repr += f"\tRED: {draw.red}, BLUE: {draw.blue}, GREEN: {draw.green}\n"
        return repr

def solve(input):
    s = 0
    for games in input:
        g = Game(games)
        s += g.find_power()
    return s


if __name__ == "__main__":
    with open("in", "r") as file:
        games = [line.strip() for line in file.readlines()]

    print(solve(games))