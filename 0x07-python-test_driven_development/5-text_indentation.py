#!/usr/bin/python3

""" Text indentation function"""


def text_indentation(text):
    """
    print New formatted line
    Check if the text is str
    if the check fail raise TypeError
    strip() usage to remove any leading space
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    punctuations = ['.', '?', ':']
    lines = []
    line = ""
    for char in text:
        line += char
        if char in punctuations:
            lines.append(line.strip())
            lines.append("")
            line = ""

    if line:
        lines.append(line.strip())

    for formatted_line in lines:
        print(formatted_line)
