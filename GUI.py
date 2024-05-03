import tkinter as tk
from main import translate_quake_text  # Import the function
import tkinter.filedialog as fd  # Import for file dialog

def translate_text():
  """Translates the text entered in the entry field and displays it."""
  english_text = entry_field.get()
  translated_text = translate_quake_text(english_text)
  output_field.config(text=translated_text)

def save_file():
  """Saves the translated text to a file chosen by the user."""
  translated_text = output_field.cget("text")  # Get translated text from label
  if translated_text:  # Check if text is present before saving
    filename = fd.asksaveasfilename(
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

# Create the main window
root = tk.Tk()
root.title("Quake Trigger Text Converter")

# Entry field for English text
entry_field = tk.Entry(root, width=50)
entry_field.pack()

# Translate button
translate_button = tk.Button(root, text="Translate", command=translate_text)
translate_button.pack()

# Output field for translated text
output_field = tk.Label(root, text="")
output_field.pack()

# Save button (functionality to be added later)
save_button = tk.Button(root, text="Save", command=save_file)
save_button.pack()

# Run the main event loop
root.mainloop()