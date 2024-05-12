import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import ctypes
from main import translate_quake_text
import pyperclip

def translate_text():
    """Translates the text entered in the entry field and displays it."""
    english_text = entry_field.get()
    translated_text = translate_quake_text(english_text).replace("\\n", "\n")
    output_field.config(text=translated_text)

def save_file():
    """Saves the translated text to a file chosen by the user."""
    english_text = entry_field.get()
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

def copy():
    english_text = entry_field.get()
    translated_text = translate_quake_text(english_text)
    if translated_text:
        pyperclip.copy(translated_text)
        print('The text to be copied to the clipboard')
    else:
        print("No translated text available to copy.")


# Set DPI awareness
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
    # Get scaling factor
    scaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0) / 10
    # Adjust desired size based on a smaller multiplier (e.g., 0.75)
    adjusted_width = int(600 * 0.75 * scaleFactor)
    adjusted_height = int(300 * 0.75 * scaleFactor)
except:
    adjusted_width = 650
    adjusted_height = 300



# Create the main window
root = tk.Tk()
root.title("Quake Trigger Text Converter")

# Set window size
root.geometry(f"{adjusted_width}x{adjusted_height}")

# Entry field for English text
entry_field = tk.Entry(root, width=50, font=("Arial", 14))
entry_field.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# Translate button
button_style = ttk.Style()
button_style.configure("TButton", background="blue", foreground="black")  # Setting text color to black
translate_button = ttk.Button(root, text="Preview", command=translate_text, style="TButton")
translate_button.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

# Output field for translated text
output_field = tk.Label(root, text="", font=("Arial", 12))
output_field.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

# Save button
save_button = ttk.Button(root, text="Save as TXT file", command=save_file)
save_button.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

# Save button
copy_button = ttk.Button(root, text="Copy", command=copy)
copy_button.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")

root.mainloop()
