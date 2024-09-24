import pandas as pd
import tkinter as tk
from tkinter import filedialog

# Create a Tkinter root window (it will not be displayed)
root = tk.Tk()
root.withdraw()

# Open a file dialog to select multiple Excel files
file_paths = filedialog.askopenfilenames(
	title="Select Excel files",
	filetypes=[("Excel files", "*.xlsx *.xls")]
)

# Check if any files were selected
if file_paths:
	# Iterate over the selected files and read each one into a DataFrame
	for file_path in file_paths:
		df = pd.read_excel(file_path)
		# Display the content of the DataFrame
		print(f"Contents of {file_path}:")
		print(df)
else:
	print("No files selected.")
