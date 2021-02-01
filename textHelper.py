# модуль для работы с текстом

def removeSymbols(string):
	# список символов к замене на пробел
	symbolsToReplaceWithSpace = ['\n', '\"', '/', '{', '}', '[', ']', '(', ')', '<', '>', '=', '.']
	# заменяем в цикле символы на пробелы
	for symbol in symbolsToReplaceWithSpace:
		string = string.replace(symbol, ' ')
	# список спецсимволов к удалению
	symbolsToRemove = [',', '?', '!', ':']
	# удаляем в цикле спецсимволы из списка
	for symbol in symbolsToRemove:
		string = string.replace(symbol, '')
	return string

def wordAmountInFile(fileAsString, wordToCount):
	fileAsString = removeSymbols(fileAsString)
	# разбиваем строку на список подстрок
	words = fileAsString.split()
	# возвращаем количество вхождений искомого слова в список
	return words.count(wordToCount)

# добавляем окончание к слову 'раз' в зависимости от числа вхождений
def decorateAmount(wordAmount):
	if wordAmount > 4 and wordAmount < 21:
		wordAmount = str(wordAmount)
		wordAmount += ' раз'
	elif wordAmount % 10 > 1 and wordAmount % 10 < 5:
		wordAmount = str(wordAmount)
		wordAmount += ' раза'
	else:
		wordAmount = str(wordAmount)
		wordAmount += ' раз'
	return wordAmount
