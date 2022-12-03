from tkinter import filedialog, messagebox
from tkinter import *
from PyPDF2 import PdfFileMerger

# create a tkinter window
root = Tk()
root.title("PDF Combiner")

# create a function that combines multiple PDFs
def combine_pdfs():
  # get the list of selected PDF files
  files = filedialog.askopenfilenames(title="Select PDFs to Combine", filetypes=[("PDF Files", "*.pdf")])
  # create a PdfFileMerger object
  merger = PdfFileMerger()
  # loop through the selected PDF files and add them to the merger
  for file in files:
    merger.append(file)
  # save the combined PDF
  merger.write("combined_pdf.pdf")
  # display a message to let the user know that the PDFs were combined
  messagebox.showinfo("Success", "PDFs were combined successfully!")

# create a button that will trigger the PDF combining function
combine_button = Button(root, text="Combine PDFs", command=combine_pdfs)
combine_button.pack()

# start the GUI
root.mainloop()