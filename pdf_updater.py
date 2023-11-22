# # Importing necessary modules
# import sys
# sys.path.insert ##
# pdf_output_path = # Path for generated pdfs

# import user_input

# import datetime
# from random import randint
# from PyPDF2 import PdfReader, PdfWriter
# from watchdog.observers import Observer
# from watchdog.events import FileSystemEventHandler
# import os

# class MyHandler(FileSystemEventHandler):
#     def __init__(self, pdf_template_path, pdf_output_path):
#         self.pdf_template_path = pdf_template_path
#         self.pdf_output_path = pdf_output_path
#         self.field_data = {}
#         self.invoice_number = ""
#         self.current_date = ""

#     def update_pdf(self):
#         try:
#             with open(self.pdf_template_path, "r") as file:
#                 lines = file.readlines()

#             for line in lines:
#                 key, value = line.strip().split('=')
#                 self.field_data[key.strip()] = value.strip()

#             self.invoice_number = self.field_data.get("invoiceNumberValue", ''.join([str(randint(0, 9)) for _ in range(9)]))
#             self.current_date = self.field_data.get("dateFieldValue", datetime.datetime.now().strftime("%d/%m/%Y")).replace('/', '-')

#             pdf_output_path = fr"{self.pdf_output_path}_{self.invoice_number}_{self.current_date}.pdf"

#             pdf = PdfReader(self.pdf_template_path)
#             pdf_writer = PdfWriter()

#             for page in range(len(pdf.pages)):
#                 pdf_page = pdf.pages[page]
#                 pdf_writer.add_page(pdf_page)

#                 if "/Annots" in pdf_page:
#                     for field in pdf_page["/Annots"]:
#                         field_name = field.get_object()["/T"]
#                         if field_name in self.field_data:
#                             field.get_object().update({
#                                 NameObject("/V"): self.field_data[field_name]
#                             })

#             with open(pdf_output_path, "wb") as output_pdf:
#                 pdf_writer.write(output_pdf)
#         except Exception as e:
#             print(f"An error occurred while updating the PDF: {e}")

#     def print_pdf(self):
#         # Implement logic to print the updated PDF if necessary
        
#         pass

# if __name__ == "__main__":
#     try:
#         # Collect user inputs and update the file first
#         data = user_input.collect_user_inputs()
#         file_path = r' # Template Path\pdf_fill.txt"  # Corrected file path
#         user_input.update_file(data, file_path)
#         print("File has been successfully updated with user inputs.")

#         # PDF processing logic starts here
#         pdf_template_path = r"# Template Path\sticker_template.pdf"
#         pdf_output_path = r"# Template Path\output"

#         event_handler = MyHandler(pdf_template_path, pdf_output_path)
#         observer = Observer()
#         observer.schedule(event_handler, r"# Template Path", recursive=True)
#         observer.start()
        
#         try:
#             while True:
#                 pass
#         except KeyboardInterrupt:
#             observer.stop()
#             observer.join()
#     except Exception as e:
#         print(f"An error occurred in the main process: {e}")
