userInput = input ( "Enter a tuple:" )
x = map ( lambda x : len ( x ) , tuple ( x . strip ( ) for x in userInput . split ( ',' ) ) )
print ( list ( x ) )
