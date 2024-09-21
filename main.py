import cv2
import numpy as np

# Load the image
img = cv2.imread("tom.png")

# Check if the image is loaded correctly
if img is None:
    print("Error: Could not load the image.")
    exit()

# Define the house shape
house_points = np.array(
    [
        [100, 100],  # top-left
        [200, 100],  # top-right
        [200, 200],  # bottom-right
        [150, 250],  # bottom of the roof
        [100, 200],  # bottom-left
        [100, 100],  # top-left (close the shape)
    ]
)

# Draw the house shape on the image
cv2.polylines(img, [house_points], True, (0, 0, 255), 2)

# Display the output
cv2.imshow("House", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
