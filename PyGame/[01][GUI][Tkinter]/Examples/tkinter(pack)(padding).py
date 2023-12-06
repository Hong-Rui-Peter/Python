'''
Tkinter-pack-padding
'''

import tkinter as tk
    
app = tk.Tk()
app.geometry('300x200')

buttonW = tk.Button(app, text="West")
buttonW.pack(side='left', ipadx=20, padx=30)

buttonE = tk.Button(app, text="East")
buttonE.pack(side='right', ipadx=20, padx=30)

app.mainloop()