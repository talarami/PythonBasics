import mathModule
import importlib # pozwala zaimportować kilkukrotnie

print( mathModule.addNumbers(10, 2) ) # 12
print( "prog.py: " + __name__ ) # prog.py: __main__, główny program który jest wywoływany zawsze będzie miał wartość main globalnej zmiennej __name__

importlib.reload(mathModule) # mathModule random int:  39
importlib.reload(mathModule) # mathModule random int:  49
importlib.reload(mathModule) #mathModule random int:  78
