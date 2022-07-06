message1 = 'Processing file %s'
print(message1 % ('file_1.txt'))

message2 = 'File %s has size %d KB' #%s rezerwuje miejsce dla stringów, a %d dla liczb(descimal)
print(message2 %('file.txt', 100))

message3 = ('File %20s has size %10d KB') #to samo co wyżej tylko rezerwujemy przy tym ilość znaków
print(message3 %('file.txt', 100))

message4 = 'Processing file {0:s}' #robi to samo co to wyżej czyli oczekuje parametru który ma być napisem
print(message4.format('file.txt'))

message5 = 'File {0:s} has size {1:d}'
print(message5.format('file.txt',100))

message5 = 'File {1:s} has size {0:d}'#poniekąd w tej metodzie możemy zamieniać parametry które są podawane wcześniej w metodzie format
print(message5.format(100, 'file.txt'))

message6 = 'File {0:20s} has size {1:10d}'
print(message6.format('file.txt',100))