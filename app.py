"""
Tkinter app
"""

from tkinter import Tk, filedialog, messagebox
from tkinter.ttk import Button, Label, Progressbar, Frame, Entry

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
    suffix = suffix_input.get().strip()

    target_dir = target_dir_input.get().strip()
    target_dir = None if target_dir == "" else target_dir

    if len(FILEPATHS) == 0:
        messagebox.showerror("Error", "No files selected")
        return

    for path in FILEPATHS:
        splitter = PdfSplitter(path, suffix, target_dir)
        splitter.split()
        progress.step(1 / len(FILEPATHS) * 100)

    messagebox.showinfo("Success", "PDFs splitted successfully")


app = Tk()
app.title("PDF Splitter")

# set minimum window size value
app.minsize(400, 400)
# set maximum window size value
app.maxsize(400, 400)

frame = Frame(app)

explore_button = Button(frame, text="Browse Files", command=browse_files_callback)
explore_button.grid(row=0, column=0, pady=5)

files_label = Label(frame, text="")
files_label.grid(row=0, column=1, pady=5)

Label(frame, text="Suffix").grid(row=1, column=0, pady=5)
suffix_input = Entry(frame)
suffix_input.grid(row=1, column=1, pady=5)

Label(frame, text="Target Directory").grid(row=2, column=0, pady=5)
target_dir_input = Entry(frame)
target_dir_input.grid(row=2, column=1, pady=5)

split_button = Button(frame, text="Split Files", command=split_files_callback)
split_button.grid(row=3, column=0, pady=5)

progress = Progressbar(frame)
progress.grid(row=3, column=1, pady=5)

close_button = Button(frame, text="Close", command=app.quit)
close_button.grid(row=4, column=0, pady=5)

frame.place(anchor='center', relx=.5, rely=.45)

app.mainloop()
