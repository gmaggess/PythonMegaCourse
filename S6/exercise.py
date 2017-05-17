import datetime
filename = datetime.datetime.now().strftime('%y-%m-%d-%H-%M-%S')+'.txt'

def merge_files():
  with open(filename, "w") as file:
    f1 = open('./Sample-Files/file1.txt', 'r');
    file.write(f1.readline())
    file.write('\n')
    f2 = open('./Sample-Files/file2.txt', 'r');
    file.write(f2.readline())
    file.write('\n')
    f3 = open('./Sample-Files/file3.txt', 'r');
    file.write(f3.readline())
    file.write('\n')

merge_files()