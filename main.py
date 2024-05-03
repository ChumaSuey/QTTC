def translate_quake_text(text):
  """
  This function translates English text into Quake trigger text format.

  Args:
      text: The raw English text as a string.

  Returns:
      The translated Quake trigger text as a string.
  """
  # Replace double quotes with backticks
  filtered_text = text.replace('"', '`')

  # Split the text into words
  words = filtered_text.split()

  # Build the translated text line by line
  translated_text = ""
  current_line = ""
  for word in words:
    # Check if adding the word exceeds the character limit
    if len(current_line) + len(word) + 1 > 40:  # +1 for space
      # Add a line break and start a new line
      translated_text += current_line + "\n"
      current_line = ""
    # Add the word with a space
    current_line += word + " "

  # Add the last line (if any)
  if current_line:
    translated_text += current_line + "\n"

  return translated_text

# Get user input
raw_text = input("Enter English text to convert: ")

# Translate the text
translated_text = translate_quake_text(raw_text)


# Get the script's filename (assuming it's a .py file)
import os
script_filename = os.path.basename(__file__)

# Construct the output filename (in the same directory)
output_filename = os.path.splitext(script_filename)[0] + "_translated_text.txt"

# Save the translated text to a file
with open(output_filename, "w") as file:
  file.write(translated_text)
  print(f"Translated text saved to: {output_filename}")

#print(translated_text)

#print(repr(translated_text))

# Save the translated text to a file (optional)
# with open("quake_text.txt", "w") as file:
#   file.write(translated_text)
#   print("Translated text saved to quake_text.txt")