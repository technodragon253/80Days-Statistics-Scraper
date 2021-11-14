import os
os.chdir("python_classes")

import intro_animation

from constants import colors

i = input(f"""
Would you like to retrieve data? {colors.green}(Press 1 and Enter){colors.default}
Or would you like to get statistics? {colors.green}(Press 2 and Enter){colors.default}
Or exit {colors.green}(Press Enter){colors.default}
""")
if i == "1":
    import get_data
elif i == "2":
    import get_statistics
else:
    quit()


input("\nPress Enter to Exit...")