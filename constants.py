from data_types import Channel

server_id = "614335416178442242"
progress_anouncements = Channel("614336214786375682", "Progress Anouncements", "Anouncements")
boars_general = Channel("614345791133188096", "Boars General", "Argent Boars")
boars_commands = Channel("614350341344985098", "Boars Commands", "Argent Boars")
wolves_general = Channel("614345822477352974", "Wolves General", "Azure Wolves")
wolves_commands = Channel("614350640264511508", "Wolves Commands", "Azure Wolves")
stallions_general = Channel("614345873463443457", "Stallions General", "Crimson Stallions")
stallions_commands = Channel("614503418299547661", "Stallions Commands", "Crimson Stallions")
all_player_channels = {1:[boars_general, boars_commands], 2:[wolves_general, wolves_commands], 3:[stallions_general, stallions_commands]}

discord_epoch = 1420070400000

initial_ratelimit_delay = 2
ratelimit_increment = 0.5
max_retries = 5

cut_off_id = 616814037086502915