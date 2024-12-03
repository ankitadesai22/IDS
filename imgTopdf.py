import os
import img2pdf

def convert_jpg_to_pdf():
    try:
        # Ask user for the path to the folder or image file
        input_path = input("Enter the path to the JPG file or folder containing JPGs: ").strip()

        # Check if the input is a file or directory
        if os.path.isfile(input_path) and input_path.lower().endswith(".jpg"):
            # Single JPG file
            image_files = [input_path]
        elif os.path.isdir(input_path):
            # Directory containing multiple JPGs
            image_files = [os.path.join(input_path, f) for f in os.listdir(input_path) if f.lower().endswith(".jpg")]
            if not image_files:
                print("No JPG files found in the directory.")
                return
        else:
            print("Invalid path. Please provide a valid JPG file or folder path.")
            return

        # Ask the user for the output PDF file name
        output_pdf = input("Enter the name for the output PDF file (without extension): ").strip() + ".pdf"

        # Convert the images to a PDF
        with open(output_pdf, "wb") as pdf_file:
            pdf_file.write(img2pdf.convert(image_files))

        print(f"Successfully converted to PDF: {output_pdf}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    convert_jpg_to_pdf()
