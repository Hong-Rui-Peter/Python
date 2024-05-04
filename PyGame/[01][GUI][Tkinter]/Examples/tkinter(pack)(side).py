'''
Tkinter-pack-side
'''

import tkinter as tk    
    
app = tk.Tk()
app.geometry('300x200')

buttonW = tk.Button(app, text="West", width=15)
buttonW.pack(side='left')

buttonE = tk.Button(app, text="East", width=15)
buttonE.pack(side='right')

app.mainloop()