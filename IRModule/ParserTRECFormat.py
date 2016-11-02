
def parser(replies):
    file = open("repliesTRECFormat.txt", "w")

    cont = 1
    fileread = open(replies, 'r')
    for line in fileread:

        content = line[0:-2]
        file.write("<DOC> \n")
        file.write("<DOCNO> " + str(cont) +" </DOCNO> \n")
        file.write(content + "\n")
        file.write("</DOC>")
        file.write("\n")
        cont +=1

    fileread.close()
    file.close()

if __name__ == '__main__':
   parser()