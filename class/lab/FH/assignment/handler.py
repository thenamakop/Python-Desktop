def Read_File_Contents(path):
    with open(path,'r') as fh:
        return fh.read()