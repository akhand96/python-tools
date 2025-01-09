# importing the required libraries
import gzip
import shutil

# creating a function to compress given file using gzip
def compressFile(inputFile, outputFile):
    with open(inputFile, 'rb') as f_in:
        with gzip.open(outputFile, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

# setting the input and  output path
input_path = input("Enter the path of file to be compressed: ")
output_path = 'compressed_output_file.pdf.gz' # replace the .pdf with your actual file format

# calling the function to compress the file
compressFile(input_path, output_path)

