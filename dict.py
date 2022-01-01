dict = { 'name' : 'bob' , 'ref' : 'Python' , 'sys' : 'Win' }
print ( 'Dictonary:' , dict )
print ( '\nReference:' , dict[ 'ref' ] )
print ( '\nKeys:' , dict.keys() )
del dict[ 'name' ]
dict[ 'user' ] = 'Tom'
print ( '\nDictonary:' , dict )
print ( '\nIs There A name key?:' ,'name' in dict )
