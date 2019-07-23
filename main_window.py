from tkinter import *

root = Tk()
root.title('Crypt your text')
canvas = Canvas(root, height=600, width=800)
canvas.pack()

bg_image = PhotoImage(file='img/background.png')
bg_label = Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

input_frame = Frame(root, bg='#304430', bd=5)
input_frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.4, anchor=N)

entry = Entry(input_frame, font=('Terminal', 20))
entry.place(relwidth=0.65, relheight=1)

button = Button(input_frame, text='Run Cipher', font=('Terminal', 15),
                command=lambda: getWeather(entry.get()))
button.place(relx=0.8, rely=0, relwidth=0.2, relheight=0.1)


output_frame = Frame(root, bg='#304430', bd=10)
output_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor=N)

label = Label(output_frame, font=('Terminal', 20), anchor=NW, justify=LEFT, bd=5)
label.place(relwidth=1, relheight=1)

root.mainloop()