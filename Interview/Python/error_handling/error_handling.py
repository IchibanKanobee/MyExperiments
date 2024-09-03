try:
    f = open("snippet.txt", "r")
#    var = bad_var
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
finally:
    print("Executing finally")
