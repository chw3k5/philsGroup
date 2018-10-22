__author__ = 'James'

import Tkinter as tk
#import tkMessageBox as tmb
import os


#########################
#File Writing
#########################

def end_template(n, inn, output):

    for i in n:
        template = """TOOL CALL {} Z S10000
M3
CYCL DEF 9.0 DWELL TIME
CYCL DEF 9.1 DWELL15
TCH PROBE 584 TOOL SETTING L,R ~
 Q350=+0    ;MEASURING TYPE ~
 Q351=+0    ;APPLICATION ~
 Q352=+0    ;CUTTING EDGE CONTROL ~
 Q355=-2    ;MEASURING POSITION ~
 Q361=+5    ;NUMBER OF MEASURINGS ~
 Q362=+0.003 ;SCATTER TOLERANCE ~
 Q359=+0    ;ADD. LENGTH CORRECT. ~
 Q360=+0    ;ADD. RADIUS CORRECT.\n""".format(i)
        inn.write(template)
        output.insert('end', template)

def drill_template(n, inn, output):
    for i in n:
        template = """TOOL CALL {} Z S10000
M3
CYCL DEF 9.0 DWELL TIME
CYCL DEF 9.1 DWELL10
TCH PROBE 583 TOOL SETTING LEN ~
  Q350=+0    ;MEASURING TYPE ~
  Q361=+5    ;NUMBER OF MEASURINGS ~
  Q362=+0.003 ;SCATTER TOLERANCE ~
  Q359=+0    ;ADD. LENGTH CORRECT.\n""".format(i)
        inn.write(template)
        output.insert('end', template)

def laser_cal_template(inn, output):
	template="""TOOL CALL 30 Z S10000
M3
CYCL DEF 9.0 DWELL TIME
CYCL DEF 9.1 DWELL10
TCH PROBE 581 CALIBRATION ~
  Q350=+0    ;MEASURING TYPE ~
  Q361=+5    ;NUMBER OF MEASURINGS ~
  Q362=+0.003 ;SCATTER TOLERANCE\n"""
	inn.write(template)
	output.insert('end', template)

def begin_gen(numbers, ent1, ent2, output):
    filename = ent2.get()
    path = ent1.get()
    infile = open("{0}\\{1}.h".format(path, filename), 'w+')
    output.insert('1.0', "Writing file:\n\n")

    infile.write("BEGIN PGM {0} MM\n".format(filename))
    output.insert('end', "BEGIN PGM {0} MM\n".format(filename))
    laser_cal_template(infile, output)

def last_gen(numbers, ent1, ent2, output):
    filename = ent2.get()
    path = ent1.get()
    infile = open("{0}\\{1}.h".format(path, filename), 'a')
    infile.write("TOOL CALL 0 Z\nEND PGM {0} MM\n".format(filename))
    output.insert('end', "TOOL CALL 0 Z\nEND PGM {0} MM\n".format(filename))
    output.insert('end', "\nFile Complete!\n")
    infile.close()

def mill_gen(numbers, ent1, ent2, output):
    filename = ent2.get()
    path = ent1.get()
    infile = open("{0}\\{1}.h".format(path, filename), 'a')
    output.insert('1.0', "Writing file:\n\n")

    #infile.write("BEGIN PGM {0} MM\n".format(filename))
    #output.insert('end', "BEGIN PGM {0} MM\n".format(filename))
    end_template(numbers, infile, output)
    #infile.write("TOOL CALL 0 Z\nEND PGM {0} MM\n".format(filename))
    #output.insert('end', "TOOL CALL 0 Z\nEND PGM {0} MM\n".format(filename))
    #output.insert('end', "\nFile Complete!\n")

