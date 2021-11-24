#import os
#os.chdir("python_classes")

import python_classes.intro_animation

from python_classes.constants import colors

i = input(f"""
Would you like to retrieve data? {colors.green}(Press '1' and 'Enter'){colors.default}
Or would you like to get statistics? {colors.green}(Press '2' and 'Enter'){colors.default}
Or exit {colors.green}(Press Enter){colors.default}
""")
if i == "1":
    import python_classes.get_data
elif i == "2":
    import python_classes.get_statistics


input("\nPress Enter to Exit...")