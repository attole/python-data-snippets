import tkinter as tk

def change_theme():
    if root["bg"] == light_bg:
        root.config(bg=dark_root_bg)
        general_info.config(bg=dark_bg, fg=dark_fg)
        task_label.config(bg=dark_bg, fg=dark_fg)
        entry.config(bg=dark_entry_bg, fg=dark_fg, insertbackground=dark_fg)
        result_label.config(bg=dark_bg, fg=dark_fg)
        format_button.config(bg=dark_button_bg, fg=dark_button_fg)
        theme_button.config(bg=dark_button_bg, fg=dark_button_fg, text="Light Mode")
    else:
        root.config(bg=light_bg)
        general_info.config(bg=light_bg, fg=light_fg)
        task_label.config(bg=light_bg, fg=light_fg)
        entry.config(bg=light_entry_bg, fg=light_fg, insertbackground=light_fg)
        result_label.config(bg=light_bg, fg=light_fg)
        format_button.config(bg=light_bg, fg=light_fg)
        theme_button.config(bg=light_button_bg, fg=light_button_fg, text="Dark Mode")

def format_number():
    user_input = entry.get()

    if all(element.isdigit() for element in user_input):
        formatted_number = ' '.join([user_input[max(i - 3, 0):i] for i in range(len(user_input), 0, -3)][::-1])
        result_label.config(text=formatted_number)
    else:
        result_label.config(text="Enter a valid number!!")

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
root.title("Number Formatter")
root.config(bg=dark_root_bg)

general_info = '''
Інформація про автора ПЗ: 
ВНЗ: "Київський політехнічний інститут імені Ігоря Сікорського"
Кафедра: Програмного забезпечення комп’ютерних систем
Факультет: Факультет прикладної математики
група: КП-11 
ПІБ: Кучеренко Сергій
Опис ПЗ: 
ПЗ розділяє число на трійки, починаючи з правого кінця
'''

general_info = tk.Label(root, text=general_info, font=("Arial", 10), justify="left", bg=dark_bg, fg=dark_fg)
general_info.grid(row=0, column=0, rowspan=3, sticky="nsew", padx=10, pady=10)

task_label = tk.Label(root, text="Enter a number:", font=("Arial", 12), bg=dark_bg, fg=dark_fg)
task_label.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

entry = tk.Entry(root, width=30, font=("Arial", 12), justify="center", bg=dark_entry_bg, fg=dark_fg)
entry.grid(row=1, column=1, sticky="nsew", padx=10, pady=5)

format_button = tk.Button(root, text="Format", font=("Arial", 12), command=format_number, bg=dark_button_bg, fg=dark_button_fg)
format_button.grid(row=2, column=1, sticky="nsew", padx=10, pady=5)

theme_button = tk.Button(root, text="Light mode", font=("Arial", 12), command=change_theme, bg=dark_button_bg, fg=dark_button_fg)
theme_button.grid(row=3, column=0, sticky="nsew", padx=10, pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12), bg=dark_bg, fg=dark_fg)
result_label.grid(row=3, column=1, sticky="nsew", padx=10, pady=5)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure([0, 1, 2, 3], weight=1)

root.mainloop()