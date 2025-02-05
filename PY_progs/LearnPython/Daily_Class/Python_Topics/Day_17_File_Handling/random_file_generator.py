import os
import random

list_of_extensions=[".docx", '.py', '.exe','.bat','.pptx','.pdf', '.html','.css','.rs','.xml','.js', '.txt','.c','.cpp','.cs','.jpg,','.jpeg','.png', '.sln','.csproj','.mp3','.mov','.mp4','.toml','.lua',]

os.chdir('D:/Downloads/File_handling_Sample')
os.getcwd()
for i in range(1,1000001):
    fh = open(f"LMAO_GET_REKT{i}{random.choice(list_of_extensions)}",'w')
    print(f"File Created at D:/Downloads/File_handling_Sample{i}")
    fh.close()  
