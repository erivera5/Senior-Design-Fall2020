#python/project7 artemia feed
#artemia return 0 problems alarm

import tkinter as tkr
from tkinter import * 
from tkinter.ttk import * 

import tkinter.messagebox

import time
import sys
import os

#========================================================================
#Plots

import matplotlib.pyplot as plt
import numpy as np
import math

#=========================================================================


print ("========================")
hostName    = "192.168.7.2"
userName    = "debian"
pasword     = "temppwd"
#client.connect(hostname=hostname, username=username, password=password)
#First Login
#ssh-keygen -R 192.168.1.31
#Login password
#ssh debian@ 192.168.1.31
cmd = 'ssh-keygen -R 192.168.7.2'
#cmd = 'TestyBoi.txt'
cmd2 = 'ssh debian@192.168.7.2'
#cmd3 = 'yes'
#cmd4 = 'temppwd'
#cmd5 = 'LiveFeeder'#'BASH LiveFeeder'
root = Tk() 
root.geometry('1920x1080') 
root.title("Feeding Fish")
#============================



#============================
print ("========================")
hostName    = "192.168.7.2"
userName    = "debian"
pasword     = "temppwd"

#=============================================================================
#varGetter
def varGetter(var):
 #turn the stringVars into a string
    stvar = var#.get()

    #turn the string into an int
    int_var = int(stvar)
    return int_var

def strGetter(var):
    stvar = var.get()
    stringy = str(stvar)
    return stringy
    
def varLabel(v):
    
    int_var = v
    tank1var = v
    
    int_var = s1.get()
    int_var2 = s2.get()
    int_var3 = s3.get()
    int_var4 = s4.get()
    int_var5 = s5.get()    

    #int_var = varGetter(tank1var)
    #int_var2 = varGetter(tank2var)
    #int_var3 = varGetter(tank3var)
    #int_var4 = varGetter(tank4var)
    #int_var5 = varGetter(tank5var)
    
    
    #tkr.Label(root, text = int_var).grid(row =2, column = 1)
    #tkr.Label(root, text = int_var2).grid(row =3, column = 1)
    #kr.Label(root, text = int_var3).grid(row =4, column = 1)
    #tkr.Label(root, text = int_var4).grid(row =5, column = 1)
    #tkr.Label(root, text = int_var5).grid(row =6, column = 1)
    


  
style = Style() 
N0 = 0
N1 = 1
N2 = 2
N3 = 3
N4 = 4

#Log
var = tkr.IntVar()
#tkr.Label(root, text ="LOG").grid(row =0, column = 1)


# Start delay
sdelvar = tkr.IntVar()
tkr.Label(root, text ="Time to begin feeding(min)").place(x=30,y= 500)#.grid(column = 1 ,row =7,pady = 5,padx = 5)
mnu1 = OptionMenu(root,sdelvar,N0,N0,N1,N2,N3,N4)
mnu1.place(x=200, y=500)#.grid(row = 8, column = 1, pady = 5, padx = 25) 

# Tank 1
#tank1var = tkr.In1Var()
#tkr.Label(root, text ="Target Concentration for treatment 1(Artemia/ml)").grid(row =2)
#mnu2 = OptionMenu(root,tank1var,N0,N0,N1,N2,N3,N4)
#mnu2.grid(row = 3, column = 0, pady = 10, padx = 100) 
#Target Concentration for treatment
s1 = tkr.Scale(root, label='Feeding Rate/Tank 1(Art/ml)', from_=0, to=20, orient=tkr.HORIZONTAL, length=500,tickinterval=1,highlightbackground = 'gray' , resolution=1,command = varLabel)
s1.grid(row = 1, column = 0, pady = 10, padx = 25) 

# tank 2
#tank2var = tkr.IntVar()
#tkr.Label(root, text ="Target Concentration for treatment 2 (Artemia/ml)").grid(row =4)
#mnu3 = OptionMenu(root,tank2var,N0,N0,N1,N2,N3,N4)
#mnu3.grid(row = 5, column = 0, pady = 10, padx = 100) 

