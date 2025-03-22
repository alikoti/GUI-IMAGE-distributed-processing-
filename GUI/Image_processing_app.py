import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import requests

# Flask API Base URL
API_URL = "http://192.168.0.125:80/process"

# List of available filters
FILTERS = [
    "Grayscale", "Gaussian Blur", "Edge Detection", "Histogram Equalization", 
    "Unsharp Masking", "Median Filter", "Bilateral Filter", "Sobel Filter", 
    "Canny Edge Detection", "Dilation", "Erosion", "Fourier Transform", 
    "Sepia Tone", "Cartoon Effect", "Oil Painting Effect"
]

class ImageFilterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Filter App")
        self.root.geometry("600x550")

        self.file_path = None  # Store uploaded image path

        # Upload Button
        self.upload_button = tk.Button(root, text="Upload Image", command=self.upload_image, font=("Arial", 12))
        self.upload_button.pack(pady=10)

        # Filter Selection Dropdown
        self.selected_filter = tk.StringVar(root)
        self.selected_filter.set(FILTERS[0])  # Default filter
        self.filter_menu = tk.OptionMenu(root, self.selected_filter, *FILTERS)
        self.filter_menu.pack(pady=10)

        # Apply Filter Button
        self.apply_button = tk.Button(root, text="Apply Filter", command=self.apply_filter, font=("Arial", 12), state=tk.DISABLED)
        self.apply_button.pack(pady=10)

        # Image Label
        self.image_label = tk.Label(root, text="Selected Image", font=("Arial", 10))
        self.image_label.pack(pady=5)

        # Display Image
        self.image_panel = tk.Label(root)
        self.image_panel.pack(pady=5)

        # Processed Image Label
        self.processed_label = tk.Label(root, text="Processed Image", font=("Arial", 10))
        self.processed_label.pack(pady=5)

        # Processed Image Display
        self.processed_panel = tk.Label(root)
        self.processed_panel.pack(pady=5)

    def upload_image(self):
        """Allow user to upload an image and enable Apply button."""
        self.file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if not self.file_path:
            return

        self.display_image(self.file_path, self.image_panel)
        self.apply_button.config(state=tk.NORMAL)  # Enable apply button

    def apply_filter(self):
        """Send request to backend to apply selected filter."""
        if not self.file_path:
            messagebox.showerror("Error", "Please upload an image first.")
            return

        selected_filter = self.selected_filter.get()  # Get chosen filter

        try:
            files = {'file': open(self.file_path, 'rb')}
            headers  = {'filter': selected_filter}  # Send filter choice
            response = requests.post(API_URL, files=files, headers =headers)
            print(headers)

            if response.status_code == 200:
                output_path = "processed_image.png"
                with open(output_path, 'wb') as f:
                    f.write(response.content)
                
                self.display_image(output_path, self.processed_panel)
            else:
                messagebox.showerror("Error", "Failed to process image.")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")

    def display_image(self, path, panel):
        """Resize and display an image in the given panel."""
        img = Image.open(path)
        img.thumbnail((250, 250))
        img = ImageTk.PhotoImage(img)
        panel.config(image=img)
        panel.image = img

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageFilterApp(root)
    root.mainloop()

