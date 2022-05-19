

# GUI
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox

root = Tk()
root.title("Standing order APP")
root.geometry("800x600")
root.option_add('*font', 'tahoma 12')
frame = Frame(root)
frame.pack()

#Label
onsetLabel = Label(frame, text="Onset Time(hr)", width=14, anchor=W)
onsetLabel.grid(column=0, row=0, padx=5, pady=10)
sbpLabel = Label(frame, text="SBP(mmHg)", width=14, anchor=W)
sbpLabel.grid(column=0,row=1, padx=5,pady=10)
dbpLabel = Label(frame, text="DBP(mmHd)", width=14, anchor=W)
dbpLabel.grid(column=2,row=1, padx=5,pady=10)
nihssLabel = Label(frame, text="NIHSS Score", width=14, anchor=W)
nihssLabel.grid(column=0,row=2, padx=5,pady=10)

#Altepase indication variable
onset = DoubleVar()
sbp = IntVar()
dbp = IntVar()
nihss = IntVar()

#Entry box
entry1 = Entry(frame, textvariable=onset, width=12)
entry1.grid(column=1, row=0, padx=5, pady=10)
entry2 = Entry(frame, textvariable=sbp, width=12)
entry2.grid(column=1, row=1, padx=5, pady=10)
entry3 = Entry(frame, textvariable=dbp, width=12)
entry3.grid(column=3, row=1, padx=5, pady=10)
entry4 = Entry(frame, textvariable=nihss, width=12)
entry4.grid(column=1, row=2, padx=5, pady=10)

#Check Altepase indication
def altepaseIndication() :

    if float(onset.get()) < 4.5 and int(sbp.get()) < 185 and int(dbp.get()) <110 and int(nihss.get()) >= 5:
        messagebox.showinfo("Result", "Altepase is indicated")
    elif float(onset.get()) > 3.5:
        messagebox.showinfo("Result", "Altepase isn't indicated due to onset > 4.5 hrs")
    elif int(sbp.get()) > 185 or int(dbp.get()) > 110:
        messagebox.showinfo("Result", "Altepase isn't indicated due to uncontrollable BP")
    elif int(nihss.get()) < 5:
        messagebox.showinfo("Result", "Altepase isn't indicated due to NIHSS Score 0-5 => no benefit")


confirm = Button(frame, text="Check", width=14, height=2, compound="left", command=altepaseIndication)
confirm.grid(column=0, row=4, padx=10,pady=10)

root.mainloop()
# Check for indication for Altepase

# Altepase indication Variable
#onset = float(input("Onset Time :"))
#sbp = int(input("SBP :"))
#dbp = int(input("DBP :"))
#nihss = int(input("NIHSS Score :"))

#Altepase contraindication Variable
#ich = bool(input())

#def altepaseIndication() :
#    if onset < 4.5 and sbp < 185 and dbp <110 and nihss >= 5:
 #       print("Altepase Indicated")
  #  else:
   #     print("Altepase isn't indicated")

