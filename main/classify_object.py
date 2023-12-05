def classify_object(width, height, depth):
    # Object classification based on dimensions
    if width > 8 and height > 8 and depth > 8:
        return "Large Object"
    elif width > 4 and height > 4 and depth > 4:
        return "Medium Object"
    else:
        return "Small Object"
