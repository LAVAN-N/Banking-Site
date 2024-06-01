import csv
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from tkinter.ttk import Combobox

# Create a new window
root = tk.Tk()
root.title("Banking Site")
f=Frame(root,height=550,width=1040,bg='black')
f.place(x=10,y=10)
root.config(bg='blue')
img=PhotoImage(file="imgs/bank.png")
root.iconphoto(False, img)

# Set the initial size of the window
root.geometry("1060x580")

# Allow the user to resize the window horizontally and vertically
root.resizable(True, True)

# Create labels and input fields for the user's information

tk.Label(root, text="Account number : ",foreground="white" , font = 'sans-serif 14 bold',bg="black").place(x=340, y=190,anchor='e')
account_entry = tk.Entry(root,width=22,bd=4,font = 'sans-serif 14 bold',textvariable = int)
account_entry.place(x=600, y=190,anchor='e')

tk.Label(root, text="Name : ",foreground="white" , font = 'sans-serif 14 bold',bg="black").place(x=340, y=240,anchor='e')
name_entry = tk.Entry(root,width=22,bd=4,font = 'sans-serif 14 bold',textvariable = str)
name_entry.place(x=600, y=240,anchor='e')

tk.Label(root, text="Phone number : ",foreground="white" , font = 'sans-serif 14 bold',bg="black").place(x=340, y=290,anchor='e')
phone_entry = tk.Entry(root,width=22,bd=4,font = 'sans-serif 14 bold',textvariable = int)
phone_entry.place(x=600, y=290,anchor='e')

tk.Label(root, text="Occupation : ",foreground="white" , font = 'sans-serif 14 bold',bg="black").place(x=340, y=340,anchor='e')
occupation_entry=Combobox(root,values=['Student','Job','Business','Other'],width=14,font = 'sans-serif 10 bold')
occupation_entry.place(x=480, y=340,anchor='e')

tk.Label(root, text="Address : ",foreground="white" , font = 'sans-serif 14 bold',bg="black").place(x=340, y=390,anchor='e')
address_entry = tk.Entry(root,width=22,bd=4,font = 'sans-serif 14 bold',textvariable = str)
address_entry.place(x=600, y=390,anchor='e')

# Define a function to save the user's information to a CSV file
def save_info():
    account = account_entry.get()
    name = name_entry.get()
    phone = phone_entry.get()
    occupation = occupation_entry.get()
    address = address_entry.get()
    
    
    with open("banking_information.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([account,name,phone,occupation,address])
        
    # Clear the input fields after saving the data
    account_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    occupation_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    
    

# Add a button to save the user's information
save_button = tk.Button(root, text="Submit",foreground="black" , font = 'monospace 12 bold',bg="light blue", command=save_info,width=6)
save_button.place(x=420, y=450,anchor='e')

# frame

a=Frame(root,height=2,width=290,bg="white")
a.place(x=700,y=120)

b=Frame(root,height=145,width=184,bg="white")
b.place(x=700,y=120)

c=Frame(root,height=2,width=290,bg="white")
c.place(x=700,y=265)

f=Frame(root,height=2,width=290,bg="white")
f.place(x=700,y=285)

g=Frame(root,height=2,width=290,bg="white")
g.place(x=700,y=300)

h=Frame(root,height=200,width=290,bg="white")
h.place(x=700,y=315)

d=Frame(root,height=148,width=2,bg="white")
d.place(x=990,y=120)


e=Frame(root,height=2,width=292,bg="white")
e.place(x=700,y=200)

# messages

m1 = Label(root , text = "YOUR" , font = 'Georgia 30 bold',bg="white")
m1.place(x=750, y=128)

m2 = Label(root , text = "BANK" ,foreground="white", font = 'monospace 27 bold',bg="black")
m2.place(x=820, y=178)

m3 = Label(root , text = "Your" ,foreground="black", font = 'georgia 18 italic',bg="white")
m3.place(x=800, y=325)

m4 = Label(root , text = "Investments $" ,foreground="yellow", font = 'monospace 15 bold',bg="black",width=22)
m4.place(x=710, y=370)

m5 = Label(root , text = "we are" ,foreground="black", font = 'Verdana 18 italic',bg="white")
m5.place(x=789, y=405)

m6 = Label(root , text = " \"",foreground="white", font = 'Verdana 15 bold',bg="white")
m6.place(x=740, y=447)

m6 = Label(root , text = "Guarantee!!" ,foreground="red", font = 'monospace 15 bold',bg="black",width=22)
m6.place(x=710, y=450)

def main():
    # Run the window
    root.mainloop()

if __name__=='__main__':
    main()

#Developed by @lavanyan