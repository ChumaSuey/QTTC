import textwrap


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
    # Replace single quotes with backticks
    filtered_text = filtered_text.replace('"', "`")
    translated_text = '\\n'.join(textwrap.wrap(
        filtered_text,
        40
    ))
    return translated_text
