s = "python"
type(s)
a= s.upper()
a =s.lower()
print(a)

b = "abrakadabra"
print(b.count("ra"))

c = "abrakadabra"
print(c.count("ra", 4)) #будет искать ra с четвертого индекса в строке

d = "abrakadabra"
print(d.count("ra", 4, 10)) #будет искать ra с четвертого индекса в строке до 10, 10 не учавствует в поиске

print(b.find("br")) #будет искать первое вхождение  br в строке

print(b.find("br",2 )) #будет искать вхождение начиная со второго индекса br в строке. Поиск осуществляется слева направо

print(b.rfind("br")) #будет искать вхождение начиная со второго индекса br в строке. Поиск осуществляется справо налево

print(b.replace("a", "o")) # заменят все буквы 'a', на 'o'

print(b.isalpha()) # вернет тру если строка состоит из букв и фолс если нет

q = "Иванов Иван Иванович" # этот метод разбивает строку в список из строк
print(q.split())

t = "1,2,3 , 4,5,6 ,7 ,8"
m = t.replace(" "," ").split(",")
print(m)
print(", ".join(m))


# len(): Это функция, а не метод, но она часто используется для работы со строками.
# Она возвращает длину строки, то есть количество символов в строке. Например:
message = "Привет, мир!"
length = len(message)
print(length)  # Вывод: 13

# lower(), upper(): Эти методы позволяют преобразовать все символы строки в нижний
# (lower()) или верхний (upper()) регистр соответственно. Например:
message = "Hello, World!"
lowercase = message.lower()
uppercase = message.upper()
print(lowercase)  # Вывод: hello, world!
print(uppercase)  # Вывод: HELLO, WORLD!

#count(): Этот метод позволяет подсчитать количество вхождений заданной подстроки в строке. Например:
message = "Hello, World!"
count = message.count("o")
print(count)  # Вывод: 2

# find(), index(): Эти методы позволяют найти первое вхождение заданной подстроки в строке.
# Разница между ними заключается в том, что find() возвращает индекс первого вхождения или -1,
# если подстрока не найдена, а index() вызывает исключение ValueError, если подстрока не найдена. Например:

message = "Hello, World!"
index = message.find("World")
print(index)  # Вывод: 7

index = message.index("World")
print(index)  # Вывод: 7

# replace(): Этот метод позволяет заменить все вхождения одной подстроки на другую подстроку в строке. Например:
message = "Hello, World!"
new_message = message.replace("World", "Python")
print(new_message)  # Вывод: Hello, Python!

#split(): Этот метод разделяет строку на список подстрок, используя заданный разделитель. Например:
message = "Hello, World!"
parts = message.split(", ")
print(parts)  # Вывод: ['Hello', 'World!']

# strip(), lstrip(), rstrip(): Эти методы удаляют пробельные символы в начале и/или конце строки.
# strip() удаляет пробелы с обоих концов строки, lstrip() удаляет пробелы только в начале строки,
# а rstrip() удаляет пробелы только в конце строки. Например:
message = "   Hello, World!   "
stripped = message.strip()
left_stripped = message.lstrip()
right_stripped = message.rstrip()
print(stripped)  # Вывод: "Hello, World!"
print(left_stripped)  # Вывод: "Hello, World!   "
print(right_stripped)  # Вывод: "   Hello, World!"

# startswith(), endswith(): Эти методы проверяют, начинается ли строка с определенной подстроки (startswith())
# или заканчивается ли строка определенной подстрокой (endswith()). Они возвращают булевое значение True или False. Например:
message = "Hello, World!"
starts_with_hello = message.startswith("Hello")
ends_with_exclamation = message.endswith("!")
print(starts_with_hello)  # Вывод: True
print(ends_with_exclamation)  # Вывод: True

# join(): Этот метод объединяет элементы списка в одну строку, вставляя между ними заданную строку-разделитель. Например:
words = ["Hello", "World", "Python"]
joined = ", ".join(words)
print(joined)  # Вывод: "Hello, World, Python"

# isdigit(), isalpha(), isalnum(): Эти методы проверяют, состоит ли строка только из цифр (isdigit()),
# только из букв (isalpha()) или из цифр и букв (isalnum()). Они возвращают булевое значение True или False. Например:
number = "123"
word = "Hello"
alphanumeric = "Hello123"
print(number.isdigit())  # Вывод: True
print(word.isalpha())  # Вывод: True
print(alphanumeric.isalnum())  # Вывод: True