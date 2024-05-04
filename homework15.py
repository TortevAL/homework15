def test_function(x):
    d = x ** 2

    def inner_function(x):
        if d % 2 == 0:
            print('Я в области видимости функции test_function')
        else:
            print('ok')

    inner_function(x)
    return d

b = test_function(8)
print(b)
inner_function()