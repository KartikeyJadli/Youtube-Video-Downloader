# import all Tkinter libraries from the module
from tkinter import StringVar
from tkinter import * 
from tkinter import messagebox

# From the  installed Pytube module, import the youtube library
from pytube import YouTube 

Kartikey = Tk()

Kartikey.geometry('800x600') # Size of the window
Kartikey.resizable(0, 0) # makes the window adjustable with its features
Kartikey.title('Youtube Downloader')
backg = Canvas(Kartikey)
Search = Frame(backg,bg = "Grey12")
bg = PhotoImage(file=r"E:\CSE N\PYTHON\Youtube_video_downloader.png")

Label(Kartikey, text="DOWNLOAD YOUTUBE VIDEOS", font='san-serif 14 bold').pack()

link = StringVar() # Specifying the variable type

Label(Kartikey, text="Paste your link here  (ONLY YOUTUBE LINK SUPPORTED)", font='san-serif 15 bold').place(x=150, y=55)
link_enter = Entry(Kartikey, width=70, textvariable=link,font=25).place(x=100, y=120)

# try:
def free_download():
    #This captures the link(url) and locates it from YouTube.
    url = YouTube(str(link.get()))
    
    # This captures the streams available for downloaded for the video i.e. 360p, 720p, 1080p. etc.
    video = url.streams.first()
    
    # This is the method with the instruction to download the video.
    video.download() 
    
    #Once the video is downloaded, this messagebox 'DOWNLOADED' is displayed to show download completion.
    messagebox.showinfo("Message", "DOWNLOADED") 

# except:
#     messagebox.showerror("Message", "INVALID LINK !!!!!")
    
Button(Kartikey, text='Download', font='san-serif 16 bold', bg='skyblue', padx=2,command=free_download).place(x=100, y=180)

# This is used to place the background image and anchor it from the left top side of the window-pane
backg.create_image(0,0,image = bg,anchor=NW)
backg.pack(fill="both",expand = True)
backg.config(bg = "GREY12")

Kartikey.mainloop()