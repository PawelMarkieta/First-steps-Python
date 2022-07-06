# == czy jest równe (is equal
# > czy jest większe niż (greater than)
# >= czy jest większe bądź równe(greater or equal)
# != czy jest różna (not equal)

'''IsWeekend = False
print('Is weekend = ', IsWeekend)

Temperature = 25
print('Temperature =', Temperature)

ToDoList = "Shopping"
print('ToDoList =', ToDoList)

IsHappy = IsWeekend and Temperature >= 20 and ToDoList == '' \
or not IsWeekend and Temperature < 20 and ToDoList != '' \
or not IsWeekend and Temperature >= 20 and ToDoList != ''
print('IsHappy =', IsHappy)'''


isAutomaticMode = False
print("Automatic mode:   ",isAutomaticMode)
is80PercentLight = True
print("Is the light good:",is80PercentLight)
isDirectLight = False
print("Is sun low:       ",isDirectLight)
isRainy = True
print("Is it rainy:      ",isRainy)

turnLightsOn = isAutomaticMode and (not is80PercentLight or isDirectLight or isRainy)
print("TURN LIGHTS ON:   ",turnLightsOn)






