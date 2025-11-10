from capitalize import capitalize


print("Тестируем: hello → Hello")
result = capitalize("hello")
if result == "Hello":
    print("Успех!")
else:
    print(f"Ошибка! Получили: '{result}', ожидали 'Hello'")


print("Тестируем: '' → ''")
result = capitalize("")
if result == "":
    print("Успех!")
else:
    print(f"Ошибка! Получили: '{result}', ожидали ''")


print("Все тесты завершены!")