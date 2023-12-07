def classify_object(width, height, depth):
    # Object classification based on dimensions
    if width > 300 and height > 300 and depth > 300:
        return "Large Object"
    elif width > 100 and height > 100 and depth > 100:
        return "Medium Object"
    else:
        return "Small Object"
