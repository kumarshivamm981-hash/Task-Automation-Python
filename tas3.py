import os
import shutil

destination_folder = "moved_images"

# Destination folder create kare
os.makedirs(destination_folder, exist_ok=True)

jpg_found = False

# Current directory ki sab files check kare
for file_name in os.listdir():
    if file_name.lower().endswith(".jpg"):
        shutil.move(file_name, os.path.join(destination_folder, file_name))
        print(f"Moved: {file_name}")
        jpg_found = True

if not jpg_found:
    print("No JPG files found in the current folder.")

print("Task completed successfully!")
