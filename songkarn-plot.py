# Python Data Visualization with Tkinter by Uncle Engineer
# www.facebook.com/UncleEngineer

from tkinter import *


GUI = Tk()
GUI.title('Songkran Accident Statistic by Uncle Engineer')
C = Canvas(GUI, height=500, width=500)

mappic = PhotoImage(file='map.png')
createmap = C.create_image(250,250,image=mappic, anchor=CENTER)

def createcircle(x,y,r,col):
    x1 = x - r
    x2 = x + r
    y1 = y - r
    y2 = y + r
    coord = x1,y1,x2,y2
    circle = C.create_oval(coord, outline=col,width=2)

region = ['Bangkok','Central','Westhern','Eastern','Northeastern','Southern','Northern']
stat = [46,109,31,49,178,43,57]
coordinate = [(199,243),(193,180),(146,217),(246,271),(280,166),(166,425),(161,83)]
color = []

for ac in stat:
    if ac > 100:
        color.append('red')
    else:
        color.append('orange')

for i,pos in enumerate(coordinate):
    createcircle(pos[0],pos[1],stat[i]*0.3,color[i])
    print("Region: %s \nPass away: %d person"%(region[i],stat[i]))
    print("---------------------------------")

#Checkposition by click
def checkposition(event):
    print("Position X: ",event.x)
    print("Position Y: ",event.y)

C.bind("<Button 1>",checkposition)

C.pack()
GUI.mainloop()

#http://rvpreport.rvpeservice.com/viewrsc.aspx?report=0545&session=16
