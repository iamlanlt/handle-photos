import cv2

def process_image(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply GaussianBlur to reduce noise and improve contour detection
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Use Canny edge detection to find edges in the image
    edges = cv2.Canny(blurred, 50, 150)

    # Find contours in the edged image
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Initialize variables for object dimensions
    object_width, object_height, object_depth = 0, 0, 0

    # Iterate through the contours to find the bounding box
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)

        # Update object dimensions if the bounding box dimensions are larger
        if w > object_width:
            object_width = w

        if h > object_height:
            object_height = h

    # Assume a constant depth or use additional techniques to estimate depth
    object_depth = min(object_width, object_height)  

    return object_width, object_height, object_depth
