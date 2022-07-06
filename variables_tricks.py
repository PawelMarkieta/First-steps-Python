# W pythonie wcale nie trzeba deklarować typów
# zmiennych, sam postara się wybrać dla zmiennej najbardziej odpowiedni typ

Title = 'Python'
print('title is', type(Title))

Version = 3
print('Version is', type(Version))

Progress = 0.21
print('Progres is', type(Progress))

#niektóre typy są silniejsze a niektóre słabsze, poniżej z mnożenia float i int
# wychodzi wynik float ponieważ jest typem obszerniejszym
print('this expression is', type(Progress * Version))

x = 1
y = 1
z = 1
print(x,y,z)
# to co wyżej można zrobić też w ten sposób (całkiem wygodne)
a=b=c=2
print(a,b,c)
#jeżeli chodzi o zadania matematyczne to w pythonie wszystko dzieje się tak jak
# w ogólnie przyjętych zasadach matematyki czyli np:
print(2+2*2) # = 6 czyli tak jak to powinno wychodzić biorąc pod uwagę kolejność wykonywania
            # działań

print(6/2 * (1+2))

print(4**3**2)


v1 = 126
v2 = '126'
v3 = 126.0
v4 = '126.0'
print('v1 is', type(v1))
print('v2 is', type(v2))
print('v3 is', type(v3))
print('v4 is', type(v4))
print('v1 + v3 is', v1+v3, 'and the type is:',type(v1+v3))
print('v2 + v4 is', v2+v4, 'and the type is:',type(v2+v4))

print('7-1*0+3+3 = ', 7-1*0+3+3)
print(4**5/2**3) #ile to jest 4 do potęgi piątej podzielone przez 2 do potęgi 3

print(99+9/9)