s2 = tkr.Scale(root, label='Feeding Rate/Tank 2(Art/ml)', from_=0, to=20, orient=tkr.HORIZONTAL, length=500,tickinterval=1,highlightbackground = 'gray', resolution=1,command = varLabel)
s2.grid(row = 2, column = 0, pady = 10, padx = 25) 

# Tank 3
#tank3var = tkr.IntVar()
#tkr.Label(root, text ="Target Concentration for treatment 3 (Artemia/ml)").grid(row =6)
#mnu4 = OptionMenu(root,tank3var,N0,N0,N1,N2,N3,N4)
#mnu4.grid(row = 7, column = 0, pady = 10, padx = 100) 

s3 = tkr.Scale(root, label='Feeding Rate/Tank 3(Art/ml)', from_=0, to=20, orient=tkr.HORIZONTAL, length=500,tickinterval=1 ,highlightbackground = 'gray', resolution=1,command = varLabel)
s3.grid(row = 3, column = 0, pady = 10, padx = 25) 

# Tank 4
#tank4var = tkr.IntVar()
#tkr.Label(root, text ="Target Concentration for treatment 4 (Artemia/ml)").grid(row =8)
#mnu5 = OptionMenu(root,tank4var,N0,N0,N1,N2,N3,N4)
#mnu5.grid(row = 9, column = 0, pady = 10, padx = 100) 

s4 = tkr.Scale(root, label='Feeding Rate/Tank 4(Art/ml)', from_=0, to=20, orient=tkr.HORIZONTAL, length=500,tickinterval=1,highlightbackground = 'gray', resolution=1,command = varLabel)
s4.grid(row = 4, column = 0, pady = 10, padx = 25) 

# tank 5
#tank5var = tkr.IntVar()
#tkr.Label(root, text ="Target Concentration for treatment 5 (Artemia/ml)").grid(row =10)
#mnu6 = OptionMenu(root,tank5var,N0,N0,N1,N2,N3,N4)
#mnu6.grid(row = 11, column = 0, pady = 10, padx = 100) 

s5 = tkr.Scale(root, label='Feeding Rate/Tank 5(Art/ml)', from_=0, to=20, orient=tkr.HORIZONTAL, length=500,tickinterval=1,highlightbackground = 'gray', resolution=1,command = varLabel)
s5.grid(row = 5, column = 0, pady = 10, padx = 25) 

s6 = tkr.Scale(root, label='Volume of Liquid in Cone #1', from_=0, to=20, orient=tkr.HORIZONTAL, length=500,tickinterval=1,highlightbackground = 'gray', resolution=1,command = varLabel)
s6.grid(row = 1, column = 1, pady = 10, padx = 25)

s7 = tkr.Scale(root, label='Volume of Liquid in Cone #2', from_=0, to=20, orient=tkr.HORIZONTAL, length=500,tickinterval=1,highlightbackground = 'gray', resolution=1,command = varLabel)
s7.grid(row = 2, column = 1, pady = 10, padx = 25)

s8 = tkr.Scale(root, label='Volume of Liquid in Cone #3', from_=0, to=20, orient=tkr.HORIZONTAL, length=500,tickinterval=1,highlightbackground = 'gray', resolution=1,command = varLabel)
s8.grid(row = 3, column = 1, pady = 10, padx = 25)

s9 = tkr.Scale(root, label='Volume of Liquid in Cone #4', from_=0, to=20, orient=tkr.HORIZONTAL, length=500,tickinterval=1,highlightbackground = 'gray', resolution=1,command = varLabel)
s9.grid(row = 4, column = 1, pady = 10, padx = 25)

s10 = tkr.Scale(root, label='Volume of Liquid in Cone #5', from_=0, to=20, orient=tkr.HORIZONTAL, length=500,tickinterval=1,highlightbackground = 'gray', resolution=1,command = varLabel)
s10.grid(row = 5, column = 1, pady = 10, padx = 25)

# number of runs
runnumvar = tkr.IntVar()
tkr.Label(root, text ="#Feedings/Cone (1-100)").place(x=30 ,y= 530)#.grid(row =7)
mnu7 = OptionMenu(root,runnumvar,N0,N0,N1,N2,N3,N4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25)
mnu7.place(x=200,y=530)#.grid(row = 8, column = 0, pady = 5, padx = 25) 
   
