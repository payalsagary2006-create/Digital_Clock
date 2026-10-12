import tkinter as tk
from datetime import datetime


def update_clock():
    current_time = datetime.now().strftime("%I:%M:%S %p")
    current_date = datetime.now().strftime("%A, %d %B %Y")

    time_label.config(text=current_time)
    date_label.config(text=current_date)

    window.after(1000, update_clock)


# Create the main window
window = tk.Tk()
window.title("My Digital Clock")
window.geometry("500x250")
window.configure(bg="black")
window.resizable(False, False)

# Heading
heading = tk.Label(
    window,
    text="DIGITAL CLOCK",
    font=("Arial", 18, "bold"),
    fg="white",
    bg="black"
)
heading.pack(pady=15)

# Display the time
time_label = tk.Label(
    window,
    font=("Arial", 36, "bold"),
    fg="cyan",
    bg="black"
)
time_label.pack(pady=10)

# Display the date
date_label = tk.Label(
    window,
    font=("Arial", 14),
    fg="white",
    bg="black"
)
date_label.pack(pady=5)

# Start updating the clock
update_clock()

# Keep the window open
window.mainloop()