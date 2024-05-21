"""
Tkinter app
"""

from tkinter import Tk, filedialog, messagebox
from tkinter.ttk import Button, Label, Progressbar, Frame

from pdf_splitter import PdfSplitter

FILEPATHS = []


def browse_files_callback():
    """
    callback function for opening the file explorer
    """
    global FILEPATHS
    FILEPATHS = filedialog.askopenfilenames(initialdir="",
                                            title="Select files",
                                            filetypes=(("PDFs", "*.pdf"),))
    files_label["text"] = f"{len(FILEPATHS)} files selected"


def split_files_callback():
    """
    callback function handling click on split files
    """
    if len(FILEPATHS) == 0:
        print("no files selected")
        return

    for path in FILEPATHS:
        splitter = PdfSplitter(path)
        splitter.split()
        progress.step(1 / len(FILEPATHS) * 100)

    messagebox.showinfo("Success", "PDFs splitted successfully")


app = Tk()
app.title("PDF Splitter")

# set minimum window size value
app.minsize(300, 400)
# set maximum window size value
app.maxsize(300, 400)

frame = Frame(app)

explore_button = Button(frame,
                        text="Browse Files",
                        command=browse_files_callback)

files_label = Label(frame, text="")

split_button = Button(frame, text="Split Files", command=split_files_callback)

progress = Progressbar(frame)

close_button = Button(frame, text="Close", command=app.quit)

explore_button.pack(pady=5)
files_label.pack(pady=5)
split_button.pack(pady=5)
progress.pack(pady=5)
close_button.pack(pady=5)

frame.place(anchor='center', relx=.5, rely=.45)

app.mainloop()
