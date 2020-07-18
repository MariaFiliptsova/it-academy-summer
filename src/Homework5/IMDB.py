'''В файле хранятся данные с сайта IMDB.
Скопированные данные хранятся в файле ./data5/ ratings.list.
Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
Найдите ТОП250 фильмов и извлеките заголовки.
Программа создает 3 файла  top250_movies.txt –
названия файлов, ratings.txt – гистограмма рейтингов,
years.txt – гистограмма годов.
'''
line_starts_with_new = False
count_movies = 0
counter = {}
y_counter = {}
try:
    with open('ratings.list', 'r', encoding="ISO-8859-1") as f:
        with open('top250_movies.txt', 'w') as top250:
            with open('ratings.txt', 'w') as movie_ratings:
                with open('years.txt', 'w') as years:
                    for line in f:
                        if line.startswith('New'):
                            line_starts_with_new = True
                            for line in f:
                                if line_starts_with_new is True:
                                    if count_movies < 250:
                                        name = line.split()[3:-1]
                                        top250.write(' '.join(name) + '\n')
                                        rating = line.split()[2]
                                        if rating not in counter:
                                            counter.update({rating: 1})
                                        else:
                                            counter[rating] += 1
                                        year = line.split()[-1]
                                        if year not in y_counter:
                                            y_counter.update({year: 1})
                                        else:
                                            y_counter[year] += 1
                                        count_movies += 1
                    list_keys = list(y_counter.keys())
                    list_keys.sort()
                    for k in counter:
                        movie_ratings.write(k + ' ' + '*' * counter[k] + '\n')
                    for y in list_keys:
                        x = y.strip('()')
                        years.write(x + ' ' + '*' * y_counter[y] + '\n')
except FileNotFoundError:
    print('File Not Found')
