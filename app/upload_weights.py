import roboflow
import os

# Replace with your actual API key
rf = roboflow.Roboflow(api_key="YwdlSzgRUOWdsymwDzw8")
project = rf.workspace().project("gaitar")  # Replace with your project ID

# Specify the directory where your images and annotations are located
data_directory = "images"  # Update this to your actual data directory


# Loop through each file in the data directory
for filename in os.listdir(data_directory):
    if filename.endswith(('.jpg', '.jpeg', '.png')):  # Check if the file is an image
        image_path = os.path.join(data_directory, filename)

        # Upload the image
        project.upload(image_path)

        # Annotations should be uploaded automatically if they are correctly formatted and named
        # Ensure that annotation files are in the same directory and named correctly (e.g., image1.txt for image1.jpg)

print("Upload complete!")


'''
# Loop through each file in the data directory
for filename in os.listdir(data_directory):
    if filename.endswith(('.jpg', '.jpeg', '.png')):  # Check if the file is an image
        image_path = os.path.join(data_directory, filename)

        # Upload the image
        project.upload(image_path)

        # Prepare the corresponding annotation filename
        annotation_filename = filename.replace('.jpg', '.txt').replace('.jpeg', '.txt').replace('.png', '.txt')
        annotation_path = os.path.join(data_directory, annotation_filename)

        # Check if the annotation file exists and upload it if it does
        if os.path.exists(annotation_path):
            with open(annotation_path, 'r') as file:
                annotations = file.read()
            # Note: The following method is a placeholder; adjust it based on Roboflow's SDK capabilities
            project.upload_annotation(annotation_path)

print("Upload complete!")
'''