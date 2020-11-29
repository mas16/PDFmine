import fitz
import os
from pathlib import Path

directory = os.getcwd()
pdf_file = "test.pdf"
pdf_path = Path(directory, pdf_file)

pdf = fitz.open(pdf_path)
test = pdf[-2].getText('xml')
print(test)