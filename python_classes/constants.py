from python_classes.data_types import Channel
from os import name


class colors:
    if name == "nt":
        try:
            import colorama
            colorama.init()
            dark_red = colorama.Fore.RED
            red = colorama.Fore.LIGHTRED_EX
            dark_green = colorama.Fore.GREEN
            green = colorama.Fore.LIGHTGREEN_EX
            dark_yellow = colorama.Fore.YELLOW
            yellow = colorama.Fore.LIGHTYELLOW_EX
            dark_blue = colorama.Fore.BLUE
            blue = colorama.Fore.LIGHTBLUE_EX
            dark_purple = colorama.Fore.MAGENTA
            purple = colorama.Fore.LIGHTMAGENTA_EX
            dark_cyan = colorama.Fore.CYAN
            cyan = colorama.Fore.LIGHTCYAN_EX
            gray = colorama.Fore.LIGHTBLACK_EX
            default = colorama.Fore.RESET
        except:  # If colorama isn't installed we'll run the rest of the program without color.
            print("Colorama not installed. Running without colors.")
            dark_red = ""
            red = ""
            dark_green = ""
            green = ""
            dark_yellow = ""
            yellow = ""
            dark_blue = ""
            blue = ""
            dark_purple = ""
            purple = ""
            dark_cyan = ""
            cyan = ""
            gray = ""
            default = ""
    else:  # Because we're using ASCII art we need to have the colors almost perfectly synced to esure it looks the same on both devices.
        dark_red = '\033[38;2;195;0;0m'
        red = '\033[38;2;205;66;66m'
        dark_green = '\033[38;2;16;132;14m'
        green = '\033[38;2;19;191;12m'
        dark_purple = '\033[38;2;124;41;147m'
        purple = '\033[38;2;180;5;166m'
        dark_blue = '\033[38;2;7;48;217m'
        blue = '\033[38;2;59;123;247m'
        dark_yellow = '\033[38;2;187;151;34m'
        yellow = '\033[38;2;220;194;154m'
        dark_cyan = '\033[38;2;58;143;205m'
        cyan = '\033[38;2;60;245;240m'
        gray = '\033[38;2;96;96;96m'
        default = '\033[0m'
    print(default, end="")  # Make sure we're using the default color settings.

    def test_colors():
        print(colors.dark_red + "dark red" + colors.default)
        print(colors.red + "red" + colors.default)
        print(colors.dark_green + "dark green" + colors.default)
        print(colors.green + "green" + colors.default)
        print(colors.dark_yellow + "dark yellow" + colors.default)
        print(colors.yellow + "yellow" + colors.default)
        print(colors.dark_blue + "dark blue" + colors.default)
        print(colors.blue + "blue" + colors.default)
        print(colors.dark_purple + "dark purple" + colors.default)
        print(colors.purple + "purple" + colors.default)
        print(colors.dark_cyan + "dark cyan" + colors.default)
        print(colors.cyan + "cyan" + colors.default)
        print(colors.gray + "gray" + colors.default)
        print(colors.default + "default" + colors.default)


server_id = "614335416178442242"
progress_anouncements = Channel(
    "614336214786375682", "Progress Anouncements", "Anouncements")
boars_general = Channel("614345791133188096", "Boars General", "Argent Boars")
boars_commands = Channel("614350341344985098",
                         "Boars Commands", "Argent Boars")
wolves_general = Channel("614345822477352974",
                         "Wolves General", "Azure Wolves")
wolves_commands = Channel("614350640264511508",
                          "Wolves Commands", "Azure Wolves")
stallions_general = Channel(
    "614345873463443457", "Stallions General", "Crimson Stallions")
stallions_commands = Channel(
    "614503418299547661", "Stallions Commands", "Crimson Stallions")
all_player_channels = {1: [boars_general, boars_commands], 2: [
    wolves_general, wolves_commands], 3: [stallions_general, stallions_commands]}

team_lookup_table = {1: "Argent Boars",
                     2: "Azure Wolves", 3: "Crimson Stallions"}

discord_epoch = 1420070400000


ratelimit_delay = 1.5
ratelimit_increment = 0.2
ratelimit_decrement = 0.05
ratelimit_minimum = 1.3

ratelimit_burst_size = 5
ratelimit_burst_delay = 4.5
ratelimit_burst_increment = 0.2
ratelimit_burst_decrement = 0.1
ratelimit_burst_minimum = 2

max_retries = 5

cut_off_id = 616814037086502915
