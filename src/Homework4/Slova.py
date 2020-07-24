import string

"""Во входной строке записан текст.
Словом считается последовательность непробельных символов идущих подряд,
слова разделены одним или большим числом пробелов или символами конца строки.
Определите, сколько различных слов содержится в этом тексте.
"""

# я не согласна, что не надо удалять знаки препинания, потому что,
# если мы это не сделаем 'Пьер' и 'Пьер,' будут различными словами,
# а на самом деле это повторяющееся слово.

tekst = 'Пьер сидел в гостиной, где Шиншин, как с приезжим из-за границы, \
завел с ним скучный для Пьера политический разговор, \
к которому присоединились и другие. Когда заиграла музыка, \
Наташа вошла в гостиную.'
punc = string.punctuation
tekst_without_punc = ''.join(symbol for symbol in tekst if symbol not in punc)
print(len(set(tekst_without_punc.split())))
