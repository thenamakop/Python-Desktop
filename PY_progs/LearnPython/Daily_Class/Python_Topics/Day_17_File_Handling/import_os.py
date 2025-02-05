from os import chdir, getcwd, mkdir

chdir("D:/Downloads")
print(getcwd)
mkdir("File_handling_Sample")
chdir("D:/Downloads/File_handling_Sample")
print(getcwd)
for i in range(1, 101):
    mkdir(f"Namak {i}")
    print(f"Namak {i} Created")
