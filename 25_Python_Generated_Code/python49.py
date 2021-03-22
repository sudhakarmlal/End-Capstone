import re
str1 = 'count001'
res = re . sub ( r'[0-9]+$' ,
lambda x : f"{str(int(x.group())+1).zfill(len(x.group()))}" , str1 )
print ( "Incremented numeric String : " + str ( res ) )
