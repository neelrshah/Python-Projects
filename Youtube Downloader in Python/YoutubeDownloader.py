
from pytube import YouTube
from tkinter.filedialog import *
from tkinter.messagebox import *
import tkinter.font
from tkinter import *
from threading import *


font = ('verdana', 20)
file_size = 0


# Download function
def completeDownload(stream=None, file_path=None):
    showinfo("message", "File Has Been Downloaded")
    downloadBtn['text'] = "Download"
    downloadBtn['state'] = "active"
    urlField.delete(0, END)


def progressDownload(stream=None, chunk=None, bytes_remaining=None):
    percent = ((file_size - bytes_remaining) / file_size) * 100
    downloadBtn['text'] = "{:00.0f}% Downloaded".format(percent)


def startDownload(url):
    global file_size
    path_to_save = askdirectory()
    if path_to_save is None:
        return
    try:
        yt = YouTube(url)
        yt.register_on_complete_callback(completeDownload)
        yt.register_on_progress_callback(progressDownload)
        st = yt.streams.get_by_resolution('720p')
        file_size = st.filesize
        st.download(output_path=path_to_save)

    except Exception as e:
        print(e)
        showinfo("message", "Error Occured")
        downloadBtn['text'] = "Download"
        downloadBtn['state'] = "active"


def btnClick():
    try:
        downloadBtn['text'] = "Please wait..."
        downloadBtn['state'] = "disabled"
        url = urlField.get()
        if url == '':
            downloadBtn['text'] = "Download"
            downloadBtn['state'] = "active"
            return
        thread = Thread(target=startDownload, args=(url,))
        thread.start()


    except EXCEPTION as e:
        print(e)


# GUI coding
root = Tk()
root.title("YouTube Downloader")
root.iconbitmap("img/icon.ico")
root.geometry("800x700")

file = PhotoImage(file="img/youtube downloader.png")
headingIcon = Label(root, image=file)
headingIcon.pack(side=TOP, fill=X, pady=10)

# url
l = Label(root, font=font, text="Enter URL of Video")
l.pack(side=TOP)
urlField = Entry(root, font=font, justify=CENTER)
urlField.pack(side=TOP, fill=X, padx=10, pady=10)
urlField.focus()



# download button
downloadBtn = Button(root, font=font, text="Download", relief=RAISED, command=btnClick)
downloadBtn.pack(side=TOP, pady=20)

root.mainloop()
