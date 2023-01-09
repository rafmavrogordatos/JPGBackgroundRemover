import cv2
import tkinter as tk
from tkinter import filedialog

# Create the input field
input_label = tk.Label(root, text="Input File: ", font=("Arial", 14), bg="#cccccc", fg="#000000")
input_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
input_entry = tk.Entry(root, font=("Arial", 14), bg="#ffffff", fg="#000000")
input_entry.grid(row=0, column=1, sticky="w", padx=5, pady=5)
input_button = tk.Button(root, text="Browse", font=("Arial", 14), bg="#cccccc", fg="#000000", command=input_browse)
input_button.grid(row=0, column=2, sticky="w", padx=5, pady=5)

# Create the output field
output_label = tk.Label(root, text="Output File: ", font=("Arial", 14), bg="#cccccc", fg="#000000")
output_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
output_entry = tk.Entry(root, font=("Arial", 14), bg="#ffffff", fg="#000000")
output_entry.grid(row=1, column=1, sticky="w", padx=5, pady=5)
output_button = tk.Button(root, text="Browse", font=("Arial", 14), bg="#cccccc", fg="#000000", command=output_browse)
output_button.grid(row=1, column=2, sticky="w", padx=5, pady=5)

# Create the process button
process_button = tk.Button(root, text="Process", font=("Arial", 14), bg="#cccccc", fg="#000000", command=process)
process_button.grid(row=2, column=1, sticky="e", padx=5, pady=5)

def input_browse():
    # Open a file dialog and get the selected file's path
    filepath = filedialog.askopenfilename()
    # Update the input entry with the selected file's path
    input_entry.delete(0, "end")
    input_entry.insert(0, filepath)

def output_browse():
    # Open a file dialog and get the selected file's path
    filepath = filedialog.asksaveasfilename(defaultextension=".jpg")
    # Update the output entry with the selected file's path
    output_entry.delete(0, "end")
    output_entry.insert(0, filepath)

def process():
    # Get the input and output file paths from the entries
    input_file = input_entry.get()
    output_file = output_entry.get()

    # Read the input image
    image = cv2.imread(input_file)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to the grayscale image to create a black and white image
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Find the contours in the thresholded image
    _, contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Find the largest contour
    largest_contour = max(contours, key=cv2.contourArea)

    # Create a mask using the largest contour
    mask = np.zeros(image.shape, np.uint8)
    cv2.drawContours(mask, [largest_contour], -1, (255, 255, 255), -1)

    # Remove the background from the image using the mask
    result = cv2.bitwise_and(image, mask)

    # Save the resulting image to the output file
    cv2.imwrite(output_file, result)

