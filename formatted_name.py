def get_formatted_name(first, last, middle = ''):
    """Згенерувати відформатоване повне імʼя"""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    clean = " ".join(full_name.split())
    return clean.title()


