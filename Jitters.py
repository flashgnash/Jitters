#JitterKeys
import sys,tkinter,keyboard
from tkinter import *
from tkinter import ttk

ThemeSelected = "light"
modifier_start = "shift"
modifier_list = "shift","ctrl","tab","alt"
available_themes = "dark","light"

def close(window):
    window.destroy()
    quit()

def style(theme):
    if theme == "light":
        return {"BG":"darkgray","TCol":"orange","MTCol":"black","Title":"Jitters [light]","other":"gray"}              
    else:
        return {"BG":"darkgray","TCol":"black","MTCol":"white","Title":"Jitters [dark]","other":"indigo"}
    
root = Tk()
root.update()
    

modifier = StringVar(root)
modifier.set(modifier_start)

root.protocol("WM_DELETE_WINDOW",lambda: close(root))
global Theme
Theme = style(ThemeSelected)
root.title(Theme["Title"])
root.configure(background=Theme["BG"])

if sys.platform.find("win") != -1: #Custom menu bar on windows
    root.attributes("-toolwindow",0,"-topmost",1,"-alpha",0.8)
    root.overrideredirect(1)

    def move(event):
        root.geometry('+'+str(event.x_root - 150)+'+'+str(event.y_root))

    TBar = Frame(root,relief=RAISED)
    
    L1 = Label(master=TBar,relief="flat")
    L1.pack(side="left",fill=Y)    

    ExitButton = Button(master=TBar,bg="red",relief=FLAT,width=1,command=lambda: close(root))
    ExitButton.pack(side=RIGHT)

    TBar.pack(fill=X)

    TBar.bind('<B1-Motion>',move)
    
L2 = Label(text="Jitters",font = ('Courier', 50))
L2.pack(pady=10)

KeyLabel = Label(text="Key combo to toggle the auto keypressing")
KeyLabel.pack()


entrybox = Frame()
entrybox.pack()

Dropdown = OptionMenu(entrybox,modifier,*modifier_list)
Dropdown.configure(font = ('Courier', 15))
Dropdown.pack(side="left",pady=1)


ThePlus = Label(master=entrybox,text=" + ",font = ('Courier', 20))
ThePlus.pack(side="left")

E1 = Entry(master=entrybox,width=1,font = ('Courier', 20))
E1.pack(side="left",pady=5)

L3 = Label(text="Text to be autotyped (use /// for enter)")
L3.pack(pady=20)

E2 = Entry(width=20,font = ('Courier', 20),)
E2.pack(side="top",pady=5)

def makeahotkeynowplease():
    Hotkey = modifier.get()+", "+E1.get()
    try:
        keyboard.remove_hotkey(Hotkey)
    except:
        print("Hotkey ["+Hotkey+"] created for the first time")
    TextToType = E2.get().replace("///","\n")
    keyboard.add_hotkey(Hotkey,lambda: keyboard.write(TextToType))



BottomFrame = Frame()
BottomFrame.pack(side="bottom",fill=X)

B1 = Button(master=BottomFrame,text="Apply",width=7,command=makeahotkeynowplease)
B1.pack(pady=3)

ThemeSelector = StringVar()
ThemeSelector.set("light")
ThemeDropDown = OptionMenu(BottomFrame,ThemeSelector,*available_themes)
ThemeDropDown.pack(side="left")
'''
HotkeyList = ["a","q","j","e"]
def keyrelease(key):
    if key.name in HotkeyList:
        IDK.set("Hotkey "+key.name+" triggered")
    else:
        IDK.set("Key Pressed: "+key.name)

keyboard.on_release(keyrelease)
'''
root.geometry("450x350")
def applyTheme(idontcare,about,thesevariables):
    Theme = style(ThemeSelector.get())
    if sys.platform.find("win") != -1:
        TBar.configure(bg=Theme["TCol"])
        L1.configure(text=Theme["Title"],background=Theme["TCol"],fg=Theme["MTCol"])
    root.title(Theme["Title"])
    root.configure(bg=Theme["BG"])
    L2.configure(background=Theme["other"],fg=Theme["MTCol"])
    KeyLabel.configure(fg=Theme["MTCol"],bg=Theme["other"])
    entrybox.configure(bg=Theme["BG"])
    Dropdown.configure(bg=Theme["BG"],fg=Theme["MTCol"])
    ThePlus.configure(bg=Theme["BG"],fg=Theme["MTCol"])
    L3.configure(fg=Theme["MTCol"],bg=Theme["other"])
    B1.configure(bg=Theme["other"],fg=Theme["MTCol"])
    BottomFrame.configure(bg=Theme["BG"])
    ThemeDropDown.configure(bg=Theme["BG"],fg=Theme["MTCol"])
    
    
applyTheme("these","are","useless")

ThemeSelector.trace("w", applyTheme)
root.mainloop()