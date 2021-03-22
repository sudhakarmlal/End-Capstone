test_str = 'Gfg is best . Geeks are good and Geeks like Gfg'
print ( "The original string is : " + str ( test_str ) )
res = { key : test_str . count ( key ) for key in test_str . split ( ) }
print ( "The words frequency : " + str ( res ) )
