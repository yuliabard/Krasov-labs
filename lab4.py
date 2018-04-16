s = input('Введите строку:')
d = {}

for i in range(len(s)):
	if (s[i] not in d):
		d[s[i]] = 1
	else:
		d[s[i]] += 1

print('Статистика вхождения символов:',d)
print('Слова в алфавитном порядке:',sorted(s.split(" ")))
st = input('Введите слово: ')
if s.find(st)!=-1:
        print('Первое вхождение подстроки в строку:',s.find(st))
else:
        print('Слово не встречается в строке')
