# 80Days-Statistics-Scraper

This is a project to get data from the 80Days game (You can join the discord where it's hosted here: https://discord.gg/v79Hk8CXem)

# Dependancies

To make it work you need to have python installed (duh) and do "pip install requests" in your terminal.

Optionally install Colorama using "pip install colorama" to get colored text. (Not required on linux)

# Add auth key

To add an authentication key you need to make a file called "auth.txt". 
Paste in your auth key and save the file.
To get your auth key follow this tutorial: https://www.youtube.com/watch?v=YEgFvgg7ZPI (I'll add my own someday...)

# Usage

Run "main.py" to download all games. By default it will only download any missing games in output.json. For now to redownload all games, not just the missing ones, you need to delete "output.json". 

Currently there is no way of automatically gathering statistics. This will be changed shortly.
