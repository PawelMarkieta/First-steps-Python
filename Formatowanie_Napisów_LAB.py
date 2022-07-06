helloMessage = "Hello %s!"
print(helloMessage %("Kate"))
print(helloMessage %("Chris"))

helloMessage = "Hello {0:s}!"
print(helloMessage.format("Chris"))
print(helloMessage.format("Kate"))

helloMessage = "%s has %d %s"
print(helloMessage %("Kate", 1, "animal"))
print(helloMessage %("Chris", 100000, '$'))

helloMessage = "{0:s} has {1:d} {2:s}"
print(helloMessage.format("Kate", 1, "animal"))
print(helloMessage.format("Chris", 100000, '$'))

line = '{0:20s} costs {1:6d} €'
print(line.format('ice cream', 3))
print(line.format('trip to venice', 119))
print(line.format('Pizza Hawai', 6))

line = '{0:s} {1:d}'
print(line.format('ice cream', 3))
print(line.format('trip to venice', 119))
print(line.format('Pizza Hawai', 6))