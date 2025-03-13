import os
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
                print("here")
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
    
    def html_to_pdf(self, html, pdf):
        self.page = QtWebEngineWidgets.QWebEnginePage()
        self.page.pdfPrintingFinished.connect(self.handle_print_finished)
        self.page.loadFinished.connect(lambda status: self.handle_load_finished(status, pdf))
        self.page.load(QtCore.QUrl.fromLocalFile(html))
    
    def handle_print_finished(self, filename, status):
        print(f"Saved Report as PDF To: {filename}, Status: {status}")

    def handle_load_finished(self, status, pdf):
        if status:
            self.page.printToPdf(pdf)
        else:
            print("Failed to Save Report as PDF")
        



    
