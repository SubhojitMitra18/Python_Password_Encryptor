from tkinter import *
from tkinter import messagebox
import base64
import os

def decrypt():
    key=code.get()

    if key=='1234':
        screen2=Toplevel(screen)
        screen2.title("Decrypted Password")
        screen2.geometry("400x200")
        screen2.configure(bg="#212F3D")

        password=text1.get(1.0,END)
        enpassword=password.encode("ascii")
        base64_bytes=base64.b64decode(enpassword)
        decrypt=base64_bytes.decode("ascii")

        Label(screen2, text="Decrypted Message", font=("Arial", 14), fg="white", bg="#28B463").place(x=10, y=10)
        text2=Text(screen2, font=("Calibri", 12), bg="white", fg="black", relief=GROOVE, wrap=WORD, bd=2)
        text2.place(x=10, y=50, width=370, height=120)
        text2.insert(END,decrypt)

    elif key=="":
        messagebox.showerror("Error","Please provide the key")
    elif key!="1234":
        messagebox.showerror("Error","Wrong Key")

def encrypt():
    key=code.get()

    if key=='1234':
        screen1=Toplevel(screen)
        screen1.title("Encrypted Password")
        screen1.geometry("400x200")
        screen1.configure(bg="#212F3D")

        password=text1.get(1.0,END)
        enpassword=password.encode("ascii")
        base64_bytes=base64.b64encode(enpassword)
        encrypt=base64_bytes.decode("ascii")

        Label(screen1, text="Encrypted Message", font=("Arial", 14), fg="white", bg="#28B463").place(x=10, y=10)
        text2=Text(screen1, font=("Calibri", 12), bg="white", fg="black", relief=GROOVE, wrap=WORD, bd=2)
        text2.place(x=10, y=50, width=370, height=120)
        text2.insert(END,encrypt)

    elif key=="":
        messagebox.showerror("Error","Please provide the key")
    elif key!="1234":
        messagebox.showerror("Error","Wrong Key")

def frontend():

    global screen
    global text1
    global code
    
    screen = Tk()
    screen.geometry("400x400")
    screen.title("Password Encryption & Decryption")
    screen.configure(bg="#2E86C1")
    
    def reset():
        code.set("")
        text1.delete(1.0,END)

    # Title Label
    Label(screen, text="Encrypt or Decrypt Your Password", fg="white", bg="#2E86C1", font=("Helvetica", 16, "bold")).place(x=40, y=10)

    # Text box to enter password
    text1 = Text(screen, font=("Arial", 12), bg="white", fg="black", relief=GROOVE, wrap=WORD, bd=2)
    text1.place(x=20, y=60, width=360, height=100)
    
    # Secret key label and entry box
    Label(screen, text="Enter Secret Key", fg="white", bg="#2E86C1", font=("Helvetica", 14)).place(x=20, y=180)
    code = StringVar()
    Entry(screen, textvariable=code, width=20, bd=2, font=("Helvetica", 14), show="*").place(x=20, y=210)

    # Buttons for Encrypt, Decrypt, and Reset
    Button(screen, text="Encrypt", height=2, width=15, bg="#28B463", fg="white", bd=0, font=("Helvetica", 12), command=encrypt).place(x=20, y=260)
    Button(screen, text="Decrypt", height=2, width=15, bg="#28B463", fg="white", bd=0, font=("Helvetica", 12), command=decrypt).place(x=200, y=260)
    Button(screen, text="Reset", height=2, width=34, bg="#E74C3C", fg="white", bd=0, font=("Helvetica", 12), command=reset).place(x=20, y=320)

    screen.mainloop()

frontend()