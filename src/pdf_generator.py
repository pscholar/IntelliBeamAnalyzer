import os
import sys
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
from abstractclasses.abstract_pdf_generator import AbstractPDFGenerator

class PDFGenerator(AbstractPDFGenerator):

    def generate_pdf(self, content: str = None, file_name: str = None, 
                     format_flag: str = 'html',output_pdf: str = None) -> str:
        if format_flag == 'html':
            if content:
                temp_html_path = self.save_content_to_temp_file(content, 'html')
                self.html_to_pdf(temp_html_path, output_pdf)
            elif file_name:
                current_dir = os.path.dirname(os.path.realpath(__file__))
                file_name = os.path.join(current_dir, file_name)
                self.html_to_pdf(file_name, output_pdf)
            else:
                raise ValueError("Either content or file_name must be provided"
                " for HTML format.")
        else:
            raise ValueError(f"Unsupported format: {format_flag}")
        return output_pdf

    def save_content_to_temp_file(self, content: str, extension: str) -> str:
        temp_file_path = os.path.join(os.path.dirname(__file__), f"temp.{extension}")
        with open(temp_file_path, 'w') as f:
            f.write(content)
        return temp_file_path
    
    def html_to_pdf(self,html, pdf):
        page = QtWebEngineWidgets.QWebEnginePage()
        def handle_print_finished(filename, status):
            print("Saved Report as PDF To: ", filename, status)
        def handle_load_finished(status):
            if status:
                page.printToPdf(pdf)
            else:
                print("Failed to Save Report as PDF")
        page.pdfPrintingFinished.connect(handle_print_finished)
        page.loadFinished.connect(handle_load_finished)
        page.load(QtCore.QUrl.fromLocalFile(html))
        



    
