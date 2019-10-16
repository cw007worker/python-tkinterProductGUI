from tkinter import *
from tkinter import ttk, messagebox
import csv

def writetocsv(data):
    with open('data.csv','a',newline='') as f:
        fw = csv.writer(f)
        fw.writerow(data)
        print('CSV was writen')
        

def Addproduct():
    calculate = int(Price.get())* int(Quantity.get())
    text = "Product Name: {}\nPrice: {}\nQuantity: {}\nTotal: {}".format(Name.get(),Price.get(),Quantity.get(),calculate)
    datatocsv = [Name.get(),Price.get(),Quantity.get(),calculate]
    print(text)
    Res.set(text)
    writetocsv(datatocsv)
    messagebox.showinfo('Adding..','Product was added')

GUI = Tk()
GUI.title('Python GUI : Ama Shop')
GUI.geometry('700x500')

#Label and Entry
#----------------------Row 0---------------------
LName = ttk.Label(GUI, text='Product Name',font=(None,18))
LName.grid(row=0,column=0,padx=10,pady=10)

Name = StringVar()

EName = ttk.Entry(GUI, textvariable=Name,font=(None,18))
EName.grid(row=0,column=1,padx=10,pady=10)
#----------------------Row 1---------------------
LPrice = ttk.Label(GUI, text='Price',font=(None,18))
LPrice.grid(row=1,column=0,padx=10,pady=10)

Price = StringVar()

EPrice = ttk.Entry(GUI, textvariable=Price,font=(None,18))
EPrice.grid(row=1,column=1,padx=10,pady=10)
#----------------------Row 2---------------------
LQuantity = ttk.Label(GUI, text='Quantity',font=(None,18))
LQuantity.grid(row=2,column=0,padx=10,pady=10)

Quantity = StringVar()

EQuantity = ttk.Entry(GUI, textvariable=Quantity,font=(None,18))
EQuantity.grid(row=2,column=1,padx=10,pady=10)
#----------------------Row 3---------------------
# This is Button 
BAdd = ttk.Button(GUI, text='Add',command=Addproduct)
BAdd.grid(row=3,column=1,padx=10,pady=10)


#Create Result Label (RL)
Res = StringVar()
Res.set('Result')

#fg is foreground fg for Label Not ttk.Label
RLRes = ttk.Label(GUI, textvariable=Res,font=(None,18,'bold'),foreground='green')
RLRes.grid(row=4,column=1,padx=10,pady=10)

GUI.mainloop()

#thank you for watching.. follow us : github.com/UncleEngineer
