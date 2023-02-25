from tkinter import *
import random
from PIL import Image, ImageTk


def dice1():
    def ran_gen():
        a = random.randint(0, 5)
        lis1 = ["1.png", "2.png", "3.png", "4.png", "5.png", "6.png"]
        img1 = ImageTk.PhotoImage(Image.open(lis1[a]))
        lbl3.configure(image=img1)  # configuring the image in label
        lbl3.image = img1

    root1 = Tk()
    root1.geometry("800x800")

    fd1 = Frame(root1, bg="RED", borderwidth=2)
    fd1.pack()
    fd1.place(anchor='center', relx=0.5, rely=0.5)
    photo1 = ImageTk.PhotoImage(Image.open("dice.jpg"))
    label = Label(root1, text="DICE SIMULATOR", fg="red", font=("times new roman", 20))
    label.pack(side=TOP, pady=50)
    lbl3 = Label(fd1, image=photo1)
    lbl3.pack()
    button2 = Button(root1, text="ROLL THE DICE", bg="pink", command=ran_gen, relief=GROOVE)
    button2.pack(side=BOTTOM, pady=50)

    root1.mainloop()


def dice2():
    def ran_gen1():
        b = random.randint(0, 7)
        lis = ["1.png", "2.png", "3.png", "4.png", "5.png", "6.png", "6.png", "6.png"]
        img = ImageTk.PhotoImage(Image.open(lis[b]))
        lbl4.configure(image=img)  # configuring the image in label
        lbl4.image = img

    root2 = Tk()
    root2.geometry("800x800")

    fd2 = Frame(root2, bg="RED", borderwidth=2)
    fd2.pack()
    fd2.place(anchor='center', relx=0.5, rely=0.5)
    photo2 = ImageTk.PhotoImage(Image.open("dice.jpg"))
    label2 = Label(root2, text="DICE SIMULATOR", fg="red", font=("times new roman", 20))
    label2.pack(side=TOP, pady=50)
    lbl4 = Label(fd2, image=photo2)
    lbl4.pack()
    button4 = Button(root2, text="ROLL THE DICE", bg="pink", command=ran_gen1, relief=GROOVE)
    button4.pack(side=BOTTOM, pady=50)

    root2.mainloop()


if __name__ == '__main__':
    print("___________________________________")
    print("1.DICE(20% changes of getting 6)")
    print("2.DICE(70% changes of getting 6)")

    user = int(input("Select the dice : "))
    if user == 1:
        dice1()
    elif user == 2:
        dice2()
    else:
        print("! Invalid Choice !")


