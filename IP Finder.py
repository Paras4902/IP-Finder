from tkinter import *
from socket import gethostname, gethostbyname
from tkinter import messagebox as msgbx

root = Tk()
root.geometry("900x500")
root.title("Get IP Address")
root.config(bg="black")
Label(root, text="Welcome to IP Address finder", font=("Times", 35, "bold underline"), bg="black", fg="grey").pack()


def getIP():
    hostname = gethostname()
    ip = gethostbyname(hostname)
    giveip.delete(0, END)
    if ip == "127.0.0.1":
        msgbx.showinfo("No Internet", "You are not connected to Internet\nYour local IP Address will be shown")
        giveip.insert(END, ip)
    else:
        giveip.insert(END, ip)


def quitted():
    msgbx.showinfo("Thanks", "Thanks for Using Our IP Address Finder")
    quit()


Button(root, text="Get IP Address", font=("Times", 25, "bold underline"), bg="black", fg="grey", bd=10, command=getIP).place(x=140, y=100, width=270, height=70)
giveip = Entry(root, bd=10, font=("Times", 25, "bold"))
giveip.place(x=450, y=100, width=240, height=65)
Button(root, text="EXIT!!", font=("Times", 25, "bold underline"), bg="black", fg="grey", bd=10, command=quitted).place(x=750, y=420)
Label(root, text="©Program@Paras4902", font=("Times", 25, "bold"), bg="black", fg="grey", bd=10).pack(side=BOTTOM, anchor=W)
root.mainloop()
