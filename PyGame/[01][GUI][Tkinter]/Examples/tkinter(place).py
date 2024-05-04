'''
Tkinter-place
'''

import tkinter as tk

app = tk.Tk()
app.geometry('300x300') 

labelA = tk.Label(app, text = "Label (0, 0)", fg="blue", bg="#FF0")
labelB = tk.Label(app, text = "Label (20, 20)", fg="green", bg="#300")
labelC = tk.Label(app, text = "Label (40, 50)", fg="black", bg="#f03")
labelD = tk.Label(app, text = "Label (0.8, 0.8)", fg="orange", bg="#0ff")

labelA.place(x=0, y=0)
labelB.place(x=20, y=20)
labelC.place(x=40, y=50)
labelD.place(relx=0.8, rely=0.8)

app.mainloop()