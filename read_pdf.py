from pathlib import Path
from PIL import Image
import fitz


def pdf_extract_images(path_to_files: str):
    path_to_files = Path(path_to_files)  # convert the str to a pathlib object

    for pdf_file in path_to_files.rglob('*.pdf'):
        pdf = fitz.open(pdf_file)
        # extract images in pdf
        for pageNumber, page in enumerate(pdf.pages(), start = 1):
            for imgNumber, img in enumerate(page.getImageList(), start = 1):
                xref = img[0]
                pix = fitz.Pixmap(pdf, xref)
                # pix.n = bytes per pixel
                if pix.n < 5: # this is GRAY or RGB
                    pix.pillowWrite(f'./output_images/image_Page{pageNumber}_{imgNumber}.jpg')
                else:
                    pix1 = fitz.open(fitz.csRGB, pix)
                    pix1.pillowWrite(f'./output_images/image_Page{pageNumber}_{imgNumber}.jpg')
                    pix1 = None
                pix = None


# path to files
path_to_files = r'B:\Research\blah7_hackathon\papers'

pdf_extract_images(path_to_files)