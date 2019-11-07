import glob

def makeTalkList():
    path = "talk/*"
    file_list = glob.glob(path)
    return file_list

def readTalk(file_list):
    for file in file_list:
        f=open(file, encoding='utf8')
        #matrix=[list(map(int,line.rstrip().replace("–","-").split(" "))) for line in file]
        print(f.readline())   
    return

readTalk(makeTalkList())