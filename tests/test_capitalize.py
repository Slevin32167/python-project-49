from capitalize import capitalize


print("Тест 1: Проверяем пустую строку ...")
assert capitalize("") == ""
print("Пустая строка работает!")


print("Тест 2: Проверяем слово 'hello'...")
assert capitalize("hello") == "Hello"
print("Слово 'hello' работает!")


print("Тест 3: Проверяем слово 'world'...")
assert capitalize("world") == "World"
print("Слово 'world' работает!")


print("Тест 3: Проверяем слово 'hexlet'...")
assert capitalize("hexlet") == "Hexlet"
print("Слово 'hexlet' работает!")



print("Все тесты завершены!")