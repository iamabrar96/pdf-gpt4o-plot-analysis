import fitz  # PyMuPDF
import io
import os
from PIL import Image

# STEP 2
# file path to pdf you want to extract images from
file_path = ""

# extract the PDF file name without extension and create a directory
pdf_name = os.path.splitext(os.path.basename(file_path))[0]
output_dir = os.path.join(os.getcwd(), pdf_name)

# create the directory if it does not exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# open the file
pdf_file = fitz.open(file_path)

# STEP 3
# iterate over PDF pages
for page_index in range(len(pdf_file)):

    # get the page itself
    page = pdf_file[page_index]
    image_list = page.get_images(full=True)

    # printing number of images found in this page
    if image_list:
        print(f"[+] Found a total of {len(image_list)} images in page {page_index}")
    else:
        print("[!] No images found on page", page_index)

    for image_index, img in enumerate(image_list, start=1):

        # get the XREF of the image
        xref = img[0]

        # extract the image bytes
        base_image = pdf_file.extract_image(xref)
        image_bytes = base_image["image"]

        # get the image extension
        image_ext = base_image["ext"]

        # load it to PIL
        image = Image.open(io.BytesIO(image_bytes))

        # save the image in the created directory
        image_filename = os.path.join(output_dir, f"image_page{page_index + 1}_img{image_index}.{image_ext}")
        image.save(image_filename)
        print(f"Saved: {image_filename}")