global_var = 1
global inner_var
inner_var = 3
def my_vars () :
    print ( 'Global Variable: ' , global_var )
local_var = 2
print ( 'Local variable:' , local_var )
my_vars ()
print ( 'Coerced Global:' , inner_var )
