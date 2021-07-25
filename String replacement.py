#string replacement
def String(original,substring,replace):
    
    for i in range(len(original)):
        if(original[i]==substring):
            original[i]=replace
    for x in original:
        print(x,end=' ')
original=input('enter the string').split(' ')
substring=input('enter the substring')
replace=input('enter string to be replaced')
String(original,substring,replace)
