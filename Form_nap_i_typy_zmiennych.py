name = 'Paweł'
age = 26
daysInYear = 365

message = '{0:s} is {1:d} years old, so is about {2:d} days old'
print(message.format(name, age, (age * daysInYear)))

name = 'Zbyszek'
age = 57
daysInYear = 365

message = '{0:s} is {1:d} years old, so is about {2:d} days old'
print(message.format(name, age, (age * daysInYear)))

message = '{0:s} is {1:d} years old, so is about {2:d} days old'
print(message.format("Chris", 17, (17 * daysInYear)))

print('1234567890 divided by 12345 is ',1234567890 // 12345,'and the rest is', 1234567890 % 12345)
