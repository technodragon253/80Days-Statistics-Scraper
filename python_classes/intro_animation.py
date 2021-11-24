from python_classes.constants import colors
import time
from os import name, system

boars = f"""
                              `+y:sNy..s+-./shdmMN
                             .yNdymMyhmMhhmNNNMMd+
                           .+dMMmmMMdNNMMmdNMMMm/`
                 `.--/:osshmMMMMMMMMNmMNdMMMMd/`  
             `-ohdmMMMMMMMMMMMMMMMNNMMmNMMMMmo    
/. `.o/-.-/oymMMMMMMNdmMMMMMMMMMMMMMMMNMMNh+`     
MmydmmymNMMMMMMMMMMdmyhNMMMMMMMMMMMMMMmMMNh       
sNMmNNmNNmNMMMMMMMMMNdmMMMMMMMMMMMMMMMMmMMm+`     
`smMNMMNmdmNmmMMMMMMMMMMMMMMMMMMMMMMMMMNNMMy-     
  ./:/yddh/+ooyddNMMMMMMMMMMMMMMMMMMMMMMNMMh/     
        .`      .:hMMMMMMMMMMMMMMMMMMMMMyMMh/     
      `:/os`  ``` -hMMMMMMMMMMMMMMMMMMMMNMMh/     
      /NdNNhhyddyhhdmMMMMMMMMMMMMMMMMMMmMMMh:     
     `+yMmMMNshydmddmMMMMMMMMMMMMMMMMMmMMMm+      
    .oddmMNMNMMddddNMMMMMMMMMMMMMMMMNNMMNy-       
      `.-://ssssssdNMMMMMMMMMMMMMMmNNMMm+         
                  `-+ydddmmNMNNmNNMMMmo.          
                      ``.:hNMMMMMmdy+.            
                          .odmNh/.`               

"""
wolves = f"""
                    `                             
               :o--o:`                            
              :yhyshs:                            
             -+hhhhhhs-  ````         `           
             :yhhhhhhho//oooo/:::///+/o:`         
             :yhhhhhhhhhhyhhhhhhhhhhhhhy-         
           `+syhhhhhhhhhhsoshhhhhhhhhhho.         
          -ohhhhhhhhhhhhhhhhhhhhhhhhhh+.``````.`  
         :shhhhhhhhhhhhhhhhhyyhhyyyyyhyo+++++ss+` 
       `:yhhhhhhhhhhhhhhhhhhyyhshysyysossssss+-`  
     `.+yhhhhhhhhhhhhhhhhhhhhhhhhhhhhhs:....`     
 `-:+syhhhhhhhhhhhhhhhhhhhsssso+::+++:.           
  -/++sohhhhhhhhhhhhhhhhsyoo-`                    
       :shhhhhhhhhhhhhhhhs/-`                     
       :shhhhhhhhhhhhhhhhhhyss++++.               
       :yhhhhhhhhhhhhhhhhhhhhhhyo/`       `-:     
      `ohhhhhhhhhhhhhhhhhhhhhhhhyo/.   .-:-`      
    `+syyssshhhhhhhhhhhhhhhhhhhhhhhy++/-`         
    `//:-`.+hhhhhhhhhhhhhhhhhhhhhhhyhh/           
          `+hhhhhhhhhhhhhhhhhhhhhhhyyoo.          
          -shhhhhhhhhhhhhhhhhhhhhhhhhs-           
         `+hhhhhhhhhhhhhhhhhhhhhhhhhhhs.          
         -sshhhhhhhhhhhhhhhhhhhhhhhhhhh/          
         `oyhhhhhhhhhhhhhhhhhhhhhhhho+/.          
          -::/++sssssssyhhhhssss+/-.`             
                     `........                    

"""
stallions = f"""
                        -+-                       
                 `-+/:::+/////::.`                
               `.:ooo++oo-+ooo+/+//:-`            
           `.:++oooooooo+:oooooooo+//--.``        
       `-:+ooo+ooooooooooo+/+oooooooooooo++/:`    
  ``.-/+ooooo//ooooooooooooo//ooooooo++//-..`     
.:++oooooooooooooooooooooooooo/ooooooooo/:```     
/oo+/oooooooooooooooooooooooooo/+oooooo+/+/++/::` 
:ooooooooooooooooooooooooooooooo:+ooooooooo+///:. 
.:://+oooooooooooooooooooooooooo+:ooooooo:.`      
 ./+ooooo/-:--+++++/+ooooooooooo+:oooooooo+++++/:.
  `-++::`     .//+ooooooooooooooo.ooooooo++++///:.
            ./oooooooooooooooooo+-ooooooo+/++/:-` 
          ./oooooooooooooooooooo+-ooooo+++//:://` 
        `:oooooooooooooooooooooo:+ooooo///.       
       `/oooooooooooooooooooooo+-oooooo+++/:.     
      .+ooooooooooooooooooooooo:/ooooo+//////.    
    `:+ooooooooooooooooooooooo+:ooo+ooooo+-`      
  `-+ooooooooooooooooooooooooo//oooo+/-`.``       
  -+oooooooooooooooooooooooooooooo+-.`            
   `-:/+++oooooooooooooooooooooooo:               
       ```..--::/++++oooooooooo+++/`              

"""
black_cats = """
                                                  
            ` .                                   
          -`` -.``-/.    `:` . .                  
        -.``.:.`             `````                
   .:``.``-. ...``    .--.   .-``.`.`` `          
  `-   `` `     .`:`  `.--.//+/`     ``.-.        
  /. ` .- ..--           -++++-`        .-        
  `.         `..          `` `          `.        
   `.          --             ` `.                
      .        -.           `.. ``.`     ..       
    ..`.-`    ..`          `:.      `---``        
   -.        .-            -.  ``.``      .   `   
  :.         .`           --`...``        .` `-   
 -.          ..           .-.`-`:` ...`.``..``` ` 
`.           `.           ``..`::::.`         `   
``            .-`                   `.-           
. -./:-.``      -.... `- `:.  `-  `-`.            
-`.:``.-::////::-..-:.-:-::/` .````               
  .`        ```...-----...``:.                    
 ..                          `.                   
 `                                  `.            
 ``                                 ``            
                                                  

"""

def animate_logo(logo: str, type: int):
    out = ""
    for i, c in enumerate(logo):
        if type == 0:
            if c == "M" or c == "N":
                out += (colors.default + c)
            else:
                out += (colors.gray + c)
        elif type == 1:
            if c == "h":
                out += (colors.cyan + c)
            else:
                out += (colors.dark_cyan + c)
        elif type == 2:
            if c == "o":
                out += (colors.red + c)
            else:
                out += (colors.dark_red + c)
        elif type == 3:
            if c == "+":
                out += (colors.green + c)
            else:
                out += (colors.default + c)

    for line in out.split("\n"):
        print(line + colors.default)
        time.sleep(0.01)
    time.sleep(1)
    system('cls' if name == 'nt' else 'clear') #Clear the terminal

    #Sadly the "scroll back" animation doesn't work in most terminals
    #for line in range(0,out.count("\n"),1):
    #    sys.stdout.write("\033[F")
    #    sys.stdout.write("\033[K")
    #    time.sleep(0.05)

system('cls' if name == 'nt' else 'clear') #Clear the terminal
animate_logo(boars, 0)
time.sleep(1)
animate_logo(wolves, 1)
time.sleep(1)
animate_logo(stallions, 2)
time.sleep(1)
animate_logo(black_cats, 3)