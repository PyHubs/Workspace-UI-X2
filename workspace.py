#from tkinter import messagebox, filedialog, ttk, import time, os and tkcalander
from tkinter import*
from tkinter import messagebox
from tkinter import filedialog
from tkcalendar import*
from tkinter import ttk
import tkinter as tk
import tkinter as tilGUI
import time
import os 

root = Tk()
root.title("Workspace for windows - Workspace UI X2")
root.configure(bg="Lightgreen")
root.geometry("1325x600")
root.iconbitmap("D:\Izu\python icon sets\icon_ws.ico")

#REALESE NOTES (ALL)
# RELEASE NOTES -- keep track of daily new version

#release note! (1)
    #workspace UI X1.0 (APPLICATION MADE, WILL BE UPDATED ON MAJOR NEXT RELEASE, ALL PATCH NOTES WILL BE NOT TOLD)
    #CONFIRMED as first major release -- X1.0 (developer version 3) (made on thrus-friday(NIGHT, 11:00PM)) week 38

#release note! (2)
    #Workspace IO X3.6 (APPLICATION MADE, REALASE MADE AS SECOND MAJOR RELEASE)
    #confiremed as second major release -- 3.6 (developer version 5) (made on sat (full), RELAESED AS FINAL STAGE)
    #NOT PUBLIC YET, in beta stage (preivews)
    #After previews will be made final and realsed to public -- RELAESE NOTES -- NEED TO PREIVEW DAD (THEN RELEAES AS FINAL (PUBLIC)) week38

#bugs
    #Green_color_error_bug = #big to fix green BG (find bug -- CHECK CODE AND FIX [bug_error_green]) -- FOUND BY PRIVIEW (AKA: relaese note! (2) preview0
    #will convert to exe (as one major version) (take screeshot or snip skecth) (after fixing bug)

#realse note (3) - Bugs note (!1+1.1+1.2 = 1)
   #workspace to 3.6,1 (APPLICATION DEVELOPED, DEVELOOPEMENT MADE name = BIGFIX@forMajor3)
   #fixed bugs are: GREENCOLORBUG9(#C#GREEN#B), PINKCOLORBUG(#C2#PINK#B2) and TITLEBUG(#ROOT#TITLE#B.notemode)
   #bug fixed (VERSION: AO1BUGFIXV3.6.1, CODE=BIXFIXMajor3AOI3.6) 
   #bug fix will be combined with -- BUGFIXMAINONE.3.0version(MajorRelease3) (BUGFIXUPDATE)
   #none updates is released

#release note (4)
    #Workspace to 3.6 (APPLICATION MADE). DEVELOPEMENT MADE - CON

#root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

#time
timeONE = time.strftime('%X')
timeTWO = time.strftime('%X')

#bindings
root.bind('<Escape>', lambda event: root.state('normal'))
root.bind('<F5>', lambda event: root.state('zoomed'))

#making def's
def clock():
    global hms
    hms = time.strftime("%X")    
    clock_label.config(text=hms+ " - Male")
    clock_label.after(500, clock)

def date():
    global day_time
    date_time = time.strftime("%x")
    day_time = time.strftime("%a")
    day_week = time.strftime("%a")
    day_label.configure(text="Date = " +date_time +" - " +day_week)
    day_label.after(199999, date)

def clockifycommand():
    bottom_lbl.configure(text='Notes mode - Workspace UI X2 '+hms)
    bottom_lbl.after(500, clockifycommand)

def enter_fullscreen_command():
    root.state('zoomed')
    pass

def exit_fullscreen_command():
    root.resizable(1,1)
    root.state('normal')
    root.geometry("1325x600")

def hide_app_window_command():
    root.overrideredirect(1)

def show_app_window_command():
    root.overrideredirect(False)

def hide_calander_command():
    the_label.pack_forget()
    name.pack_forget()
    Cal.pack_forget()

def show_calander_command():
    global name
    global the_label
    the_label = Label(root, text='', bg="Lightgreen", font=('Comfortaa', 5))
    the_label.pack()
    name = Label(root, text='Calander', bg="Lightgreen", font=('Comfortaa', 18))
    name.pack()
    Cal.pack()

def exit_command():
    global timepro
    timepro = time.strftime("%X")
    root.destroy()
    print('NOTIFICATION: Workspace for windows X2 closed at ' +timepro)

def show_about_command():
    messagebox.showinfo("About","Workspace UI X2 is a version of workpsace UI, the UI name for workspace for windows.\nVersion workspace for windows X2 (2), workspace UI X2 (3.6)")

def show_help_command():
    messagebox.showinfo("Help","For help email izooizkaan@gmail.com")

#def section - Freezing workspace
def freez_5min_command():
    warningFOUR = messagebox.showwarning("Warning", "Do you want to lock workpsace, until 5 minuetes you cant do anything with workpsace")
    time.sleep(300)
    print('WORKSPACE IS LOCKED')

def freez_3min_command():
    warningTWO = messagebox.showwarning("Warning", "Do you want to lock workpsace, until 03 minuetes you cant do anything with workpsace")
    time.sleep(180)
    print('WORKSPACE IS LOCKED')

def freez_60sec_command():
    warningONE = messagebox.showwarning("Warning", "Do you want to lock workpsace, until 01 minuetes you cant do anything with workpsace")
    time.sleep(60)
    print('WORKSPACE IS LOCKED')

def freez_30sec_command():
    warningTHREE = messagebox.showwarning("Warning", "Do you want to lock workpsace, until 30 seconds you cant do anything with workpsace")
    time.sleep(30)
    print('WORKSPACE IS LOCKED')

def freez_15sec_command():
    warningFIVE = messagebox.showwarning("Warning", "Do you want to lock workpsace, until 15 seconds you cant do anything with workpsace")
    time.sleep(15)
    print('WORKSPACE IS LOCKED')

def freez_5sec_command():
    warningSIX = messagebox.showwarning("Warning", "Do you want to lock workpsace, until 05 seconds you cant do anything with workpsace")
    time.sleep(5)
    print('WORKSPACE IS LOCKED')

#def section - open apps
def link_open_command():
    e = input('Fille location:')
    #___ (TILMAINFWORD*art)seperator
    os.system('"%s"' % e)

def Laungceytictactoey():
    print('NOTIFICATION: Tic tac toe has been opened') 
    os.system('"%s"' %'D:\Izu\Python\Tic-tac-toe.py')
    print('NOTIFICATION: Tic tac toe has been closed')      

def launch_text_editor_command():
    print('NOTIFICATION: Basic Text for windows has been opened')
    os.system('"%s"' %'D:\Izu\Python\Basic Text for windows.py')
    print('NOTIFICATION: Basic Text for windows has been closed')

def launch_basictext30_command():
    print('NOTIFICATION: Basictext 3.0 has been opened')
    os.system('"%s"' %'D:\Izu\Python/basictext3.0.py')
    print('NOTIFICATION: Basictext 3.0 has been closed')

def launch_basictext20_command():
    print('NOTIFICATION: Basic text editor 2.0 has been opened')
    os.system('"%s"' %'D:\Izu\Python\BasicTextEditor2.0.py')
    print('NOTIFICATION: Basic text editor 2.0 has been closed')

