words = {
            'кринж': 'Что-то очень странное или стыдное',
            'лол': 'Что-то очень смешное',
            'рофл': 'Прикол',
            'олд': 'Старый',
            'изи': 'Легко',
            'хард': 'сложно',
            'нормис': 'обычный человек'
            }
word = input("Какое слово вам перевести?").lower()
if word in words:
    print('перевод:', words[word])
else:
    print('нету такого')