# Feeding Intervals
intervalvar = tkr.IntVar()
tkr.Label(root, text ="Feeding Intervals(hours)").place(x= 30,y= 560)#.grid(row =9)
mnu8 = OptionMenu(root,runnumvar,N0,N0,N1,N2,N3,N4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25)
mnu8.place(x= 200,y= 560)#.grid(row = 10, column = 0, pady = 5, padx = 25) 


def varBox():
    varLabel()
#    top = Toplevel()
#    top.title("Variables")
#    top.geometry('270x300')

    #place them this is just to prove that we can get the inputs and move them around
#    int_var = varGetter(var)
#    tkr.Label(top,text = int_var ).grid(row =1)
#    int_var2 = varGetter(var2)
#    tkr.Label(top,text = int_var2).grid(row =2)
#    int_var3 = varGetter(var3)
#    tkr.Label(top,text = int_var3).grid(row =3)
#    int_var4 = varGetter(var4)
#    tkr.Label(top,text = int_var4).grid(row =4)
#    #exit button closes the program
#    b1 = tkr.Button(top, text = "exit", command = top.quit).grid(row = 5)
#    top.mainloop()



def varLabel():
    int_var = varGetter(tank1var)
    int_var2 = varGetter(tank2var)
    int_var3 = varGetter(tank3var)
    int_var4 = varGetter(tank4var)
    int_var5 = varGetter(tank5var)
    
    
    #tkr.Label(root, text = int_var).grid(row =2, column = 2)
    #tkr.Label(root, text = int_var2).grid(row =3, column = 2)
    #tkr.Label(root, text = int_var3).grid(row =4, column = 2)
    #tkr.Label(root, text = int_var4).grid(row =5, column = 2)
    #tkr.Label(root, text = int_var5).grid(row =6, column = 2)
    
def logfile():
    
    strvar = str(sdelvar)
    strvar2 = str(s1.get())
    strvar3 = str(s2.get())
    strvar4 = str(s3.get())
    strvar5 = str(s4.get())
    strvar6 = str(s5.get())
    strvar7 = str(runnumvar)
    
    AppendTxt = open("Out_file.txt","a")
    AppendTxt.write(" ************************************* \n")
    AppendTxt.write(" Start Delay ------------------- = \n")
    AppendTxt.write(strvar)
    AppendTxt.write("\n Target Concentration for test 1 = \n")
    AppendTxt.write(strvar2)
    AppendTxt.write("\n Target Concentration for test 2 = \n")
    AppendTxt.write(strvar3)
    AppendTxt.write("\n Target Concentration for test 3 = \n")
    AppendTxt.write(strvar4)
    AppendTxt.write("\n Target Concentration for test 4 = \n")
    AppendTxt.write(strvar5)
    AppendTxt.write("\n Target Concentration for test 5 = \n")
    AppendTxt.write(strvar6)
    AppendTxt.write("\n Total # of Runs --------------- = \n")
    AppendTxt.write(strvar7)
    AppendTxt.write("\n ************************************* \n")
    AppendTxt.close()
    AppendTxt = open("logF.txt","a")
    #AppendTxt.write("\n Target Concentration for test 1 = \n")
    AppendTxt.write(strvar2)
    AppendTxt.write(" ")
    #AppendTxt.write("\n Target Concentration for test 2 = \n")
    AppendTxt.write(strvar3)
    AppendTxt.write(" ")
    AppendTxt.write(strvar4)
    AppendTxt.write(" ")
    AppendTxt.write(strvar5)
    AppendTxt.write(" ")
    AppendTxt.write(strvar6)
    AppendTxt.write("\n")
    
    AppendTxt.close()
    
    
    
def deleteLog():
    WriteTxt = open("Out_file.txt", "w")
    WriteTxt.write("")
    WriteTxt.close()
    WriteTxt = open("logF.txt", "w")
    WriteTxt.write("")
    WriteTxt.close()
    
def livefeeding():
    os.system('LiveFeeder')

