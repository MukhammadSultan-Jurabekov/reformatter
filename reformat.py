from docx import Document
import pdfkit
from fpdf import FPDF
from PIL import Image
import pdf2image
from pptx import Presentation
import pandas as pd
import os

def word_to_pdf(docx_path, pdf_path):
    pdfkit.from_file(docx_path, pdf_path)

def txt_to_pdf(txt_path, pdf_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    with open(txt_path, 'r') as file:
        for line in file:
            pdf.cell(200, 10, txt=line.encode('latin-1', 'replace').decode('latin-1'), ln=True)
    
    pdf.output(pdf_path)

