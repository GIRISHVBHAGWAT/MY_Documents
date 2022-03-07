import io
file = io.open("om.txt",'r',encoding='utf8')
file_read = file.readlines()
file.close()

Write_file = io.open("written_code",'a',encoding='utf8')
for line in file_read:
    Write_file.write("<p>"+line[:-1]+"</p>\n")
else:
    Write_file.close()

    