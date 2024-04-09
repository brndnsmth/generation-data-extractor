import os
from PIL import Image
from tqdm import tqdm


# Extracts parameter and additional metadata from the given image file and returns it
def extract_generation_metadata(image_path):
    try:
        with Image.open(image_path) as img:
            metadata = img.info
            return metadata
    except Exception as e:
        print(f"Error extracting metadata from {image_path}: {e}")
        return None


# Process image files and export to txt files
def export_generation_metadata_to_text(image_dir):
    # Get list of image files in the directory
    image_files = [
        filename
        for filename in os.listdir(image_dir)
        if filename.endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif"))
    ]
    # Iterate over each image file and extract parameters metadata
    for filename in tqdm(image_files, desc="Extracting Metadata"):
        image_path = os.path.join(image_dir, filename)
        metadata = extract_generation_metadata(image_path)
        if metadata:
            txt_filename = os.path.splitext(filename)[0] + ".txt"
            with open(os.path.join(image_dir, txt_filename), "w") as f:
                for key, value in metadata.items():
                    f.write(f"{key}: {value}\n")
        else:
            print(f"Skipping {filename} due to extraction error")


if __name__ == "__main__":
    image_directory = "images"
    export_generation_metadata_to_text(image_directory)
