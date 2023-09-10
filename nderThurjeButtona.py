import csv
import tkinter
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import time
import pyautogui
from tkinter import PhotoImage
from PIL import Image, ImageTk
from tkinter import font

x_shift = 0
y_shift = 100
x_wp_shift = 0
y_wp_shift = 50
x_gmail_shift = 0
y_gmail_shift = 50
jeshile = "#3EAD7F"
gri = "#3B3B3B"
gri_leht = "#4C4C4C"
kuqe = '#E84B4F'


# Button commands to change frames
def change_to_duplicate_frame():
    frames["Duplicate"].pack(fill=tk.BOTH)
    frames["What's App"].pack_forget()
    frames["Gmail"].pack_forget()
    csv_button.config(state=tk.NORMAL)


def change_to_whatsapp_frame():
    frames["Duplicate"].pack_forget()
    frames["What's App"].pack(fill=tk.BOTH)
    frames["Gmail"].pack_forget()
    csv_button.config(state=tk.NORMAL)


def change_to_gmail_frame():
    frames["Duplicate"].pack_forget()
    frames["What's App"].pack_forget()
    frames["Gmail"].pack(fill=tk.BOTH)
    csv_button.config(state=tk.NORMAL)


# Random Functions
def display_duplicates():
    if not csv_file:
        messagebox.showerror("Error", "Please select a CSV file first.")
        return

    unique_numbers = set()
    duplicates_text = ""

    with open(csv_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row_number, row in enumerate(reader, start=1):
            phone_number, name = row
            if phone_number in unique_numbers:
                duplicates_text += f"Row {row_number}: {phone_number} - {name}\n"
            else:
                unique_numbers.add(phone_number)

    result_text.delete(1.0, tk.END)  # Clear previous content
    result_text.insert(tk.END, duplicates_text)

def csv_command():
    global csv_file, original_content
    csv_file = filedialog.askopenfilename(initialdir="/", title="Select CSV file",
                                          filetypes=(("CSV files", "*.csv"), ("all files", "*.*")))
    csv_file_path.set(csv_file.replace("C:/Users/User/Desktop/", ""))
    if csv_file:
        with open(csv_file, "r") as input_csv:
            original_content = input_csv.read()
        display_duplicates()

            # -------------WhatsApp-------------
def run_wp():
    if not csv_file:
        messagebox.showerror("Error", "Chose a CSV file")
        return
    pyautogui.hotkey('alt''tab')
    with open(csv_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        numbers = list(reader)
        pyautogui.hotkey('alt', 'tab')
        for number in numbers:
            text = textbox.get(1.0, tk.END)
            text = text.replace("{name}", number[1])
            window.clipboard_clear()
            window.clipboard_append(text)

            pyautogui.hotkey('ctrl', 'alt', 'n')
            time.sleep(0.3)
            pyautogui.typewrite("+355" + number[0])
            time.sleep(0.2)
            pyautogui.press("enter")
            time.sleep(0.3)
            pyautogui.hotkey('shift', 'enter')
            pyautogui.hotkey('shift', 'enter')
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(.3)
            pyautogui.press('enter')
            time.sleep(.2)
            pyautogui.press('esc')

            # -------------Gmail-------------


def run_gmail():
    time.sleep(1)
    with open(csv_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        emails = list(reader)
        pyautogui.hotkey('alt', 'tab')
        for email in emails:
            subject = subject_box.get()
            subject = subject.replace("{name}", email[1])
            window.clipboard_clear()
            window.clipboard_append(subject)
            pyautogui.press('c')
            time.sleep(0.3)
            pyautogui.typewrite(email[0])
            time.sleep(0.3)
            pyautogui.press('enter')
            pyautogui.press('tab')
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(0.4)
            pyautogui.press('tab')
            message = message_box.get("1.0", tk.END)
            message = message.replace("{name}", email[1])
            window.clipboard_clear()
            window.clipboard_append(message)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(0.7)
            pyautogui.hotkey('ctrl', 'enter')
            time.sleep(1)
            # -------------Duplicate-------------


def ruaj_first():
    unique_numbers = set()
    processed_content = []

    with open(csv_file, "r") as input_csv:
        reader = csv.reader(input_csv)
        for row in reader:
            phone_number, name = row
            if phone_number not in unique_numbers:
                processed_content.append(row)
                unique_numbers.add(phone_number)

    with open(csv_file, "w", newline="") as output_csv:
        writer = csv.writer(output_csv)
        writer.writerows(processed_content)
    display_duplicates()
    messagebox.showinfo("File Processing Complete", f"The file has been updated and changes are saved.")
    undo_button.config(state=tk.NORMAL)


def undo_changes():
    global csv_file, original_content
    if csv_file and original_content:
        with open(csv_file, "w") as file:
            file.write(original_content)

        messagebox.showinfo("Undo Complete", "The file has been reverted to its original state.")
        undo_button.config(state=tk.DISABLED)
    display_duplicates()

# Create main window
window = tk.Tk()
window.geometry("900x700+660+150")
window.title("NderThurje")
window.resizable(False, False)

# Create left frame
left_frame = tk.Frame(window, width=300, height=700, bg=gri, borderwidth=10, highlightbackground="#2B2B2B", highlightthickness=3)
left_frame.pack(side=tk.LEFT, fill='both', expand=True, anchor="n")

# Load Image
duplicate_image = Image.open("../images/duplicates1.png")
whatsapp_image = Image.open("../images/whatsapp1.png")
gmail_image = Image.open("../images/gmail1.png")
# Resize Image
duplicate_image.thumbnail((50, 50))
whatsapp_image.thumbnail((50, 50))
gmail_image.thumbnail((50, 50))
# Summon Image
duplicate_image = ImageTk.PhotoImage(duplicate_image)
whatsapp_image = ImageTk.PhotoImage(whatsapp_image)
gmail_image = ImageTk.PhotoImage(gmail_image)
# Creating Buttons Left Frame
duplicate_button = tk.Button(left_frame, relief="flat", highlightthickness=0, image=duplicate_image, width=50, height=50,
                             text="Duplicate", command=change_to_duplicate_frame, padx=10, pady=5, bg="white",
                             fg="black", bd=0, activeforeground='white', activebackground="black")
whatsapp_button = tk.Button(left_frame, relief="flat", highlightthickness=0, image=whatsapp_image, width=50, height=50,
                            text="WhatsApp", command=change_to_whatsapp_frame, padx=10, pady=5, bg="white", fg="black",
                            bd=0, activeforeground='white', activebackground="black")
gmail_button = tk.Button(left_frame, relief="flat", highlightthickness=0, image=gmail_image, width=50, height=50, text="Gmail",
                         command=change_to_gmail_frame, padx=10, pady=5, bg="white", fg="black", bd=0,
                         activeforeground='white', activebackground="black")
# CSV Selection Area Left Frame
csv_file_path = tk.StringVar()
csv_file_label = tk.Label(left_frame, text="Chose a CSV file", bg=gri, fg='white')
csv_file_entry = tk.Entry(left_frame, textvariable=csv_file_path, state="readonly")
csv_button = tk.Button(left_frame, relief="flat", text="CSV File", state=tk.DISABLED, command=csv_command, width=8, padx=10, pady=5, bg="white",
                       fg="black", bd=0, activeforeground='white', activebackground="black")
# Label
label = tk.Label(left_frame, text="Choose the script", font=("Dancing Script", 16), bg=gri, fg='white')
# LEFT LABEL LAYOUT
label.pack(pady=(100, 10))
duplicate_button.pack(pady=(70, 0))
whatsapp_button.pack(pady=(20, 0))
gmail_button.pack(pady=(20, 0))
csv_file_label.pack(pady=(70, 0))
csv_file_entry.pack(pady=(10, 0))
csv_button.pack(pady=(10, 0))

# Create right frame
right_frame = tk.Frame(window, width=600, height=700, bg=gri)
right_frame.pack(side=tk.RIGHT)

# Create frames for each option
frames = {}
# -------------------------------Zgjidhni-----------------------------------------#
frames["Zgjidhni"] = tk.Frame(right_frame, width=600, height=700, bg=gri)
frames["Zgjidhni"].pack_propagate(False)
# ---------------------------------Dupicate---------------------------------------#

frames["Duplicate"] = tk.Frame(right_frame, width=600, height=700, bg=gri)
frames["Duplicate"].pack_propagate(False)

# container to hold 2 buttons
container = tk.Label(frames["Duplicate"], bg=gri, fg="white", text="Removes duplicate")
# buttoni 1 left
button_left = tk.Button(container,relief="flat", command=ruaj_first, width=8, text='Change', bg="#FF7F50")
undo_button = tk.Button(container, relief="flat", text="Undo", command=undo_changes, width=8, bg="#FF0000")
result_label = tk.Label(frames["Duplicate"], text='Make sure to select a CSV file:', bg=gri, fg='white')
# PACKING DUPLICATES TOP
container.pack(side=tkinter.TOP)
button_left.pack(side=tkinter.LEFT, pady=(140, 50), padx=(30, 30))
undo_button.pack(side=tkinter.RIGHT, pady=(140, 50), padx=(30, 30))
result_label.pack(padx=10, pady=0)

# add a scrollable text widget to display the result
scrollbar = tk.Scrollbar(frames["Duplicate"])
scrollbar.pack(side='right', fill='y')
result_text = tk.Text(frames["Duplicate"], yscrollcommand=scrollbar.set, bg=gri_leht, fg="white")
result_text.pack(side='left', fill='both', expand=True)
scrollbar.config(command=result_text.yview)

# -------------------------------Whats App----------------------------------------#
frames["What's App"] = tk.Frame(right_frame, width=600, height=700, bg=gri)
frames["What's App"].pack_propagate(False)

mesazhi = tk.Label(frames["What's App"], text="Message Content:", font=("Arial", 14), bg=gri, fg=jeshile)
textbox = tk.Text(frames["What's App"], height=20, width=50, bg=gri_leht, fg="white")
run_wp = tk.Button(frames["What's App"], relief="flat", text="Run script", command=run_wp, width=8, padx=10, pady=5, bg=jeshile, fg="white",
                       bd=0, activeforeground=jeshile, activebackground="white")

mesazhi.pack(side=tkinter.TOP, pady=(120, 30))
textbox.pack(side=tkinter.TOP, pady=(0, 30))
run_wp.pack(side=tkinter.TOP, pady=(0, 0))
# -------------------------------Gmail----------------------------------------------#

frames["Gmail"] = tk.Frame(right_frame, width=600, height=700, bg=gri)
frames["Gmail"].pack_propagate(False)

subject_label = tk.Label(frames["Gmail"], text="Subject:", font=("Arial", 14), bg=gri, fg=kuqe)
subject_box = tk.Entry(frames["Gmail"], width=50, bg=gri_leht, fg="white")

message_label = tk.Label(frames["Gmail"], text="Message Content:", font=("Arial", 14), bg=gri, fg=kuqe)
message_box = tk.Text(frames["Gmail"], height=15, width=50, bg=gri_leht, fg="white")

run_gmail = tk.Button(frames["Gmail"], relief="flat", text="Run Script", command=run_gmail, width=8, padx=10, pady=5, bg=kuqe, fg="white", bd=0,
                       activeforeground=kuqe, activebackground="white")

subject_label.pack(side=tkinter.TOP, pady=(100, 0))
subject_box.pack(side=tkinter.TOP, pady=(30, 35))

message_label.pack(side=tkinter.TOP, pady=(0, 15))
message_box.pack(side=tkinter.TOP, pady=(0, 40))

run_gmail.pack(side=tkinter.TOP, pady=(0, 20))

# Start the GUI main loop
window.mainloop()
