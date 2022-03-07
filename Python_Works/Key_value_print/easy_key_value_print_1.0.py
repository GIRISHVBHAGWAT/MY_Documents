


def writing_file(file,key,value):
    import io
    dictwr=io.open(file,'a',encoding='utf8')
    dictwr.write(f"\n{key} --- {value}")
    dictwr.close()


listkanw=[]
listsanw=[]
while(True):
    kanwin=input(" Key: ")
    if kanwin == "":
        break
    sanwin=input("Value: ")
    if sanwin == "":
        break
    writing_file("shishupalvadha.txt",kanwin,sanwin)

      
      
      

