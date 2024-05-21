"""
Tkinter app
"""

from tkinter import Tk, filedialog
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


app = Tk()

# set minimum window size value
app.minsize(400, 400)
# set maximum window size value
app.maxsize(400, 400)

frame = Frame(app)

explore_button = Button(frame,
                        text="Browse Files",
                        command=browse_files_callback)

files_label = Label(frame, text="")

split_button = Button(frame, text="Split Files", command=split_files_callback)

progress = Progressbar(frame)

close_button = Button(frame, text="Close", command=app.quit)

explore_button.pack(anchor='center')
files_label.pack(anchor='center')
split_button.pack(anchor='center')
progress.pack(anchor='center')
close_button.pack(anchor='center')

frame.pack(anchor='center')

app.mainloop()
