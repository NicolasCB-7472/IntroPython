import zipfile
# import pathlib, it also works for different OS

def make_archive(source, destination):
    source_list = source
    with zipfile.ZipFile(destination + "/" + "mycompression.zip", 'w') as archive:
        for single_file in source_list:
            source_list = single_file
            source_header = parse_path(str(source_list))
            archive.write(source_list, arcname=source_header)
    print("File compressed!")

def parse_path(filepath : str):
    length = len(filepath)

    filepath = filepath.replace("/", " ",  length)      
    if length > 0:
        header = ""
        aux = 0

        if(filepath[length-1] != '/' ):
            # File case
            while((length - aux >= 0) and (filepath[length - aux - 1] != " ")):
                header = str(header) + str(filepath[length-aux - 1])
                aux = aux + 1
            header = header[::-1]
            filepath = header
        else:
            print("Folders compressions are not supported, this error message should not be readable given files input library")
            # Folder case
            # The program is only set to check for files, was not meant to compress folders as well in the course example
            # In the spirit of not departing from the original example code, I won't implement it.
            # Any how, it should be considering changing input format in GUI, and in parsing dir aux=1 for the second '/' in '/example/'   
    else:
        filepath = ""
    
    return filepath

