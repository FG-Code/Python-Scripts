"""Fizz Buzz"""

for i in range(1, 101):
    
    var = ''
    
    if i % 3 == 0:
        var = var + 'Fizz'

    if i % 5 == 0:
        var = var + 'Buzz'

    if i % 7 == 0:
        var = var + 'Biff'
    
    if var != '':
        print(var)
        
    else:
        print(i)
