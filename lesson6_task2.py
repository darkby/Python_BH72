"""Код Морзе для представления цифр и букв использует тире и точки. Напишите
функцию для кодирования текстового сообщения в соответствии с кодом Морзе.
(словари в помощь)"""

morze = {'a': '•—', 'b': '—•••', 'c': '—•—•', 'd': '—••',
         'e': '•', 'f': '••—•', 'g': '——•', 'h': '••••',
         'i': '••', 'j': '•———', 'k': '—•—', 'l': '•—••',
         'm': '——', 'n': '—•', 'o': '———', 'p': '•——•',
         'q': '——•—', 'r': '•—•', 's': '•••', 't': '—',
         'u': '••—', 'v': '•••—', 'w': '•——', 'x': '—••—',
         'y': '—•——', 'z': '——••'}
def text_in_morze(text):
    result = []
    text_in_lower = text.lower()
    space_count = text_in_lower.count(' ')
    text_final = text_in_lower.replace(' ','', space_count)
    for i in text_final:
        result += morze.get(i)
    print(result)

text_in_morze(text = input('Enter text for codind in Morze '))