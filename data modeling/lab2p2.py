import tkinter as tk
import numpy as np

def change_theme():
    if root["bg"] == light_bg:
        root.config(bg=dark_root_bg)
        general_info_label.config(bg=dark_bg, fg=dark_fg)
        task_label.config(bg=dark_bg, fg=dark_fg)
        matrix_text.config(bg=dark_entry_bg, fg=dark_fg, insertbackground=dark_fg)
        result_label.config(bg=dark_bg, fg=dark_fg)
        format_button.config(bg=dark_button_bg, fg=dark_button_fg)
        theme_button.config(bg=dark_button_bg, fg=dark_button_fg, text="Light Mode")
    else:
        root.config(bg=light_bg)
        general_info_label.config(bg=light_bg, fg=light_fg)
        task_label.config(bg=light_bg, fg=light_fg)
        matrix_text.config(bg=light_entry_bg, fg=light_fg, insertbackground=light_fg)
        result_label.config(bg=light_bg, fg=light_fg)
        format_button.config(bg=light_bg, fg=light_fg)
        theme_button.config(bg=light_button_bg, fg=light_button_fg, text="Dark Mode")

def format():
    user_input = matrix_text.get("1.0", tk.END).strip()
    
    try:
        # convert string to float, possible ValueError
        matrix = np.array([list(line) for line in user_input.split('\n')], dtype=float)

        # assume matrix is valid and square, possible ValueError
        if np.linalg.det(matrix) == 0:
           result_label.config(text="Matrix is singular!!")
           return

        result = np.array([[f"{x}".ljust(4, '0') for x in row] for row in np.round(np.linalg.inv(matrix), decimals=2)])
        result_label.config(text=result)
    except:
        result_label.config(text="Enter a valid matrix!!")

light_bg = "#ffffff"
light_fg = "#000000"
light_entry_bg = "#f0f0f0"
light_button_bg = "#d0d0d0"
light_button_fg = "#000000"

dark_root_bg = "#2c2c2c"
dark_bg = "#3D3D3D"
dark_fg = "#ffffff"
dark_entry_bg = "#3d3d3d"
dark_button_bg = "#444444"
dark_button_fg = "#ffffff"

root = tk.Tk()
root.geometry("700x200")
root.title("Matrix invertor")
root.config(bg=dark_root_bg)

general_info = '''
Інформація про автора ПЗ: 
ВНЗ: "Київський політехнічний інститут імені Ігоря Сікорського"
Кафедра: Програмного забезпечення комп’ютерних систем
Факультет: Факультет прикладної математики
група: КП-11 
ПІБ: Кучеренко Сергій
Опис ПЗ: 
ПЗ повертає значення зворотної матриці
'''

general_info_label = tk.Label(root, text=general_info, font=("Arial", 10), justify="left", bg=dark_bg, fg=dark_fg)
general_info_label.grid(row=0, column=0, rowspan=3, sticky="nsew", padx=10, pady=10)

task_label = tk.Label(root, text="Enter matrix:", font=("Arial", 12), bg=dark_bg, fg=dark_fg)
task_label.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

matrix_text = tk.Text(root, height=3, width=3, font=("Arial", 12), bg=dark_entry_bg, fg=dark_fg)
matrix_text.grid(row=1, column=1, sticky="nsew", padx=10, pady=5)

format_button = tk.Button(root, text="Format", font=("Arial", 12), command=format, bg=dark_button_bg, fg=dark_button_fg)
format_button.grid(row=2, column=1, sticky="nsew", padx=10, pady=5)

theme_button = tk.Button(root, text="Light mode", font=("Arial", 12), command=change_theme, bg=dark_button_bg, fg=dark_button_fg)
theme_button.grid(row=3, column=0, sticky="nsew", padx=10, pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12), bg=dark_bg, fg=dark_fg)
result_label.grid(row=3, column=1, sticky="nsew", padx=10, pady=5)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure([0, 1, 2, 3], weight=1)

root.mainloop()

root = tk.Tk()
button = tk.Button(root, text="Button")
button.pack(padx=20, pady=20)

root.grid_columnconfigure(0, weight=1)
root.mainloop()