import xy

while True:
    input_var = input("xy > ")
    result, error = xy.run('<stdin>',input_var)

    if error: print(error.as_string())
    elif result: print(repr(result))