'''
Tkinter-pack-fill
'''

import tkinter as tk
    
app = tk.Tk()
app.geometry('300x200')

buttonX = tk.Button(app, text="Fill X", bg="red", height=5)
buttonX.pack(fill='x')

buttonY = tk.Button(app, text="Fill Y", bg="green", width=10)
buttonY.pack(side='left', fill='y')

app.mainloop()