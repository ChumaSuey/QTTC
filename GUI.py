import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import ctypes
from main import translate_quake_text
import pyperclip

def translate_text():
    """Translates the text entered in the text field and displays it."""
    english_text = text_field.get("1.0", tk.END).replace("/n", "\n").replace("//n", "\n")
    translated_text = translate_quake_text(english_text)
    output_field.config(state=tk.NORMAL)
    output_field.delete("1.0", tk.END)
    output_field.insert(tk.END, translated_text)
    output_field.config(state=tk.DISABLED)
    newline_label.config(text="Newline added")

def clear_text():
    """Clears the text entered in the text field."""
    text_field.delete("1.0", tk.END)
    newline_label.config(text="")

def save_file():
    """Saves the translated text to a file chosen by the user."""
    english_text = text_field.get("1.0", tk.END)
    translated_text = translate_quake_text(english_text)
    if translated_text:  # Check if text is present before saving
        filename = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt")],
            title="Save Translated Text"
        )
        if filename:  # Check if a filename was chosen
            with open(filename, "w") as file:
                file.write(translated_text)
                print(f"Translated text saved to: {filename}")
    else:
        print("No translated text available to save.")
    newline_label.config(text="")

def copy():
    """Copies the translated text to the clipboard."""
    translated_text = output_field.get("1.0", tk.END)
    if translated_text:
        pyperclip.copy(translated_text)
        print('The text to be copied to the clipboard')
    else:
        print("No translated text available to copy.")
    newline_label.config(text="")

def copy_trenchbroom():
    """Copies the translated text to the clipboard in the format you specified."""
    translated_text = output_field.get("1.0", tk.END)
    if translated_text:
        translated_text = '// entity 0\n{\n'
        translated_text += '  "classname" "trigger_relay"\n'
        translated_text += '  "message" "' + translated_text + '"\n'
        translated_text += '}\n'  # Add the closing curly brace here
        pyperclip.copy(translated_text)
        print('The text to be copied to the clipboard')
    else:
        print("No translated text available to copy.")
    newline_label.config(text="")

root = tk.Tk()
root.title("Quake Trigger Text Converter")

newline_label = tk.Label(root, text="")
newline_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

preview_label = ttk.Label(root, text="Preview:")
preview_label.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

text_field = tk.Text(root, height=10, width=50, font=("Arial", 14))
text_field.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

scrollbar = tk.Scrollbar(root)
scrollbar.grid(row=0, column=1, sticky="nsew")
text_field.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text_field.yview)

translate_button = ttk.Button(root, text="Translate", command=translate_text)
translate_button.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

clear_button = ttk.Button(root, text="Clear", command=clear_text)
clear_button.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

save_button = ttk.Button(root, text="Save", command=save_file)
save_button.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

copy_button = ttk.Button(root, text="Copy", command=copy)
copy_button.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

copy_trenchbroom_button = ttk.Button(root, text="Copy Trenchbroom Format", command=copy_trenchbroom)
copy_trenchbroom_button.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

preview_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")


output_field = tk.Text(root, height=10, width=50, state=tk.DISABLED, font=("Arial", 14))
output_field.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

root.mainloop()