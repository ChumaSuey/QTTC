def translate_quake_text(text):
  """
  This function translates English text into Quake trigger text format.

  Args:
      text: The raw English text as a string.

  Returns:
      The translated Quake trigger text as a string.
  """
  # Replace double quotes with backticks
  filtered_text = text.replace("'", "`")
  filtered_text = filtered_text.replace('"', '`')

  # Split the text into words
  words = filtered_text.split()

  # Build the translated text line by line
  translated_text = ""
  current_line = ""
  for word in words:
    # Check if adding the word exceeds the character limit
    if len(current_line) + len(word) + 1 > 40:  # +1 for space
      # Add a line break and start a new line
      translated_text += current_line + "\\n"
      current_line = ""
    # Add the word with a space
    current_line += word + " "

  # Add the last line (if any)
  if current_line:
    translated_text += current_line + "\n"

  return translated_text