def Plotter():
    pval = [0] * 10
    pval2 =[0] * 10
    pval3 =[0] * 10
    pval4 =[0] * 10
    pval5 =[0] * 10
    
    #get the values from log.txt
    with open("logF.txt", "r") as f:
        data = f.readlines()
        a=0
        
    for line in data:
        words = line.split()
        #Grab the first number that we can find
        stringy = str(words[0])
        intvar = int(stringy)
        #grab the second
        stringy = str(words[1])
        intvar2 = int(stringy)
        #grab the third
        stringy = str(words[2])
        intvar3 = int(stringy)
        #grab the fourth
        stringy = str(words[3])
        intvar4 = int(stringy)
        #grab the last number on the line
        stringy = str(words[4])
        intvar5 = int(stringy)
        pval[a] = intvar
        pval2[a]=intvar2
        pval3[a]=intvar3
        pval4[a]=intvar4
        pval5[a]=intvar5
        a=a+1
        
    
    y = [1,2,3,4,5]
    a = [pval[0],pval[1],pval[2],pval[3],pval[4]]
    b = [pval2[0],pval2[1],pval2[2],pval2[3],pval2[4]]
    c = [pval3[0],pval3[1],pval3[2],pval3[3],pval3[4]]
    d = [pval4[0],pval4[1],pval4[2],pval4[3],pval4[4]]
    e = [pval5[0],pval5[1],pval5[2],pval5[3],pval5[4]]
    plt.plot(y,a,label = 'Tank 1')
    plt.plot(y,b,label = 'Tank 2')
    plt.plot(y,c,label = 'Tank 3')
    plt.plot(y,d,label = 'Tank 4')
    plt.plot(y,e,label = 'Tank 5')
    plt.legend()
    plt.xlabel("Runs")
    plt.ylabel("Concentration (Artemia/ml)")
    plt.title('History')
    plt.show()

def Plotter10():
    pval = [0] * 30
    pval2 =[0] * 30
    pval3 =[0] * 30
    pval4 =[0] * 30
    pval5 =[0] * 30
    
    #get the values from log.txt
    with open("logF.txt", "r") as f:
        data = f.readlines()
        a=0
        
    for line in data:
        words = line.split()
        #Grab the first number that we can find
        stringy = str(words[0])
        intvar = int(stringy)
        #grab the second
        stringy = str(words[1])
        intvar2 = int(stringy)
        #grab the third
        stringy = str(words[2])
        intvar3 = int(stringy)
        #grab the fourth
        stringy = str(words[3])
        intvar4 = int(stringy)
        #grab the last number on the line
        stringy = str(words[4])
        intvar5 = int(stringy)
        pval[a] = intvar
        pval2[a]=intvar2
        pval3[a]=intvar3
        pval4[a]=intvar4
        pval5[a]=intvar5
        a=a+1
        
    
    y = [1,2,3,4,5,6,7,8,9,10]
    a = [pval[0],pval[1],pval[2],pval[3],pval[4],pval[5],pval[6],pval[7],pval[8],pval[9]]
    b = [pval2[0],pval2[1],pval2[2],pval2[3],pval2[4],pval2[5],pval2[6],pval2[7],pval2[8],pval2[9]]
    c = [pval3[0],pval3[1],pval3[2],pval3[3],pval3[4],pval3[5],pval3[6],pval3[7],pval3[8],pval3[9]]
    d = [pval4[0],pval4[1],pval4[2],pval4[3],pval4[4],pval4[5],pval4[6],pval4[7],pval4[8],pval4[9]]
    e = [pval5[0],pval5[1],pval5[2],pval5[3],pval5[4],pval5[5],pval5[6],pval5[7],pval5[8],pval5[9]]
    plt.plot(y,a,label = 'Tank 1')
    plt.plot(y,b,label = 'Tank 2')
    plt.plot(y,c,label = 'Tank 3')
    plt.plot(y,d,label = 'Tank 4')
    plt.plot(y,e,label = 'Tank 5')
    plt.legend()
    plt.xlabel("Runs")
    plt.ylabel("Concentration (Artemia/ml)")
    plt.title('History')
    plt.show()
    
