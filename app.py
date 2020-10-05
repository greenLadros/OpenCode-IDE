#ivri korem 2020
"""
description
"""

#init
#import
from tkinter import *
from tkinter import ttk, filedialog
from os import mkdir, path
from assets.themes import themes 

#creating the gui
#creating the window seetings
root = Tk()
root.title("OpenCode - IDE")
#root.iconbitmap(" ")
root.geometry("1800x3500")
root.minsize(240, 200)
#root.attributes("-fullscreen", True)

# NOTE suggestions
# split things up into different files, makes code more managable
# be super careful with memory usage, python is not great at doing big projects and uses alot of memory (shrink things down)
# tkinter is somewhat limiting, might be a issue for some features
# terminal is in every modern IDE, i already dont like how stressful that sounds to implement

#########################creating toolbar########################
toolBar = Menu(root)

#creating menus
#creating commands for file menu


#TODO: use tk.filedialog, doing any with files creates them inside the repo, not ideal
class FileMenu():
    def CreateNewFile(self):
        fileLocation = filedialog.asksaveasfilename() # it probably doesnt even need to save, just create the new tab
        open(f"{fileLocation}","w+")
        createNewTab(fileLocation)

    # I really dont think you need to create new folders + no support for this in tkinter.filedialog
    def CreateNewFolder(self):
        popup = Tk()
        Label(popup).pack() #for space
        popup.geometry("200x120")
        entry = Entry(popup, width=25)
        entry.pack()
        Label(popup).pack() #for space
        def command():
            mkdir(f"{entry.get()}")
            popup.destroy()
        Button(popup, text="Save", padx=25, pady=10, command=command).pack()

    def OpenFile(self):
        fileLocation = filedialog.askopenfile()
        f = open(f'{fileLocation}', 'r')
        createNewTab(fileLocation)

    def OpenFolder(self):
        filedialog.askdirectory()

    def SaveFile(self):
        filename = Notepads[0] # not the best solution
        if path.exists(filename):
            content = Notepads[0] # not the best solution
            open(filename, "w").write(content)
        else:
            self.SaveFileAs()

    def SaveFileAs(self):
        content = Notepads[0].get(1.0, END)
        fileLocation = filedialog.asksaveasfile()
        open(f"{fileLocation}","w+").write(content)


fm = FileMenu()

#creating file menu
fileMenu = Menu(toolBar, tearoff=False)

fileMenu.add_command(label="New File", accelerator="Ctrl+N", command=fm.CreateNewFile)
fileMenu.add_command(label="New Folder", accelerator="Ctrl+Shift+N", command=fm.CreateNewFolder)
fileMenu.add_command(label="Open File", accelerator="Ctrl+O", command=fm.OpenFile)
fileMenu.add_command(label="Open Folder", accelerator="Ctrl+Alt+O", command=fm.OpenFolder)
fileMenu.add_command(label="Save", accelerator="Ctrl+S", command=fm.SaveFile)
fileMenu.add_command(label="Save As...", accelerator="Ctrl+Shift+S", command=fm.SaveFileAs)
fileMenu.add_checkbutton(label="Auto Save")


#creating commands for edit menu
class EditMenu():
    def Undo(self):
        pass
    def Redo(self):
        pass
    def Cut(self):
        pass
    def Copy(self):
        pass
    def Paste(self):
        pass
    def Find(self):
        #TODO: use Regex, pop up window maybe, seems like a hassle
        pass

em = EditMenu()

#creating edit menu
editMenu = Menu(toolBar, tearoff=False)

editMenu.add_command(label="Undo", accelerator="Ctrl+Z", command=em.Undo)
editMenu.add_command(label="Redo", accelerator="Ctrl+Y", command=em.Redo)
editMenu.add_command(label="Cut", accelerator="Ctrl+X", command=em.Cut)
editMenu.add_command(label="Copy", accelerator="Ctrl+C", command=em.Copy)
editMenu.add_command(label="Paste", accelerator="Ctrl+V", command=em.Paste)
editMenu.add_command(label="Find", accelerator="Ctrl+F", command=em.Find)


#creating commands for view menu
class ViewMenu():
    def goFullScreen(self):
        root.attributes("-fullscreen", True)
    
    def createEditorTheme(self):
        pass

    def importEditorTheme(self):
        pass

vm = ViewMenu()

#creating view menu
viewMenu = Menu(toolBar, tearoff=False)

editorTheme = Menu(viewMenu, tearoff=False)
viewMenu.add_command(label="Full Screen", accelerator="F11", command=vm.goFullScreen)
viewMenu.add_checkbutton(label="Enable Mark Errors")
viewMenu.add_command(label="Create Editor Theme", command=vm.createEditorTheme)
viewMenu.add_command(label="Import Editor Theme", command=vm.importEditorTheme)

