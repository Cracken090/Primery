day = 32
try :
    if day > 31 :
        raise ValueError ( 'Invalid Day Number' )
except ValueError as msg :
        print ( 'The Program found An' , msg )
nfinally :
            print ( 'But Today Is Beautiful Anyway.' )
