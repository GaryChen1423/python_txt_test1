with open("test1.txt","w") as f:
    f.write('aef124rf342ealjkferin')
ft = open("test1.txt", "r+")
fileaString = ft.read()
search = 'f124'
addaddress = fileaString.find(search)
ft.seek(addaddress,0)
ft.write('NICE')  
ft.close()
