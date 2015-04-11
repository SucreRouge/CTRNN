from ea.ea import EA
from tkinter import *
from config.configuration import  Configuration
from gui.visualization import ResultDialog
import numpy as np
from simulator.environment import Environment
import cProfile

class Listner:
    def update(self, c, p, cf, bf, std):
            pass

def show_result(best):
    root = Tk()
    f = Frame(master=root)
    config = Configuration.get()
    result_dialog = ResultDialog(f, best)
    root.mainloop()

def debug_ann(best):
    ann = best.phenotype_container.get_ANN()
    while(True):
        txt = input('Test ANN:')
        if txt == 'q':
            break
        try:
            numbers = np.array([int(x) for x in txt.split(sep=" ")])
            print(numbers)
            a = ann.feedforward(numbers)
            print(a)
            action = np.argmax(a)
            if(action == Environment.MOVE_LEFT):
                print("LEFT")
            elif(action==Environment.MOVE_FORWARD):
                print("FORWARD")
            elif(action==Environment.MOVE_RIGHT):
                print("RIGHT")
        except:
            print("Not valid!")

genome_length = 352
pop_size = 20
gen = 20
threshold = 20
ea_system = EA()
listner = Listner()
ea_system.add_listener(listner)
translator = "parameter"
fitness = "tracker"
genotype = "default"
adult = "mixing"
parent = "sigma"

ea_system.setup(translator,fitness,genotype,adult,parent,genome_length)

best = ea_system.run(pop_size, gen, threshold)
#debug_ann(best)
show_result(best)



#cProfile.run('ea_system.run(pop_size, gen, threshold)', sort='cumtime')