import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from main import translate_quake_text
from main import remove_linebreaks
import pyperclip

def translate_text():
    """Translates the text entered in the text field and displays it."""
    english_text = text_field.get("1.0", tk.END).replace("/n", "\n").replace("//n", "\n")
    translated_text = translate_quake_text(english_text)
    output_field.config(state=tk.NORMAL)
    output_field.delete("1.0", tk.END)
    output_field.insert(tk.END, translated_text)
    output_field.config(state=tk.DISABLED)
    newline_label.config(text="Text translated to Quake format successfully!")

def clear_text():
    """Clears the text entered in the text field and the translated text screen."""
    text_field.delete("1.0", tk.END)
    output_field.config(state=tk.NORMAL)
    output_field.delete("1.0", tk.END)
    output_field.config(state=tk.DISABLED)
    newline_label.config(text="")

def linebreak_cleaning():
    """Removes the "\n" characters from the text field."""
    current_text = text_field.get("1.0", tk.END)
    updated_text = remove_linebreaks(current_text)
    text_field.delete("1.0", tk.END)
    text_field.insert(tk.END, updated_text)

    # Update the output field with the cleaned text at the end
    output_field.delete("1.0", tk.END)  # Clear the existing content
    output_field.insert(tk.END, updated_text)  # Insert the cleaned text at the end
    newline_label.config(text="Linebreaks cleaned!")
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
    newline_label.config(text="Text saved as a file in the selected destination!")

def copy():
    """Copies the translated text to the clipboard."""
    translated_text = output_field.get("1.0", tk.END)
    if translated_text:
        pyperclip.copy(translated_text)
        print('The text to be copied to the clipboard')
    else:
        print("No translated text available to copy.")
    newline_label.config(text="Text copied to clipboard!")

def copy_trenchbroom():
    """Copies the translated text to the clipboard in the format of a trigger_relay (point entity)."""
    translated_text = output_field.get("1.0", tk.END)
    if translated_text:
        translated_text = translated_text.rstrip('\n')
        translated_text2 = '// entity 0\n{\n'
        translated_text2 += '  "classname" "trigger_relay"\n'
        translated_text2 += '  "message" "' + translated_text + '"\n'
        translated_text2 += '}\n'  # Add the closing curly brace here
        absoluteshambler = translated_text2
        #pyperclip.copy(translated_text)
        pyperclip.copy(absoluteshambler)
        print('Text copied to the clipboard')
    else:
        print("No translated text available to copy.")
    newline_label.config(text="Trigger_relay (point entity) copied to clipboard!")

def copy_trenchbroom2():
    """Copies the translated text to the clipboard in the format of a trigger_textstory (brush entity)."""
    translated_text = output_field.get("1.0", tk.END)
    if translated_text:
        translated_text = translated_text.rstrip('\n')
        translated_text2 = '// entity 0\n{\n'
        translated_text2 += '  "classname" "trigger_textstory"\n'
        translated_text2 += '  "message" "' + translated_text + '"\n'
        translated_text2 += '// brush 0\n{\n'
        translated_text2 += '( -96 -144 64 ) ( -96 -143 64 ) ( -96 -144 65 ) trigger [ 0 -1 0 0 ] [ 0 0 -1 0 ] 0 1 1\n'
        translated_text2 += '( -112 -112 64 ) ( -112 -112 65 ) ( -111 -112 64 ) trigger [ 1 0 0 0 ] [ 0 0 -1 0 ] 0 1 1\n'
        translated_text2 += '( -112 -144 32 ) ( -111 -144 32 ) ( -112 -143 32 ) trigger [ -1 0 0 0 ] [ 0 -1 0 0 ] 0 1 1\n'
        translated_text2 += '( -48 -64 80 ) ( -48 -63 80 ) ( -47 -64 80 ) trigger [ 1 0 0 0 ] [ 0 -1 0 0 ] 0 1 1\n'
        translated_text2 += '( -48 -64 80 ) ( -47 -64 80 ) ( -48 -64 81 ) trigger [ -1 0 0 0 ] [ 0 0 -1 0 ] 0 1 1\n'
        translated_text2 += '( -48 -64 80 ) ( -48 -64 81 ) ( -48 -63 80 ) trigger [ 0 1 0 0 ] [ 0 0 -1 0 ] 0 1 1\n'
        translated_text2 += '}\n'  # Add the closing curly brace here
        absoluteshambler = translated_text2
        pyperclip.copy(absoluteshambler)
        print('Text copied to the clipboard')
    else:
        print("No translated text available to copy.")
    newline_label.config(text="Trigger_textstory (point entity) copied to clipboard!")


root = tk.Tk()
root.title("Quake Trigger Text Converter")

newline_label = tk.Label(root, text="")
newline_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

preview_label = ttk.Label(root, text="Preview:")
preview_label.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

text_field = tk.Text(root, height=10, width=50, font=("Arial", 14))
text_field.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

copy_save_row = tk.Frame(root)
copy_save_row.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")


scrollbar = tk.Scrollbar(root)
scrollbar.grid(row=0, column=1, sticky="nsew")
text_field.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text_field.yview)

translate_button = ttk.Button(root, text="Translate", command=translate_text)
translate_button.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

clear_button = ttk.Button(root, text="Clear", command=clear_text)
clear_button.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

save_button = ttk.Button(root, text="Save", command=save_file)
save_button.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")

copy_button = ttk.Button(root, text="Copy", command=copy)
copy_button.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

copy_trenchbroom_button = ttk.Button(root, text="Copy into trigger_relay", command=copy_trenchbroom)
copy_trenchbroom_button.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

copy_trenchbroom_button2 = tk.Button(root, text="Copy into trigger_textstory", command=copy_trenchbroom2)
copy_trenchbroom_button2.grid(row=2, column=2, padx=10, pady=10, sticky="nsew")

linebreak_clean_button = ttk.Button(root, text="Linebreak Cleaning", command=linebreak_cleaning)
linebreak_clean_button.grid(row=1, column=3, padx=10, pady=10, sticky="nsew")


preview_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")


output_field = tk.Text(root, height=10, width=50, state=tk.DISABLED, font=("Arial", 14))
output_field.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

root.mainloop()
