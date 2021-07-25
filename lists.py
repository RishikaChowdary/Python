#lists
val=[]
while True:
    print('1.insert')
    print('2.update')
    print('3.delete')
    print('4.show')
    print('5.exit')
    commands=input('enter your choice:').split(' ')
    cmd=commands[0].lower()
    if(cmd=='insert'):
        print('you selected "insert" command')
        if(len(commands)==2):
            val.append(commands[1])
        if(len(commands)==3):
            val.insert(int(commands[1],commands[2])
        else:
            ex_list=list(commands[1:])
            val.extend(ex_list)
            print('value inserted successfully')
    elif(cmd=='update'):
        print('you selected "update" command')
        val[0]=10
    elif(cmd=='delete'):
        print('you selected "delete" command')
        if(len(commands)==2):
            val.pop()
        if(len(commands)>2):
            val.remove(int(commands[1]))
    elif(cmd=='show'):
        print('you selected "show" command')
        for i in value:
            print(i,end=' ')
    elif(cmd=='exit'):
        print('exit')
        
    