def Plotter20():
    pval = [0] * 30
    pval2 =[0] * 30
    pval3 =[0] * 30
    pval4 =[0] * 30
    pval5 =[0] * 30
    
    #get the values from log.txt
    with open("logF.txt", "r") as f:
        data = f.readlines()
        a=0
        
    for line in data:
        words = line.split()
        #Grab the first number that we can find
        stringy = str(words[0])
        intvar = int(stringy)
        #grab the second
        stringy = str(words[1])
        intvar2 = int(stringy)
        #grab the third
        stringy = str(words[2])
        intvar3 = int(stringy)
        #grab the fourth
        stringy = str(words[3])
        intvar4 = int(stringy)
        #grab the last number on the line
        stringy = str(words[4])
        intvar5 = int(stringy)
        pval[a] = intvar
        pval2[a]=intvar2
        pval3[a]=intvar3
        pval4[a]=intvar4
        pval5[a]=intvar5
        a=a+1
        
    
    y = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    a = [pval[0],pval[1],pval[2],pval[3],pval[4],pval[5],pval[6],pval[7],pval[8],pval[9],pval[10],pval[11],pval[12],pval[13],pval[14],pval[15],pval[16],pval[17],pval[18],pval[19]]
    b = [pval2[0],pval2[1],pval2[2],pval2[3],pval2[4],pval2[5],pval2[6],pval2[7],pval2[8],pval2[9],pval2[10],pval2[11],pval2[12],pval2[13],pval2[14],pval2[15],pval2[16],pval2[17],pval2[18],pval2[19]]
    c = [pval3[0],pval3[1],pval3[2],pval3[3],pval3[4],pval3[5],pval3[6],pval3[7],pval3[8],pval3[9],pval3[10],pval3[11],pval3[12],pval3[13],pval3[14],pval3[15],pval3[16],pval3[17],pval3[18],pval3[19]]
    d = [pval4[0],pval4[1],pval4[2],pval4[3],pval4[4],pval4[5],pval4[6],pval4[7],pval4[8],pval4[9],pval4[10],pval4[11],pval4[12],pval4[13],pval4[14],pval4[15],pval4[16],pval4[17],pval4[18],pval4[19]]
    e = [pval5[0],pval5[1],pval5[2],pval5[3],pval5[4],pval5[5],pval5[6],pval5[7],pval5[8],pval5[9],pval5[10],pval5[11],pval5[12],pval5[13],pval5[14],pval5[15],pval5[16],pval5[17],pval5[18],pval5[19]]
    plt.plot(y,a,label = 'Tank 1')
    plt.plot(y,b,label = 'Tank 2')
    plt.plot(y,c,label = 'Tank 3')
    plt.plot(y,d,label = 'Tank 4')
    plt.plot(y,e,label = 'Tank 5')
    plt.legend()
    plt.xlabel("Runs")
    plt.ylabel("Concentration (Artemia/ml)")
    plt.title('History')
    plt.show()

plot5 = tkr.Button(root, text = 'Plot 5  ', command = Plotter)
plot5.place(x=600,y=500)
#b4.grid(row = 3, column =2, pady = 10, padx = 100)
plot10 = tkr.Button(root, text ='Plot 10',command = Plotter10)
plot10.place(x=600 ,y=535 )
plot20 = tkr.Button(root, text ='Plot 20',command = Plotter20)
plot20.place(x= 600, y= 570)
    
b1 = tkr.Button(root, text = "Variables", command = varBox)
b1.place(x=1200,y=45)
#b1.grid(row = 1, column = 2, pady = 10, padx = 100)
b2 = tkr.Button(root, text = "LOG ITEMS", command = logfile)
b2.place(x=1200,y=80)
#b2.grid(row = 2, column = 2, pady = 10, padx = 100)

b3 = tkr.Button(root, text = "clear LOG", command = deleteLog)
b3.place(x=1200,y=115)
#b3.grid(row = 4, column =2, pady = 10, padx = 100)
LFB = tkr.Button(root, text = "GOING LIVE", command = livefeeding)
LFB.place(x=1200,y=150)
#LFB.grid(row = 5, column =2, pady = 10, padx = 100)


root.mainloop() 