## not sure
themeChoice = StringVar(root)

colorThemes = themes.colorThemes

for theme in colorThemes:
    editorTheme.add_radiobutton(label=theme, variable=themeChoice)
## not sure

#creating commands for prefrences menu
class PrefrencesMenu():
    def popupConfigure(self):
        pass
    
    def popupShortcuts(self):
        pass
    
    def createEditorExtension(self):
        pass

pm = PrefrencesMenu()

#creating prefrences menu
prefrencesMenu = Menu(toolBar, tearoff=False)

prefrencesMenu.add_command(label="Configure", command=pm.popupConfigure)
prefrencesMenu.add_checkbutton(label="Enable Hints")
prefrencesMenu.add_command(label="Shortcuts", command=pm.popupShortcuts)
prefrencesMenu.add_command(label="Create Extension", command=pm.createEditorExtension)


#creating commands for help menu
class HelpMenu():
    def popupHelp(self):
        pass

    def openWelcomeFile(self):
        content = open('welcome.md', 'r').read()
        global comp

        #creating the notepad tab
        Tabs[comp] = Frame(tabs, padx=5, pady=5)       #not finished
        Notepads[comp] = Text(Tabs[comp], padx=500, pady=300)
        Notepads[comp].config(wrap="word", relief=FLAT)

        scroll = Scrollbar(Tabs[comp])
        Notepads[comp].focus_set()
        scroll.config(command=Notepads[comp].yview)
        Notepads[comp].config(yscrollcommand=scroll.set)
        Notepads[comp].insert(END, content)

        #displaying everything
        Notepads[comp].pack(fill=BOTH, expand=True)
        Tabs[comp].pack(fill=BOTH, expand=True)
        tabs.add(Tabs[comp], text="Welcome")
    
        #incremeting the comparison
        comp += 1

    
    def openExplanationFile(self):
        pass
    
    def openContributeFile(self):
        pass

hm = HelpMenu()

#creating help menu
helpMenu = Menu(toolBar, tearoff=False)

helpMenu.add_command(label="Help", accelerator="Ctrl+Shift+H", command=hm.popupHelp)
helpMenu.add_command(label="How to get started?", accelerator="Ctrl+Shift+W", command=hm.openWelcomeFile)
helpMenu.add_command(label="What is OpenCode ?", command=hm.openExplanationFile)
helpMenu.add_command(label="How can i contribute?", command=hm.openContributeFile)
helpMenu.add_command(label="How to create editor themes?", command=hm.openContributeFile)
helpMenu.add_command(label="How to create extension?", command=hm.openContributeFile)

#adding all the menus to the toolbar
toolBar.add_cascade(label="File", menu=fileMenu)

toolBar.add_cascade(label="Edit", menu=editMenu)

toolBar.add_cascade(label="View", menu=viewMenu)
viewMenu.add_cascade(label="Editor Theme", menu=editorTheme)

toolBar.add_cascade(label="Prefrences", menu=prefrencesMenu)

toolBar.add_cascade(label="Help", menu=helpMenu)

#displaying the toolbar
root.config(menu = toolBar)
#------------------------ending toolbar-----------------------#


#########################creating sidebar########################

#------------------------ending sidebar-----------------------#


#########################creating FileExplorer########################

#------------------------ending FileExplorer-----------------------#


#########################creating NotePad########################
#creating tabs
tabs = ttk.Notebook(root)
tabs.pack(pady=10)
Tabs = {}
Notepads = {}
comp = 0

def createNewTab(fileName):
    global comp

    #creating the notepad tab
    Tabs[comp] = Frame(tabs, padx=5, pady=5)       #not finished
    Notepads[comp] = Text(Tabs[comp], padx=500, pady=300)
    Notepads[comp].config(wrap="word", relief=FLAT)

    scroll = Scrollbar(Tabs[comp])
    Notepads[comp].focus_set()
    scroll.config(command=Notepads[comp].yview)
    Notepads[comp].config(yscrollcommand=scroll.set)

    #displaying everything
    Notepads[comp].pack(fill=BOTH, expand=True)
    Tabs[comp].pack(fill=BOTH, expand=True)
    tabs.add(Tabs[comp], text=fileName)
    
    #incremeting the comparison
    comp += 1

hm.openWelcomeFile()

#font family and font size usage

##
#------------------------ending NotePad-----------------------#


#########################creating console########################

#------------------------ending console-----------------------#



#running main loop
root.mainloop()