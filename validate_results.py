import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from check_kraken_results import check_file

VERSION = '20230204.1'

def run_process():
    print("---- Start processing ----")
    # title = title_entry.get()
    # print(title)
    filename = input_file.get()
    print(filename)
    
    check_file(filename)

    messagebox.showinfo(title = "LIMS results validation", message = "Results were validated.")
    
    # app.destroy()
    
def select_file():
    file_path = filedialog.askopenfilename(title='Select Kraken results file', initialdir='/')
    print(f'selected file: {file_path}')
    
    if file_path:
        input_file.set(file_path)
        process_button["state"] = "normal"
    
def run_about():
    message = f'Version {VERSION}\n\nContact information: Shuly Avraham'
    messagebox.showinfo(title = "About", message = message)
    
def run_exit():
    print("exit")
    app.destroy()
    
app = tk.Tk()

app.geometry("1000x100")
app.title('Kraken results validation')

input_file = tk.StringVar()
input_dir = tk.StringVar()

# title_label = tk.Label(app, text='Title')
# title_label.pack()
# title_entry = tk.Entry(app)
# title_entry.pack()

dir_button = tk.Button(app, text='Select Kraken file', command=select_file)
dir_button.pack()
dir_label = tk.Label(app, textvariable=input_file)
dir_label.pack()

process_button = tk.Button(app, text='Run validation', width=25, command=run_process)
process_button["state"] = "disabled"
process_button.pack()

menubar = tk.Menu(app)

menu1 = tk.Menu(menubar, tearoff=0)
menu1.add_command(label="Exit", underline=1, command=run_exit)
menubar.add_cascade(label="File", underline=0, menu=menu1)

menubar.add_command(label="About", underline=0, command=run_about)

app.config(menu=menubar)

app.mainloop()

