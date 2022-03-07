import io
Open_file = io.open("sabhapooje.txt",'r',encoding='utf8')
Read_file = Open_file.readlines()

Write_File = io.open("sabhapooje_breaken_code.txt","a",encoding='utf8')


for lines in Read_file:
    Write_File.write(lines[:-1]+"<br />\n")
else:
    Write_File.close()


