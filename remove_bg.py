import cv2
import tkinter as tk
from tkinter import filedialog

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("JPG Background Remover")

        # Create the input field
        self.input_label = tk.Label(root, text="Input File: ", font=("Arial", 14), bg="#cccccc", fg="#000000")
        self.input_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.input_entry = tk.Entry(root, font=("Arial", 14), bg="#ffffff", fg="#000000")
        self.input_entry.grid(row=0, column=1, sticky="w", padx=5, pady=5)
        self.input_button = tk.Button(root, text="Browse", font=("Arial", 14), bg="#cccccc", fg="#000000", command=self.input_browse)
        self.input_button.grid(row=0, column=2, sticky="w", padx=5, pady=5)
        
        # Create the output field
        self.output_label = tk.Label(root, text="Output File: ", font=("Arial", 14), bg="#cccccc", fg="#000000")
        self.output_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.output_entry = tk.Entry(root, font=("Arial", 14), bg="#ffffff", fg="#000000")
        self.output_entry.grid(row=1, column=1, sticky="w", padx=5, pady=5)
        self.output_button = tk.Button(root, text="Browse", font=("Arial", 14), bg="#cccccc", fg="#000000", command=self.output_browse)
        self.output_button.grid(row=1, column=2, sticky="w", padx=5, pady=5)
        
        # Create the process button
        self.process_button = tk.Button(root, text="Process", font=("Arial", 14), bg="#cccccc", fg="#000000", command=self.process)
        self.process_button.grid(row=2, column=1, sticky="e", padx=5, pady=5)
        
    def input_browse(self):
        # Open a file dialog and get the selected file's path
        filepath = filedialog.askopenfilename()
        # Update the input entry with the selected file's path
        self.input_entry.delete(0, "end")
        self.input_entry.insert(0, filepath)
        
    def output_browse(self):
        # Open a file dialog and get the selected file's path
        filepath = filedialog.asksaveasfilename(defaultextension=".jpg")
        # Update the output entry with the selected file's path
        self.output_entry.delete(0, "end")
        self.output_entry.insert(0, filepath)
        
    def process(self):
        # Get the input and output file paths from the entries
        input_file = self.input_entry.get()
        output_file = self.output_entry.get()
        
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
        
        # Create a mask with the same size as the image, filled with zeros (black)
        mask = np.zeros(image.shape, np.uint8)
        
        # Draw the largest contour on the mask
        cv2.drawContours(mask, [largest_contour], -1, (255, 255, 255), -1)
        
        # Convert the mask to grayscale
        mask_gray = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
        
        # Apply thresholding to the mask to create a black and white mask
        _, mask_thresh = cv2.threshold(mask_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        
        # Create a 3-channel mask with white pixels in the areas where the mask is white
        mask_3_channel = cv2.cvtColor(mask_thresh, cv2.COLOR_GRAY2BGR)
        
        # Multiply the mask by the image to keep only the pixels of the image where the mask is white
        result = cv2.bitwise_and(image, mask_3_channel)
        
        # Save the result to the output file
        cv2.imwrite(output_file, result)

        # Create the root window
        root = tk.Tk()

        # Set the size and position of the window
        root.geometry("500x200+300+300")

        # Create an instance of the App class
        app = App(root)

        # Run the Tkinter event loop
        root.mainloop()

        