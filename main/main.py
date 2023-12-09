import cv2
import time
from process_image import process_image
from classify_object import classify_object


def main():
    # Open the camera
    cap = cv2.VideoCapture(0)

    # Set optional reading interval (unit: seconds)
    read_interval = 5  # Read every 5 seconds
    last_read_time = time.time() - read_interval

    while True:
        # Read image from the camera
        ret, frame = cap.read()

        # Check if it's time for a new reading
        current_time = time.time()
        if current_time - last_read_time >= read_interval:
            # Process the image
            width, height, depth = process_image(frame)

            # Classify the object
            object_class = classify_object(width, height, depth)

            # Display information
            print(f"Object dimensions: {width} x {height} x {depth}")
            print(f"Object classification: {object_class}")

            # Display the object image
            cv2.imshow("Object Image", frame)

            # Update the last reading time
            last_read_time = current_time

        # Exit on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