def launch_basictext5_command():
    print('NOTIFICATION: Basic text editor 1.0 has been opened')
    os.system('"%s"' %'D:\Izu\Python\BasicTextEditor1.0.py')
    print('NOTIFICATION: Basic text editor 1.0 has been closed')

def launch_simple_payments_app():
    print('NOTIFICATION: simple payment app has been opened')
    os.system('"%s"' %'D:\Izu\Python\Simple payment app.py')
    print('NOTIFICATION: simple payment app has been closed')

def launch_simple_payments_XA():
    print('NOTIFICATION: Simple payment XA has been opened')
    os.system('"%s"' %'D:\Izu\Python\Simple payment XA.py')
    print('NOTIFICATION: Simple payment XA has been closed')

def launch_sublime_text_command():
    print('NOTIFICATION: Sublime text 3 has been opened')
    os.system('"%s"' %'C:\Program Files\Sublime Text 3\sublime_text.exe')
    print('NOTIFICATION: Sublime text 3 has been closed')

def launch_edge_browser_command():
    print('NOTIFICATION: Microsoft edge has been opened')
    os.system('"%s"' %'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe')
    print('NOTIFICATION: Microsoft edge has been closed')

def launch_chrome_browser_command():
    print('NOTIFICATION: Google chrome has been opened')
    os.system('"%s"' %'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
    print('NOTIFICATION: Google chrome has been closed')

def launch_fbr_command():
    print('NOTIFICATION: Flashback Express Recorder has been opened')
    os.system('"%s"' %'C:\Program Files (x86)\Blueberry Software\FlashBack Express 5\FlashBack Recorder.exe')
    print('NOTIFICATION: Flashback Express Recorder has been closed')

def launch_fbp_command():
    print('NOTIFICATION: Flashback Express Player has been opened')
    os.system('"%s"' %'C:\Program Files (x86)\Blueberry Software\FlashBack Express 5\FlashBack Player.exe')
    print('NOTIFICATION: Flashback Express Player has been clsoed')

def other_workspae_command():
    print('NOTIFICATION: Other workspace user (old version) has been opened')
    os.system('"%s"' %'D:\Izu\Python\Workspace for windows - Workspace UI - Other user.py')
    print('NOTIFICATION: Other workspace user (old version) has been closed')

def search_file():
    my_program = filedialog.askopenfilename()
    os.system('"%s"' % my_program)

#def section - Color's, customize workspace
def grey_text_active_bg():
    launch_text_editor_btn.configure(activebackground="Lightgrey")
    exit_btn.configure(activebackground="Lightgrey")
    applist_btn. configure(activebackground="Lightgrey")
    note_btn.configure(activebackground="Lightgrey") 
    launch_text_editor_btn.configure(activebackground="Lightgrey")
    Customize_btn.configure(activebackground="Lightgrey")
    edge_btn.configure(activebackground="Lightgrey")
    tkcopen_btn.configure(activebackground="Lightgrey") 


def orange_text_active_bg():
    launch_text_editor_btn.configure(activebackground="#fed8b1")
    exit_btn.configure(activebackground="#fed8b1")
    applist_btn.configure(activebackground="#fed8b1")
    note_btn.configure(activebackground="#fed8b1") 
    launch_text_editor_btn.configure(activebackground="#fed8b1")
    Customize_btn.configure(activebackground="#fed8b1")
    edge_btn.configure(activebackground="#fed8b1")
    tkcopen_btn.configure(activebackground="#fed8b1") 

def pink_text_active_bg():
    launch_text_editor_btn.configure(activebackground="Pink")
    exit_btn.configure(activebackground="Pink")
    applist_btn.configure(activebackground="Pink")
    note_btn.configure(activebackground="Pink") 
    launch_text_editor_btn.configure(activebackground="Pink")
    Customize_btn.configure(activebackground="Pink")
    edge_btn.configure(activebackground="Pink")
    tkcopen_btn.configure(activebackground="Pink") 

def purple_text_active_bg():
    launch_text_editor_btn.configure(activebackground="#e2d5e8")
    exit_btn.configure(activebackground="#e2d5e8")
    applist_btn.configure(activebackground="#e2d5e8")
    note_btn.configure(activebackground="#e2d5e8") 
    launch_text_editor_btn.configure(activebackground="#e2d5e8")
    Customize_btn.configure(activebackground="#e2d5e8")
    edge_btn.configure(activebackground="#e2d5e8")
    tkcopen_btn.configure(activebackground="#e2d5e8") 

def blue_text_active_bg():
    launch_text_editor_btn.configure(activebackground="Light blue")
    exit_btn.configure(activebackground="Light blue")
    applist_btn.configure(activebackground="Light blue")
    note_btn.configure(activebackground="Light blue") 
    launch_text_editor_btn.configure(activebackground="Light blue")
    Customize_btn.configure(activebackground="Light blue")
    edge_btn.configure(activebackground="Light blue")
    tkcopen_btn.configure(activebackground="Light blue") 

def green_text_active_bg():
    launch_text_editor_btn.configure(activebackground="Light green")
    exit_btn.configure(activebackground="Light green")
    applist_btn.configure(activebackground="Light green")
    note_btn.configure(activebackground="Light green") 
    launch_text_editor_btn.configure(activebackground="Light green")
    Customize_btn.configure(activebackground="Light green")
    edge_btn.configure(activebackground="Light green")
    tkcopen_btn.configure(activebackground="Light green") 

def green_text_active():
    launch_text_editor_btn.configure(activeforeground="Dark green")
    #exit_btn.configure(activeforeground="Dark green")
    applist_btn.configure(activeforeground="Dark green")
    note_btn.configure(activeforeground="Dark green") 
    launch_text_editor_btn.configure(activeforeground="Dark green")
    Customize_btn.configure(activeforeground="Dark green")
    edge_btn.configure(activeforeground="Dark green")
    tkcopen_btn.configure(activeforeground="Dark green") 

def black_text_active():
    launch_text_editor_btn.configure(activeforeground="Black")
    #exit_btn.configure(activeforeground="Black")
    applist_btn.configure(activeforeground="Black")
    note_btn.configure(activeforeground="Black")
    launch_text_editor_btn.configure(activeforeground="Black")
    Customize_btn.configure(activeforeground="Black")
    edge_btn.configure(activeforeground="Black")
    tkcopen_btn.configure(activeforeground="Black") 

def blue_text_active():
    launch_text_editor_btn.configure(activeforeground="Dark blue")
    #exit_btn.configure(activeforeground="Dark blue")
    applist_btn.configure(activeforeground="Dark blue")
    note_btn.configure(activeforeground="Dark blue")
    launch_text_editor_btn.configure(activeforeground="Dark blue")
    Customize_btn.configure(activeforeground="Dark blue")
    edge_btn.configure(activeforeground="Dark blue")
    tkcopen_btn.configure(activeforeground="Dark blue") 

def purple_text_active():
    launch_text_editor_btn.configure(activeforeground="Purple")
    #exit_btn.configure(activeforeground="Purple")
    applist_btn.configure(activeforeground="Purple")
    note_btn.configure(activeforeground="Purple")
    launch_text_editor_btn.configure(activeforeground="Purple")
    Customize_btn.configure(activeforeground="Purple")
    edge_btn.configure(activeforeground="Purple")
    tkcopen_btn.configure(activeforeground="Purple") 

def orange_text_active():
    launch_text_editor_btn.configure(activeforeground="#c4981d")
    #exit_btn.configure(activeforeground="#c4981d")
    applist_btn.configure(activeforeground="#c4981d")
    note_btn.configure(activeforeground="#c4981d")
    launch_text_editor_btn.configure(activeforeground="#c4981d")
    Customize_btn.configure(activeforeground="#c4981d")
    edge_btn.configure(activeforeground="#c4981d")
    tkcopen_btn.configure(activeforeground="#c4981d") 

def black_text_active():
    launch_text_editor_btn.configure(activeforeground="Black")
    #exit_btn.configure(activeforeground="Black")
    applist_btn.configure(activeforeground="Black")
    note_btn.configure(activeforeground="Black")
    launch_text_editor_btn.configure(activeforeground="Black")
    Customize_btn.configure(activeforeground="Black")
    tkcopen_btn.configure(activeforeground='Black') 
    edge_btn.configure(activeforeground="Black")

def pink_text_active():
    launch_text_editor_btn.configure(activeforeground="pink")
    #exit_btn.configure(activeforeground="Pink")
    applist_btn.configure(activeforeground="Pink")
    note_btn.configure(activeforeground="pink")
    launch_text_editor_btn.configure(activeforeground="Pink")
    Customize_btn.configure(activeforeground="Pink")
    tkcopen_btn.configure(activeforeground='Pink') 
    edge_btn.configure(activeforeground="Pink")

def green_text():
    launch_text_editor_btn.configure(fg="Dark green")
    exit_btn.configure(fg="Dark green")
    applist_btn.configure(fg="Dark green")
    note_btn.configure(fg="Dark green") 
    launch_text_editor_btn.configure(fg="Dark green")
    Customize_btn.configure(fg="Dark green")
    edge_btn.configure(fg="Dark green")
    tkcopen_btn.configure(fg="Dark green") 

def blue_text():
    launch_text_editor_btn.configure(fg="Dark blue")
    exit_btn.configure(fg="Dark blue")
    applist_btn.configure(fg="Dark blue")
    note_btn.configure(fg="Dark blue")
    launch_text_editor_btn.configure(fg="Dark blue")
    Customize_btn.configure(fg="Dark blue")
    edge_btn.configure(fg="Dark blue")
    tkcopen_btn.configure(fg="Dark blue") 

def purple_text():
    launch_text_editor_btn.configure(fg="Purple")
    exit_btn.configure(fg="Purple")
    applist_btn.configure(fg="Purple")
    note_btn.configure(fg="Purple")
    launch_text_editor_btn.configure(fg="Purple")
    Customize_btn.configure(fg="Purple")
    edge_btn.configure(fg="Purple")
    tkcopen_btn.configure(fg="Purple") 

def orange_text():
    launch_text_editor_btn.configure(fg="#c4981d")
    exit_btn.configure(fg="#c4981d")
    applist_btn.configure(fg="#c4981d")
    note_btn.configure(fg="#c4981d")
    launch_text_editor_btn.configure(fg="#c4981d")
    Customize_btn.configure(fg="#c4981d")
    edge_btn.configure(fg="#c4981d")
    tkcopen_btn.configure(fg="#c4981d") 

def black_text():
    launch_text_editor_btn.configure(fg="Black")
    exit_btn.configure(fg="Black")
    applist_btn.configure(fg="Black")
    note_btn.configure(fg="Black")
    launch_text_editor_btn.configure(fg="Black")
    Customize_btn.configure(fg="Black")
    tkcopen_btn.configure(fg='Black') 
    edge_btn.configure(fg="Black")

def pink_text():
    launch_text_editor_btn.configure(fg="pink")
    exit_btn.configure(fg="Pink")
    applist_btn.configure(fg="Pink")
    note_btn.configure(fg="Pink")
    launch_text_editor_btn.configure(fg="Pink")
    Customize_btn.configure(fg="Pink")
    tkcopen_btn.configure(fg='Pink') 
    edge_btn.configure(fg="Pink")

def date_black():
    day_label.configure(fg='Black')

def date_orange():
    day_label.configure(fg="#c4981d")

def date_green():
    day_label.configure(fg="Dark green")

def date_blue():
    day_label.configure(fg="Dark Blue")

def date_yellow():
    day_label.configure(fg="Yellow")

def date_pink():
    day_label.configure(fg="Pink")

def date_purple():
    day_label.configure(fg="Purple")

def orangeBG():
    random.configure(bg="#fed8b1")
    root.configure(bg="#fed8b1")
    clock_label.configure(bg="#fed8b1")
    day_label.configure(bg="#fed8b1")
    bottom_lbl.configure(bg="#fed8b1")
    #add menu MENU
    thanxuey.configure(bg="#fed8b1")
    kawamath.configure(bg="#fed8b1")
    xux_label.configure(bg="#fed8b1")
    xaq_label.configure(bg="#fed8b1")
    the_frame.configure(bg='#fed8b1')
    app_frame.configure(bg='#fed8b1')
    random_label.configure(bg='#fed8b1')

def purpleBG():
    random.configure(bg="#e2d5e8")
    root.configure(bg="#e2d5e8")
    clock_label.configure(bg="#e2d5e8")
    day_label.configure(bg="#e2d5e8")
    bottom_lbl.configure(bg="#e2d5e8")    
    #add menu MENU
    thanxuey.configure(bg="#e2d5e8")
    kawamath.configure(bg="#e2d5e8")
    xux_label.configure(bg="#e2d5e8")
    xaq_label.configure(bg="#e2d5e8")
    the_frame.configure(bg='#e2d5e8')
    app_frame.configure(bg='#e2d5e8')
    random_label.configure(bg='#e2d5e8')

def greenBG():
    random.configure(bg="Light green")
    root.configure(bg="Light green")
    clock_label.configure(bg="Light green")
    day_label.configure(bg="Light green")
    bottom_lbl.configure(bg="Light green")
    #add menu MENU
    thanxuey.configure(bg="Lightgreen")
    kawamath.configure(bg="Lightgreen")
    xux_label.configure(bg="Lightgreen")
    xaq_label.configure(bg="Lightgreen")
    the_frame.configure(bg='Lightgreen')
    app_frame.configure(bg='Lightgreen')
    random_label.configure(bg='Lightgreen')

def pinkBG():
    random.configure(bg="Light pink")
    root.configure(bg="Light pink")
    clock_label.configure(bg="Light pink")
    day_label.configure(bg="Light pink")
    bottom_lbl.configure(bg="Light pink")
    #add menu MENU
    thanxuey.configure(bg="Lightpink")
    kawamath.configure(bg="Lightpink")
    xux_label.configure(bg="Lightpink")
    xaq_label.configure(bg="Lightpink")
    the_frame.configure(bg='Lightpink')
    app_frame.configure(bg='Lightpink')
    random_label.configure(bg='Lightpink')

def blueBG():
    random.configure(bg="Light blue")
    root.configure(bg="Light blue")
    clock_label.configure(bg="Light blue")
    day_label.configure(bg="Light blue")
    bottom_lbl.configure(bg="Light blue")
    #add menu MENU
    thanxuey.configure(bg="Lightblue")
    kawamath.configure(bg="Lightblue")
    xux_label.configure(bg="Lightblue")
    xaq_label.configure(bg="Lightblue")
    the_frame.configure(bg='Lightblue')
    app_frame.configure(bg='Lightblue')
    random_label.configure(bg='Lightblue')

def yellowBG():
    random.configure(bg="Light yellow")
    root.configure(bg="Light yellow")
    clock_label.configure(bg="Light yellow")
    day_label.configure(bg="Light yellow")
    bottom_lbl.configure(bg="Light yellow")
    #add menu MENU
    thanxuey.configure(bg="Lightyellow")
    kawamath.configure(bg="Lightyellow")
    xux_label.configure(bg="Lightyellow")
    xaq_label.configure(bg="Lightyellow")
    the_frame.configure(bg='Lightyellow')
    app_frame.configure(bg='Lightyellow')
    random_label.configure(bg='Lightyellow')


def orangeFG():
    clock_label.configure(fg="#c4981d")
    print("NOTIFICATION: clock text color has changed")

def purpleFG():
    clock_label.configure(fg="Purple")
    print("NOTIFICATION: clock text color has changed")

def greenFG():
    clock_label.configure(fg="Dark green")
    print("NOTIFICATION: clock text color has changed")

def blueFG():
    clock_label.configure(fg="Dark blue")
    print("NOTIFICATION: clock text color has changed")

def yellowFG():
    clock_label.configure(fg="Yellow")
    print("NOTIFICATION: clock text color has changed")

def pinkFG():
    clock_label.configure(fg="Pink")
    print("NOTIFICATION: clock text color has changed")

def blackFG():
    clock_label.configure(fg="Black")
    print("NOTIFICATION: clock text color has changed")

#def section in section (customize workspace and colors) #taskbar options
def center_taskbar_command():
    bottom_lbl.pack_forget()
    messagebox.showwarning("Warning","You have to hide the taskbar before centering the taskbar")
    taskbar.pack(side=BOTTOM)
    bottom_lbl.pack(side=BOTTOM)

def show_taskbar_command():
    bottom_lbl.pack_forget()
    taskbar.pack(side=BOTTOM, fill=X)
    bottom_lbl.pack(side=BOTTOM)

def hide_taskbar_command():
    taskbar.pack_forget()

def greencolor():
    launch_text_editor_btn.configure(bg="Light green")
    exit_btn.configure(bg="Light green")
    applist_btn.configure(bg="Light green")
    note_btn.configure(bg="Light green")
    launch_text_editor_btn.configure(bg="Light green")
    Customize_btn.configure(bg="Light green")
    edge_btn.configure(bg="Light green")
    tkcopen_btn.configure(bg="Lightgreen")
    taskbar.configure(bg='Lightgreen')
    print("NOTIFICATION: Taskbar color has changed")

def purplecolor():
    launch_text_editor_btn.configure(bg="#e2d5e8")
    exit_btn.configure(bg="#e2d5e8")
    applist_btn.configure(bg="#e2d5e8")
    note_btn.configure(bg="#e2d5e8")
    launch_text_editor_btn.configure(bg="#e2d5e8")
    Customize_btn.configure(bg="#e2d5e8")
    tkcopen_btn.configure(bg="#e2d5e8")
    edge_btn.configure(bg="#e2d5e8")
    taskbar.configure(bg='#e2d5e8')
    print("NOTIFICATION: Taskbar color has changed")

def bluecolor():
    launch_text_editor_btn.configure(bg="Light blue")
    exit_btn.configure(bg="Light blue")
    applist_btn.configure(bg="Light blue")
    note_btn.configure(bg="Light blue")
    launch_text_editor_btn.configure(bg="Light blue")
    Customize_btn.configure(bg="Light blue")
    tkcopen_btn.configure(bg="Light blue")
    edge_btn.configure(bg="Light blue")
    taskbar.configure(bg="Light blue")
    clock_label.configure(fg="Dark green")
    print("NOTIFICATION: Taskbar color has changed")

def yellowcolor():
    launch_text_editor_btn.configure(bg="Light yellow")
    exit_btn.configure(bg="Light yellow")
    applist_btn.configure(bg="Light yellow")
    note_btn.configure(bg="Light yellow")
    launch_text_editor_btn.configure(bg="Light yellow")
    Customize_btn.configure(bg="Light yellow")
    tkcopen_btn.configure(bg="Light yellow")
    edge_btn.configure(bg="Light yellow")
    taskbar.configure(bg='Light yellow')
    print("NOTIFICATION: Taskbar color has changed")

def pinkcolor():
    launch_text_editor_btn.configure(bg="Light pink")
    exit_btn.configure(bg="Light pink")
    applist_btn.configure(bg="Light pink")       
    note_btn.configure(bg="Light pink")
    launch_text_editor_btn.configure(bg="Light pink")
    Customize_btn.configure(bg="Light pink")
    tkcopen_btn.configure(bg="Lightpink")
    edge_btn.configure(bg="Light pink")
    taskbar.configure(bg='Light pink')
    print("NOTIFICATION: Taskbar color has changed")

def orangecolor():
    launch_text_editor_btn.configure(bg="#fed8b1")
    exit_btn.configure(bg="#fed8b1")
    #.configure(bg="#fed8b1")
    note_btn.configure(bg="#fed8b1")
    launch_text_editor_btn.configure(bg="#fed8b1")
    Customize_btn.configure(bg="#fed8b1")
    tkcopen_btn.configure(bg="#fed8b1")
    edge_btn.configure(bg="#fed8b1")
    taskbar.configure(bg='#fed8b1')
    print("NOTIFICATION: Taskbar color has changed")

def greycolor():
    launch_text_editor_btn.configure(bg="Light grey")
    exit_btn.configure(bg="Light grey")
    #.configure(bg="Light grey")
    note_btn.configure(bg="Light grey")
    launch_text_editor_btn.configure(bg="Light grey")
    tkcopen_btn.configure(bg="Lightgrey")
    Customize_btn.configure(bg="Light grey")
    edge_btn.configure(bg="Light grey")
    taskbar.configure(bg='Light grey')
    print("NOTIFICATION: Taskbar color has changed")

#def section -modes

header_font = ('Comfortaa', 21)
grey = 'Lightgrey'
size = ('500x400')
the_font = ('Comfortaa', 16)

def Settings_workspace():
    root.geometry("1325x600")
    bottom_lbl.configure(text='Customize workspace homescreen - Workspace UI X2')

    the_menu = Menu(root)
    root.config(menu=the_menu)

    #background color
    setting_menu = Menu(the_menu, tearoff=False)
    the_menu.add_cascade(label="Background color", menu=setting_menu)
    setting_menu.add_command(label="Light green", command=greenBG)
    setting_menu.add_command(label="Light blue", command=blueBG)
    #setting_menu.add_command(label="Light yellow", command=yellowBG)
    setting_menu.add_command(label="Light pink", command=pinkBG)
    setting_menu.add_command(label="Light purple", command=purpleBG)
    setting_menu.add_command(label="Light orange", command=orangeBG)

    #clock label color
    clock_label_color = Menu(the_menu, tearoff=False)
    the_menu.add_cascade(label="Clock text color", menu=clock_label_color)
    clock_label_color.add_command(label="Dark green", command=greenFG)
    clock_label_color.add_command(label="Dark blue", command=blueFG)
    #clock_label_color.add_command(label="Light yellow", command=yellowFG)
    clock_label_color.add_command(label="Light pink", command=pinkFG)
    clock_label_color.add_command(label="Dark purple", command=purpleFG)
    clock_label_color.add_command(label="Brown", command=orangeFG)
    clock_label_color.add_command(label="Black", command=blackFG)

    #taskbar
    taskbar_menu = Menu(the_menu, tearoff=False)
    the_menu.add_cascade(label="Taskbar options", menu=taskbar_menu)
    taskbar_menu.add_command(label="Light green", command=greencolor)
    taskbar_menu.add_command(label="Light blue", command=bluecolor)
    taskbar_menu.add_command(label="Light grey", command=greycolor)
    taskbar_menu.add_command(label="Light purple", command=purplecolor)
    taskbar_menu.add_command(label="Light orange", command=orangecolor)
    taskbar_menu.add_command(label="Pink", command=pinkcolor)
    taskbar_menu.add_separator()
    taskbar_menu.add_command(label="Hide taskbar", command=hide_taskbar_command)
    taskbar_menu.add_command(label="Show taskbar", command=show_taskbar_command)
    taskbar_menu.add_command(label="Center taskbar", command=center_taskbar_command)

    #tdate_menu
    date_menu = Menu(the_menu, tearoff=False)
    the_menu.add_cascade(label="Date and day text color", menu=date_menu)
    date_menu.add_command(label="Dark green", command=date_green)
    date_menu.add_command(label="Dark blue", command=date_blue)
    date_menu.add_command(label="Dark purple", command=date_purple)
    date_menu.add_command(label="Brown", command=date_orange)
    date_menu.add_command(label="Black", command=date_black)
    date_menu.add_command(label="Pink", command=date_pink)

    #tdate_menu
    SEARCH_MENU_CUS = Menu(the_menu, tearoff=False)
    the_menu.add_cascade(label="Button text color", menu=SEARCH_MENU_CUS)
    SEARCH_MENU_CUS.add_command(label="Dark green", command=green_text)
    SEARCH_MENU_CUS.add_command(label="Dark blue", command=blue_text)
    SEARCH_MENU_CUS.add_command(label="Dark purple", command=purple_text)
    SEARCH_MENU_CUS.add_command(label="Brown", command=orange_text)
    SEARCH_MENU_CUS.add_command(label="Black", command=black_text)
    SEARCH_MENU_CUS.add_command(label="Pink", command=pink_text)

    #tdate_menu
    ABC_menu = Menu(the_menu, tearoff=False)
    the_menu.add_cascade(label="Active button text color", menu=ABC_menu)
    ABC_menu.add_command(label="Dark green", command=green_text_active)
    ABC_menu.add_command(label="Dark blue", command=blue_text_active)
    ABC_menu.add_command(label="Dark purple", command=purple_text_active)
    ABC_menu.add_command(label="Brown", command=orange_text_active)
    ABC_menu.add_command(label="Black", command=black_text_active)
    ABC_menu.add_command(label="Pink", command=pink_text_active)

    #tdate_menu
    menu_menu = Menu(the_menu, tearoff=False)
    the_menu.add_cascade(label="Active button background color", menu=menu_menu)
    menu_menu.add_command(label="Light green", command=green_text_active_bg)
    menu_menu.add_command(label="Light blue", command=blue_text_active_bg)
    menu_menu.add_command(label="Light purple", command=purple_text_active_bg)
    menu_menu.add_command(label="light orange", command=orange_text_active_bg)
    menu_menu.add_command(label="Light grey", command=grey_text_active_bg)
    menu_menu.add_command(label="Pink", command=pink_text_active_bg)

    #lakure menu
    lakure_menu = Menu(the_menu, tearoff=False)
    the_menu.add_cascade(label="Exit modes", menu=lakure_menu)
    lakure_menu.add_command(label="Exit customize workspace mode", command=commandrandom)

    #break ----
    Customize_btn.configure(text='Normal mode', command=commandrandom)

    root.title("Workspace for windows - Workspace UI X2 - Customize workspace")

#break -- add functions for notes mode
def deleterONE():
    textONE.delete(1.0, END)
    textONE.insert(1.0, 'Type a note..')

def deleterTWO():
    textTAW.delete(1.0, END)
    textTAW.insert(1.0, 'Type a note..')

def deleterTHREY():
    taxtey.delete(1.0, END)
    taxtey.insert(1.0, 'Type a note..')

def deletare():
    tanultexta.delete(1.0, END)
    tanultexta.insert(1.0, 'Type a note..')

def saveAS_command_seven():
    text_file = filedialog.asksaveasfilename(filetypes=(("Text Files", "*txt"), ("Documents Files", "*.docx"), ("Python Files", "*.py"), ("All Files", "*.*")))
    text_file = open(text_file, 'w')
    text_file.write(tanultexta.get(1.0, END))

def open_file_seven():
    tanultexta.delete("1.0", END)
    text_file = filedialog.askopenfilename(title="Open file", filetypes=(("Text Files", "*txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
    text_file = open(text_file, 'r')
    stuff = text_file.read()
    tanultexta.insert(END, stuff)
    text_file.close()

def saveAS_command_five():
    text_file = filedialog.asksaveasfilename(filetypes=(("Text Files", "*txt"), ("Documents Files", "*.docx"), ("Python Files", "*.py"), ("All Files", "*.*")))
    text_file = open(text_file, 'w')
    text_file.write(taxtey.get(1.0, END))

def open_file_five():
    taxtey.delete("1.0", END)
    text_file = filedialog.askopenfilename(title="Open file", filetypes=(("Text Files", "*txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
    text_file = open(text_file, 'r')
    stuff = text_file.read()
    taxtey.insert(END, stuff)
    text_file.close()

def saveAS_command_three():
    text_file = filedialog.asksaveasfilename(filetypes=(("Text Files", "*txt"), ("Documents Files", "*.docx"), ("Python Files", "*.py"), ("All Files", "*.*")))
    text_file = open(text_file, 'w')
    text_file.write(textTAW.get(1.0, END))

def open_file_three():
    textTAW.delete("1.0", END)
    text_file = filedialog.askopenfilename(title="Open file", filetypes=(("Text Files", "*txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
    text_file = open(text_file, 'r')
    stuff = text_file.read()
    textTAW.insert(END, stuff)
    text_file.close()

def saveAS_command_van():
    text_file = filedialog.asksaveasfilename(filetypes=(("Text Files", "*txt"), ("Documents Files", "*.docx"), ("Python Files", "*.py"), ("All Files", "*.*")))
    text_file = open(text_file, 'w')
    text_file.write(textONE.get(1.0, END))

def open_file_van():
    textONE.delete("1.0", END)
    text_file = filedialog.askopenfilename(title="Open file", filetypes=(("Text Files", "*txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
    text_file = open(text_file, 'r')
    stuff = text_file.read()
    textONE.insert(END, stuff)
    text_file.close()

#break -- BREAK
the_frame = Frame(root, bg='Lightgreen')
thanxuey = Label(the_frame, text='            ', bg='Lightgreen')
kawamath = Label(the_frame, text='            ', bg='Lightgreen')
xaq_label = Label(the_frame, text='            ', bg='Lightgreen')
xux_label = Label(the_frame, text='            ', bg='Lightgreen')

def notes_mode_command():
    random.pack_forget()
    root.geometry("1325x630")
    #some configuration
    root.title("Workspace for windows - Workspace UI 2X - Notes mode")

    Customize_btn.configure(text=' Customize mode ', command=Settings_workspace)
    note_btn.configure(text='Normal mode', command=commandrandom)
    app_frame.pack_forget()
    random_label.pack_forget()

    #hiding or clearning the screen
    day_label.pack_forget()
    clock_label.pack_forget()

    #menu
    new_menu = Menu(root)
    root.configure(menu=new_menu)

    #making a top notes heading label
    random.configure(text='Notes - Workspace UI X2', font=('Comfortaa', 23))
    random.pack(side=TOP, fill=X)
    #making a frame
    global the_frame
    the_frame.pack(fill=X)

    #adding notepads (text boxes) and globak
    #Learn about these ODD text boxes, textONE, textTAW, taxtey and tanultexa, these are all good behaving text boxes
    global textONE, textTAW, taxtey, tanultexta

    xaq_label.grid(row=0, column=0)

    textONE = Text(the_frame, width=25, height=15, font=("Calbari", 14), selectbackground="Lightgrey", selectforeground="Black", undo=True, bg='#e4f0e7', borderwidth=0)
    textONE.grid(row=1, column=1)

    xux_label.grid(row=1, column=2)

    textTAW = Text(the_frame, width=25, height=15, font=("Calbari", 14), selectbackground="Lightgrey", selectforeground="Black", undo=True, bg='#e4f0e7', borderwidth=0)
    textTAW.grid(row=1, column=3)

    kawamath.grid(row=1, column=4)

    taxtey = Text(the_frame, width=25, height=15, font=("Calbari", 14), selectbackground="Lightgrey", selectforeground="Black", undo=True, bg='#e4f0e7', borderwidth=0)
    taxtey.grid(row=1, column=5)

    thanxuey.grid(row=1, column=6)

    tanultexta = Text(the_frame, width=25, height=15, font=("Calbari", 14), selectbackground="Lightgrey", selectforeground="Black", undo=True, bg='#e4f0e7', borderwidth=0)
    tanultexta.grid(row=1, column=7)

    #insert text 
    textONE.insert(1.0, 'Type a note..')
    textTAW.insert(1.0, 'Type a note..')
    taxtey.insert(1.0, 'Type a note..')
    tanultexta.insert(1.0, 'Type a note..')

    #clear
    clicker_abb = Button(the_frame, text='Clear text', bg="Lightgrey" ,font=("Comfortaa", "17"), borderwidth=0 ,activebackground="Lightgrey",activeforeground="Darkgreen" ,width=21 ,command=deleterONE)
    clicker_abb.grid(row=3, column=1)

    cowmilk = Button(the_frame, text='Clear text', bg="Lightgrey" ,font=("Comfortaa", "17"), borderwidth=0 ,activebackground="Lightgrey",activeforeground="Darkgreen" ,width=21 ,command=deleterTWO)
    cowmilk.grid(row=3, column=3)

    gerikiru = Button(the_frame, text='Clear text', bg="Lightgrey" ,font=("Comfortaa", "17"), borderwidth=0 ,activebackground="Lightgrey",activeforeground="Darkgreen" ,width=21 ,command=deleterTHREY)
    gerikiru.grid(row=3, column=5)

    kanzukahama = Button(the_frame, text=" Clear text ", bg="Lightgrey" ,font=("Comfortaa", "17"), borderwidth=0 ,activebackground="Lightgrey",activeforeground="Darkgreen" ,width=21 ,command=deletare)
    kanzukahama.grid(row=3, column=7)

    #save as
    ismaIL = Button(the_frame, text=" Save AS ", bg="Lightgrey" ,font=("Comfortaa", "17"), borderwidth=0 ,activebackground="Lightgrey",activeforeground="Darkgreen" ,width=21 ,command=saveAS_command_seven)
    ismaIL.grid(row=4, column=7)

    somekan = Button(the_frame, text=" Save AS ", bg="Lightgrey" ,font=("Comfortaa", "17"), borderwidth=0 ,activebackground="Lightgrey",activeforeground="Darkgreen" ,width=21 ,command=saveAS_command_five)
    somekan.grid(row=4, column=5)

    uknet = Button(the_frame, text=" Save AS ", bg="Lightgrey" ,font=("Comfortaa", "17"), borderwidth=0 ,activebackground="Lightgrey",activeforeground="Darkgreen" ,width=21 ,command=saveAS_command_three)
    uknet.grid(row=4, column=3)

    someunkn = Button(the_frame, text=" Save AS ", bg="Lightgrey" ,font=("Comfortaa", "17"), borderwidth=0 ,activebackground="Lightgrey",activeforeground="Darkgreen" ,width=21 ,command=saveAS_command_van)
    someunkn.grid(row=4, column=1)

    #open
    sandiypoorey = Button(the_frame, text=" Open notes ", bg="Lightgrey" ,font=("Comfortaa", "17"), borderwidth=0 ,activebackground="Lightgrey",activeforeground="Darkgreen" ,width=21 ,command=open_file_seven)
    sandiypoorey.grid(row=5, column=7)

    samwaat = Button(the_frame, text=" Open notes ", bg="Lightgrey" ,font=("Comfortaa", "17"), borderwidth=0 ,activebackground="Lightgrey",activeforeground="Darkgreen" ,width=21 ,command=open_file_five)
    samwaat.grid(row=5, column=5)

    borr = Button(the_frame, text=" Open notes ", bg="Lightgrey" ,font=("Comfortaa", "17"), borderwidth=0 ,activebackground="Lightgrey",activeforeground="Darkgreen" ,width=21 ,command=open_file_three)
    borr.grid(row=5, column=3)

    kasaniku = Button(the_frame, text=" Open notes ", bg="Lightgrey" ,font=("Comfortaa", "17"), borderwidth=0 ,activebackground="Lightgrey",activeforeground="Darkgreen" ,width=21 ,command=open_file_van)
    kasaniku.grid(row=5, column=1)

    #editing the taskbar
    ##.grid_forget()

    #editing or configuring
    bottom_lbl.config(font=("Comfortaa", "16"))
    bottom_lbl.config(text='Notes mode - Workspace UI X2  - '+hms)

    bottom_lbl.after(500, clockifycommand)

#def -- BREAKLINE
app_frame = Frame(root, bg='Lightgreen')
random_label = Label(root, text='Application list', font=('Comfortaa', 27), bg='Lightgreen')

username = 'izkaan DEVELOPER'
job_name = 'izkaan and dad python productions'

def end_session_command_msg():
    data_end = str( username+ '' + ' has ended a session on '+ time.strftime("%a") + ' '+ time.strftime('%X') + ' for ' + job_name + ' company')
    print("Workspace UI session update")
    print("Brand new session ended now!")
    print(data_end)
    messagebox.showinfo("Sessions" ,data_end)

def Start_session_command_msg():
    data_start = str( username+ '' + ' has started a new session on '+ time.strftime("%a") + ' '+ time.strftime('%X') + ' for ' + job_name+ ' company')
    print("Workspace UI session update")
    print("Brand new session started now!")
    print(data_start)
    messagebox.showinfo("Sessions" ,data_start)

def AppList_ShowCommand():
    #clear the screen and edit the title
    random.pack_forget()
    clock_label.pack_forget()
    day_label.pack_forget()
    bottom_lbl.configure(text='App list - Workspace UI X2')
    the_frame.pack_forget()

    #configure
    applist_btn.configure(text='Normal mode', command=commandrandom)
    root.title('Workspace for windows - Workspace UI X2 - App list')
    random_label.pack(side=TOP, pady=5)

    #frame
    app_frame.pack(side=TOP, fill=X)

    b1 = Button(app_frame, text=" Sublime text editor ", bg="Lightgrey" ,font=("Comfortaa", "17"), borderwidth=0 ,activebackground="Lightgrey",activeforeground="Darkgreen", width=20,command=launch_sublime_text_command)
    b1.grid(row=0, column=0, padx=5)

    b2 = Button(app_frame, text=" Basic text for windows ", bg="Lightgrey" ,font=("Comfortaa", "17"), borderwidth=0 ,activebackground="Lightgrey",activeforeground="Darkgreen", width=20,command=launch_text_editor_command)
    b2.grid(row=0, column=1, padx=5)

    b3 = Button(app_frame, text=" Basic text editor 3.0 ", bg="Lightgrey" ,font=("Comfortaa", "17"), borderwidth=0 ,activebackground="Lightgrey",activeforeground="Darkgreen", width=20,command=launch_basictext30_command)
    b3.grid(row=0, column=2, padx=5)

    b4 = Button(app_frame, text=" Basic text editor 2.0 ", bg="Lightgrey" ,font=("Comfortaa", "17"), borderwidth=0 ,activebackground="Lightgrey",activeforeground="Darkgreen", width=20,command=launch_basictext20_command)
    b4.grid(row=0, column=3, padx=5)

    b8 = Button(app_frame, text=" Tic Tac Toe ", bg="Lightgrey" ,font=("Comfortaa", "17"), borderwidth=0 ,activebackground="Lightgrey",activeforeground="Darkgreen", width=15,command=Laungceytictactoey)
    b8.grid(row=0, column=4, padx=5)

    b5 = Button(app_frame, text=" Basic text editor 1.0 ", bg="Lightgrey" ,font=("Comfortaa", "17"), borderwidth=0 ,activebackground="Lightgrey",activeforeground="Darkgreen", width=20,command=launch_basictext5_command)
    b5.grid(row=1, column=0, padx=5, pady=5)

    b6 = Button(app_frame, text=" Simple payment app ", bg="Lightgrey" ,font=("Comfortaa", "17"), borderwidth=0 ,activebackground="Lightgrey",activeforeground="Darkgreen", width=20,command=launch_simple_payments_app)
    b6.grid(row=1, column=1, padx=5, pady=5)

    b7 = Button(app_frame, text=" Simple payment XA ", bg="Lightgrey" ,font=("Comfortaa", "17"), borderwidth=0 ,activebackground="Lightgrey",activeforeground="Darkgreen", width=20,command=launch_simple_payments_XA)
    b7.grid(row=1, column=2, padx=5, pady=5)

    b9= Button(app_frame, text=" Microsoft edge ", bg="Lightgrey" ,font=("Comfortaa", "17"), borderwidth=0 ,activebackground="Lightgrey",activeforeground="Darkgreen", width=20,command=launch_edge_browser_command)
    b9.grid(row=1, column=3, padx=5, pady=5)

    B10= Button(app_frame, text=" Google chrome ", bg="Lightgrey" ,font=("Comfortaa", "17"), borderwidth=0 ,activebackground="Lightgrey",activeforeground="Darkgreen", width=15,command=launch_chrome_browser_command)
    b10.grid(row=1, column=4, padx=5, pady=5)

    b11= Button(app_frame, text=" Flashback player ", bg="Lightgrey" ,font=("Comfortaa", "17"), borderwidth=0 ,activebackground="Lightgrey",activeforeground="Darkgreen", width=20,command=launch_fbp_command)
    b11.grid(row=2, column=0, padx=5, pady=5)

    b12= Button(app_frame, text=" Flashback recorder ", bg="Lightgrey" ,font=("Comfortaa", "17"), borderwidth=0 ,activebackground="Lightgrey",activeforeground="Darkgreen", width=20,command=launch_fbr_command)
    b12.grid(row=2, column=1, padx=5, pady=5)

#taskabr
#making a taskbar (smaller than before!)
taskbar = Frame(root)
taskbar.pack(fill=X, side=BOTTOM)
taskbar.configure(bg="Lightgrey")

#LABELS
random = Label(root, text="", bg="Lightgreen")
random.pack(fill=X)

clock_label = Label(root, text="Activating clock", bg="Lightgreen", font=("Comfortaa", "65"))
clock_label.pack(pady=5, side=TOP)

day_label = Label(root, text="Finding date and day", font=("Comfortaa", "37"), bg="Lightgreen")
day_label.pack(side=TOP)

day_label.after(500, date)
clock_label.after(500, clock)

#making a taskbar (smaller than before!)
taskbar = Frame(root)
taskbar.pack(fill=X, side=BOTTOM)
taskbar.configure(bg="Lightgrey")

search = Button(taskbar, bg="#e4f0e7" ,text=" Search files ", font=("Comfortaa", "17"), borderwidth=0 ,activebackground="#e4f0e7",activeforeground="Darkblue" ,command=search_file)
search.grid(row=0, column=0)

applist_btn = Button(taskbar, bg="#e4f0e7" ,text=" Application list ", font=("Comfortaa", "17"), borderwidth=0 ,activebackground="#e4f0e7",activeforeground="Darkblue" ,command=AppList_ShowCommand)
applist_btn.grid(row=0, column=1)

launch_text_editor_btn = Button(taskbar, text=" Text editor ", bg="Lightgrey" ,font=("Comfortaa", "17"), borderwidth=0 ,activebackground="Lightgrey",activeforeground="Darkgreen" ,command=launch_text_editor_command)
launch_text_editor_btn.grid(row=0, column=2)

tkcopen_btn = Button(taskbar, text=" Tic tac toe ", bg="Lightgrey" ,font=("Comfortaa", "17"), borderwidth=0 ,activebackground="Lightgrey",activeforeground="Darkgreen" ,command=Laungceytictactoey)
tkcopen_btn.grid(row=0, column=3)

edge_btn = Button(taskbar, text=" Microsoft edge ", bg="Lightgrey" ,font=("Comfortaa", "17"), borderwidth=0 ,activebackground="Lightgrey",activeforeground="Darkgreen" ,command=launch_edge_browser_command)
edge_btn.grid(row=0, column=4)

note_btn = Button(taskbar, text='Notes mode', bg="Lightgrey" ,font=("Comfortaa", "17"), borderwidth=0 ,activebackground="Lightgrey",activeforeground="Darkgreen" ,command=notes_mode_command)
note_btn.grid(row=0, column=6)

Customize_btn = Button(taskbar, text=" Customize mode ", bg="Lightgrey" ,font=("Comfortaa", "17"), borderwidth=0 ,activebackground="Lightgrey",activeforeground="Darkgreen",command=Settings_workspace)
Customize_btn.grid(row=0, column=7)

exit_btn = Button(taskbar, text=" Exit workspace ", bg="Lightgrey" ,font=("Comfortaa", "17"), borderwidth=0 ,activebackground="Lightgrey",activeforeground="Darkred" ,command=exit_command)
exit_btn.grid(row=0, column=8)

#-- Labels
bottom_lbl = Label(root, text="Homescreen - Workspace UI X2", font=("Comfortaa", "14"), bg="Lightgreen")
bottom_lbl.pack(side=BOTTOM)

#making a calander
style = ttk.Style(root)
style.theme_use('clam') 
Cal = Calendar(root, background="Light green", disabledbackground="Light green", bordercolor="Light green", 
               headersbackground="Light green", normalbackground="Light green", foreground='Black', 
               normalforeground='Black', headersforeground='Black')
Cal.config(background = "Light green")

def commandrandom():
    #configure text
    Customize_btn.configure(text=" Customize mode ", command=Settings_workspace)
    note_btn.configure(text=" Notes mode ", command=notes_mode_command)
    root.title("Workspace for windows - Workspace UI X2")
    Homescreen = bottom_lbl.configure(text="Homescreen - Workspace UI X2")
    bottom_lbl.config(font=("Comfortaa", "14"))
    the_frame.pack_forget()
    random_label.pack_forget()
    app_frame.pack_forget()

    #repack
    clock_label.pack(side=TOP)
    day_label.pack(side=TOP)

    applist_btn.configure(text=" Application list ", command=AppList_ShowCommand)

    #Menubars help navigate
    global my_menu
    my_menu = Menu(root)
    root.config(menu=my_menu)
    random.configure(text=' ')
    
    #filemenu
    BE_external_M = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label=" Workspace  tools ", menu=BE_external_M)
    BE_external_M.add_command(label="Search files",command=search_file)
    BE_external_M.add_command(label="Customize workpace", command=Settings_workspace)
    #BE_external_M.add_command(label="Developer mode", command=commandrandom)
    BE_external_M.add_separator()
    BE_external_M.add_command(label="Start session", command=Start_session_command_msg)
    BE_external_M.add_command(label="End session", command=end_session_command_msg)
    BE_external_M.add_separator()
    BE_external_M.add_command(label="Notes mode", command=notes_mode_command)
    BE_external_M.add_command(label="Show Calande", command=show_calander_command)
    BE_external_M.add_command(label="Hide Calander", command=hide_calander_command)
    BE_external_M.add_command(label="Exit Workspace", command=exit_command)

    #text editors menu
    #textmenu
    text_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Text editors", menu=text_menu)
    text_menu.add_command(label="Sublime text editor", command=launch_sublime_text_command)
    text_menu.add_command(label="Basic Text For Windows", command=launch_text_editor_command)
    text_menu.add_command(label="Basic Text 3.0", command=launch_basictext30_command)
    text_menu.add_command(label="Basic Text 2.0", command=launch_basictext20_command)
    text_menu.add_command(label="Basic Text 1.0", command=launch_basictext5_command)

    #paymeny menu
    paymeny_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Simple payments", menu=paymeny_menu)
    paymeny_menu.add_command(label="Simple payment app", command=launch_simple_payments_app)
    paymeny_menu.add_command(label="Simple payment XA", command=launch_simple_payments_XA)

    #browsers
    browser_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Browsers", menu=browser_menu)
    browser_menu.add_command(label="Microsoft edge", command=launch_edge_browser_command)
    browser_menu.add_command(label="Google chrome", command=launch_chrome_browser_command)

    #flashback
    fb_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Flashback tools", menu=fb_menu)
    fb_menu.add_command(label="Flashback express recorder", command=launch_fbr_command)
    fb_menu.add_command(label="Flashback express player", command=launch_fbp_command)

    #all apps
    allapps_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="All apps", menu=allapps_menu)
    allapps_menu.add_command(label="Simple payment app", command=launch_simple_payments_app)
    allapps_menu.add_command(label="Simple payment XA", command=launch_simple_payments_XA)
    allapps_menu.add_command(label='Tic tac toe', command=Laungceytictactoey)
    allapps_menu.add_separator()
    allapps_menu.add_command(label="Sublime text editor", command=launch_sublime_text_command)
    allapps_menu.add_command(label="Basic Text For Windows", command=launch_text_editor_command)
    allapps_menu.add_command(label="Basic Text 3.0", command=launch_basictext30_command)
    allapps_menu.add_command(label="Basic Text 2.0", command=launch_basictext20_command)
    allapps_menu.add_command(label="Basic Text 1.0", command=launch_basictext5_command)
    allapps_menu.add_separator()
    allapps_menu.add_command(label="Microsoft edge", command=launch_edge_browser_command)
    allapps_menu.add_command(label="Google chrome", command=launch_chrome_browser_command)
    allapps_menu.add_separator()
    allapps_menu.add_command(label="Flashback express recorder", command=launch_fbr_command)
    allapps_menu.add_command(label="Flashback express player", command=launch_fbp_command)

    #freeze program
    freeze_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Lock workpsace", menu=freeze_menu)
    freeze_menu.add_command(label="05 sec", command=freez_5sec_command)
    freeze_menu.add_command(label="15 sec", command=freez_15sec_command)
    freeze_menu.add_command(label="30 sec", command=freez_30sec_command)
    freeze_menu.add_separator()
    freeze_menu.add_command(label="01 min", command=freez_60sec_command)
    freeze_menu.add_command(label="03 min", command=freez_3min_command)
    freeze_menu.add_command(label="05 min", command=freez_5min_command)

    #freeze program
    v_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="View options", menu=v_menu)
    v_menu.add_command(label="Fullscreen", command=enter_fullscreen_command)
    v_menu.add_command(label="Exit Fullscreen", command=exit_fullscreen_command)
    v_menu.add_separator()
    v_menu.add_command(label="Hide window title", command=hide_app_window_command)
    v_menu.add_command(label="Show window title", command=show_app_window_command)

    #intepretern
    c_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Modes", menu=c_menu)
    c_menu.add_command(label="Notes mode", command=notes_mode_command)
    c_menu.add_command(label="Customize workspace", command=Settings_workspace)

    #intepretern
    int_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Help", menu=int_menu)
    int_menu.add_command(label="Help", command=show_help_command)
    int_menu.add_command(label="About", command=show_about_command)

commandrandom() #command random is the deafult main winword

#prining some text
print("Notification center - Workspace UI X2")
hrminssec = time.strftime("%X")
print('NOTIFICATION: Workspace for windows X2 opened at ' +hrminssec)

root.mainloop()
