s = 'Röd'
print( '\nRed String:' , s )
print( 'Type:' , type( s ) , '\tLenght:' , len( s ) )
s = s.encode( 'utf-8' )
print( '\nEncodedString:' , s )
print( 'Type:' , type( s ) , '\tLenght:' , len( s ) )
s = s.decode( 'utf-8' )
print( '\nDecoded String:' , s )
print( 'Type:' , type( s ) , '\tLenght:' , len( s ) )
import unicodedata
for i in range( len( s ) ):
    print( s[ i ] , unicodedata.name( s[ i ] ) , sep = ' : ' )
s = b'GR\xc3\xb6n'
print( '\nGreen String:' , s.decode( 'utf-8' ) )
s = 'Gr\N{LATIN SMALL LETTER O WITH DIAERESIS}n'
print( 'Green String:' , s )