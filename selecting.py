import cgi
import cgitb
cgitb.enable()

data = cgi.FieldStorage()
if data.getvalue('CityList'):
    city = data.getvalue('CityList')
else:
    city = 'Not entered'
print( 'Content-type:text/html\r\n\r\n' )
print( '<!DOCTYPE HTML>' )
print( '<html lang="en">' )
print( '<head>' )
print( '<meta charset="UTF-8">' )
print( '<title>Python Response</title>' )
print( '</head>' )
print( '<body>' )
print( '<h1>City:', city , '</h1>' )
print( '<a href="selecting.html">Back</a>' )
print( '</body>' )
print( '</html>' )