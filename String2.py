#konkatenacja napisów czyli łączenie(dodawanie) kilku stringów w jeden
#aby python dobrze czytał w stringach "\"" trzeba zrobić podwójy "\\"
#lub przed stringiem możemy napisać "r" i będzie brał dosłownie np. r"dosłownie\zadziała"
#znak \ służy również do brania dosłownie ' lub " w tekście(niezależnie w czym go piszemy)
drive = 'c:\\'
folder = 'scripts\\python\\'
file = 'myscript.py'

path = drive + folder + file

print(path)
justText = r'bla bla bla\tak to działa'
input('coś')