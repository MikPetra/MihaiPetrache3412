import os
import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox
import webbrowser
from datetime import datetime


#URL_SCHEDULE = "https://www.ub.ro/stiinte/studenti/orar"
URL_SCHEDULE = "https://ifrinf.ub.ro/wp-content/uploads/2024/11/ORAR_Info_IFR_sem_I_2024-2025_definitiv.pdf"
URL_EXAMS = "https://www.ub.ro/stiinte/studenti/programare-examene"
URL_CONTACT = "https://www.ub.ro/stiinte/contact"
URL_PAYMENTS = "https://smartums.ub.ro/as/dashboard"

BUTTON_SCHEDULE = "ORAR INFORMATICĂ IFR"


def open_url(url):
    webbrowser.open(url)

def calculate_weeks_left():
    today = datetime.today()
    current_year = today.year

    first_semester_start = datetime(current_year, 10, 1)
    first_semester_end = datetime(current_year + 1, 2, 12)
    second_semester_start = datetime(current_year, 2, 13)
    second_semester_end = datetime(current_year, 7, 1)

    if first_semester_start <= today <= first_semester_end:
        weeks_left = (first_semester_end - today).days // 7
        return f"Saptamani ramase semestru 1: {weeks_left}"
    elif second_semester_start <= today <= second_semester_end:
        weeks_left = (second_semester_end - today).days // 7
        return f"Saptamani ramase semestru 2: {weeks_left}"
    else:
        return "Vacanta!"
    
def calculate_days_left():
    try:
        user_date = date_entry.get()
        # Convert to a datetime object
        target_date = datetime.strptime(user_date, "%d-%m-%Y")
        today = datetime.today()

        if target_date < today:
            messagebox.showinfo("Info", "Nu ai un Delorean!")
        else:
            days_left = (target_date - today).days
            messagebox.showinfo("Info", f"Zile pana la data {user_date}: \n {days_left}")
    except ValueError:
        messagebox.showerror("Eroare", "Format invalid! Introdu DD-MM-YYYY.")

app = tk.Tk()
app.title("Student Utility")
app.geometry("250x350")

script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, "LOGO_INFORMATICA_IFR_SMALL.png")

try:
    image = PhotoImage(file=image_path)
    image_label = tk.Label(app, image=image)
    image_label.grid(row=0, column=0, rowspan=3, padx=10, pady=10)
except:
    # If the image can't be loaded, display a placeholder label
    image_label = tk.Label(app, text="[Image Placeholder]", width=15, height=5, bg="gray")
    image_label.grid(row=0, column=0, rowspan=3, padx=10, pady=10)

buttonSchedule = tk.Button(app, text="Orar", command=lambda: open_url(URL_SCHEDULE), width=10, height=2, bg="lightblue", fg="black")
buttonSchedule.grid(row=0, column=1, padx=10, pady=5)

buttonExams = tk.Button(app, text="Examene", command=lambda: open_url(URL_EXAMS), width=10, height=2, bg="lightgreen", fg="black")
buttonExams.grid(row=1, column=1, padx=10, pady=5)

buttonContact = tk.Button(app, text="Secretariat", command=lambda: open_url(URL_CONTACT), width=10, height=2, bg="lightgrey", fg="black")
buttonContact.grid(row=2, column=1, padx=10, pady=5)

buttonPayments = tk.Button(app, text="Plati", command=lambda: open_url(URL_PAYMENTS), width=10, height=2, bg="darkred", fg="black")
buttonPayments.grid(row=3, column=1, padx=10, pady=5)

semester_label = tk.Label(app, text=calculate_weeks_left(), font=("Arial", 10))
semester_label.grid(row=4, column=0, columnspan=2, sticky="w", padx=10, pady=5)

instruction_label = tk.Label(app, text="Introdu o zi in formatul:", font=("Arial", 10))
instruction_label.grid(row=5, column=0, columnspan=2, sticky="w", padx=10, pady=5)
instruction_label_date = tk.Label(app, text="(DD-MM-YYYY)", font=("Arial", 10))
instruction_label_date.grid(row=6, column=1, columnspan=2, sticky="w", padx=10, pady=5)
date_entry = tk.Entry(app, width=15, justify="center")
date_entry.grid(row=6, column=0, columnspan=2, sticky="w", padx=10, pady=5)
calculate_button = tk.Button(app, text="Calculeaza zile pana la exam", font=("Arial", 12), bg="blue", fg="white", command=calculate_days_left)
calculate_button.grid(row=7, column=0, columnspan=2, sticky="w", padx=10, pady=5)

app.mainloop()