def drill_gen(numbers, ent1, ent2, output):
    filename = ent2.get()
    path = ent1.get()
    infile = open("{0}\\{1}.h".format(path, filename), 'a')
    output.insert('1.0', "Writing file:\n\n")

    #infile.write("BEGIN PGM {0} MM\n".format(filename))
    #output.insert('end', "BEGIN PGM {0} MM\n".format(filename))
    drill_template(numbers, infile, output)
    #infile.write("TOOL CALL 0 Z\nEND PGM {0} MM\n".format(filename))
    #output.insert('end', "TOOL CALL 0 Z\nEND PGM {0} MM\n".format(filename))
    #output.insert('end', "\nFile Complete!\n")


##########################
#Tkinter Stuff
##########################

def appendtool(var, num):
    if num not in var:
        var.append(num)
    else:
        var.remove(num)
    #print var #Debug
    return var

def buttoncheck(message, selected):
    try:
        message.set(selected)
        print selected
        return message
    except AttributeError:
        pass

def checkboxes(self, tools):
    self.cb = []
    roff = 3 #row offset
    coff = 1 #column offset
    for i in range(1, 31):
        self.cb.append(tk.Checkbutton(self, text= "T"+str(i), command= lambda i=i: appendtool(tools, str(i))))
        if i <=3:
            self.cb[i-1].grid(column=i+coff, row=roff)
        else:
            if i%3 != 0:
                self.cb[i-1].grid(column=i%3+coff, row=i/3+roff)
            else:
               self.cb[i-1].grid(column=3+coff, row=i/3+roff-1)
    return tools

def outputframe(self):
    outputvar = tk.StringVar()
    outputvar.set("")

    self.f1 = tk.Frame(self)
    self.f1.grid(column=7, row=2, rowspan= 10)
    l1 = tk.Label(self.f1, text = "Output:")
    l1.grid(sticky='N')
    self.text1 = tk.Text(self.f1, width=40, height=10)
    self.text1.grid(column=1, row=1, rowspan= 10)
    self.b1 = tk.Button(self.f1, text="Clear", command= lambda : self.text1.delete('1.0', 'end'))
    self.b1.grid(column=0, row = 11)


def main_window():
    mw = tk.Tk()


    mw.title("Tool Adjuster")
    mw.geometry("750x350")

    path = tk.StringVar()
    path.set("{}".format(os.path.realpath(__file__))[:-10])
	#print len("{}".format(__file__))
    #path.set("{}".format(os.getcwd()))
    filename = tk.StringVar()
    filename.set("ED_Tool_Measure") #Default Filename
    tnum = []

    L1 = tk.Label(mw, text="Path: ")
    L2 = tk.Label(mw, text="Filename: ")
    E1 = tk.Entry(mw, width=40, textvariable = path)
    E2 = tk.Entry(mw, width=40, textvariable = filename)
    L1.grid(column = 1, row = 0, columnspan = 1)
    E1.grid(column = 2, row = 0, columnspan = 5)
    L2.grid(column = 1, row = 1, columnspan = 1)
    E2.grid(column = 2, row = 1, columnspan = 5)
    checkboxes(mw, tnum)
    outputframe(mw)
    begin_button = tk.Button(mw, text="Begin", command= lambda: begin_gen(tnum, E1, E2, mw.text1))
    button = tk.Button(mw, text="Endmill", command= lambda: mill_gen(tnum, E1, E2, mw.text1))
    button2 = tk.Button(mw, text="Drill", command= lambda: drill_gen(tnum, E1, E2, mw.text1))
    end_button = tk.Button(mw, text="End", command= lambda: last_gen(tnum, E1, E2, mw.text1))
    quitter = tk.Button(mw, text="Quit", command= lambda: mw.destroy())
    begin_button.grid(column=1, row=13, columnspan = 2)
    button.grid(column=2, row=13, columnspan = 2)
    button2.grid(column=3, row=13, columnspan = 2)
    end_button.grid(column=4, row=13, columnspan = 2)
    quitter.grid(column=5, row=13, sticky='E')


    mw.mainloop()



if __name__ == '__main__':

    main_window()

