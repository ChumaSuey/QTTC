import textwrap


def translate_quake_text(text):
    """
    This function translates English text into Quake trigger text format.

    Args:
        text: The raw English text as a string.

    Returns:
        The translated Quake trigger text as a string.
    """

    # Replace single curly quotes with backticks
    filtered_text = text.replace('‘', '`').replace('’', '`')
    # Replace double curly quotes with backticks
    filtered_text = filtered_text.replace('“', '`').replace('”', '`')
    # Replace double quotes with backticks
    filtered_text = filtered_text.replace('"', "`")
    translated_text = '\\n'.join(textwrap.wrap(
        filtered_text,
        40
    ))
    return translated_text


def remove_linebreaks(text):
    """
    This function removes the "/n" characters from the input text.

    Args:
        text: The text from which to remove the "/n" characters.

    Returns:
        The text with "/n" characters removed.
    """
    cleaned_text = text.replace("\\n", " ")
    return cleaned_text


    # Replace single quotes with backticks
    # filtered_text = text.replace("'", "`")