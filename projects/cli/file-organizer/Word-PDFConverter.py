import os, sys
import getopt 

def convert_word_to_pdf(word_file, pdf_file):
    try:
        from docx2pdf import convert
    except ImportError:
        print("The 'docx2pdf' library is not installed. Please install it using 'pip install docx2pdf'.")
        sys.exit(1)

    try:
        convert(word_file, pdf_file)
        print(f"Successfully converted '{word_file}' to '{pdf_file}'")
    except Exception as e:
        print(f"An error occurred during conversion: {e}")

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:],'w:o:')
    except getopt.GetoptError:
        print("Usage: python Word-PDFConverter.py -w inputfolder -o outputfolder")
        sys.exit(1)

    for opt, arg in opts:
        if opt == '-w':
            inputfolder = arg
        elif opt == '-o':
            outputfolder = arg
    
    if not os.path.exists(inputfolder):
        print(f"{inputfolder} not exist.")
        sys.exit(2)

    if not os.path.exists(outputfolder):
        os.makedirs(outputfolder)

    counter = 0
    
    for filename in os.listdir(inputfolder):
        if filename.lower().endswith('.docx'):
            f1 = os.path.join(inputfolder, filename)
            f2 = os.path.join(outputfolder, filename[:-5] + ".pdf")
            convert_word_to_pdf(word_file = f1, pdf_file = f2) 
            counter += 1
    print(f"Converted {counter} files.")

                        
            
    


if __name__ == "__main__":
    main()