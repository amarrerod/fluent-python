class Led:
    def __init__(self, brightness=0):
        self.bright = 0
        self.colors = [0, 0, 0]

    def set_brightness(self, bright):
        self.bright = bright

    def set_color(self, red=0, green=0, blue=0):
        self.colors = [red, green, blue]

    def __repr__(self) -> str:
        (r, g, b) = self.colors
        return f"({r},{g},{b}) with bright: {self.bright}"


class InvalidCommand(Exception):
    pass


class Robot:
    def __init__(self, n_leds=10):
        self.n_leds = n_leds
        self.leds = [Led(0) for _ in range(n_leds)]

    def __repr__(self) -> str:
        return (
            "Robot with leds\n"
            + "#" * 60
            + "\n"
            + "".join(f"Led #{i} -> {self.leds[i]}\n" for i in range(self.n_leds))
            + "#" * 60
            + "\n"
        )

    def beep(self, times, frequency):
        print(f"Beeping {times} times with a {frequency} frequency")

    def rotate_neck(self, angle):
        print(f"Rotate neck {angle} degrees")

    def handle_command(self, message):
        # Matches any subject that is a sequence with three items
        match message:
            case ["BEEPER", times, frequency]:
                self.beep(times, frequency)

            case ["NECK", angle]:
                self.rotate_neck(angle)

            case ["LED", ident, intensity]:
                self.leds[ident].set_brightness(intensity)

            case ["LED", ident, red, green, blue]:
                self.leds[ident].set_color(red, green, blue)

            case _:
                raise InvalidCommand(message)


def test_robot_matching():
    robot = Robot()

    cmd_1 = ["BEEPER", 100, 0.5]
    cmd_2 = ["NECK", 180]
    cmd_3 = ["LED", 0, 95]
    cmd_4 = ["LED", 0, 0.85, 0.50, 0.90]
    cmds = [cmd_1, cmd_2, cmd_3, cmd_4]
    for command in cmds:
        (cmd, *args) = command
        print(f"Running command: {cmd} with args: {args}")
        robot.handle_command(command)

    print(robot)
