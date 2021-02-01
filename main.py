# импортим функции для работы с текстом
from textHelper import *

def main():
	while True:
		fileName = ''
		# запрашиваем имя файла, пока оно не станет непустым
		while len(fileName) == 0:
			fileName = input('Введите имя файла, либо [Y] для выхода: ')	
		if fileName.lower() == 'y':
			break
		try:
			file = open(fileName, 'r', encoding='utf8')
			fileAsString = file.read()
			file.close()
			if len(fileAsString) == 0:
				raise Exception('Файл пуст')
			try:
				wordToCount = ''
				# запрашиваем имя файла, пока оно не станет непустым
				while len(wordToCount) == 0:
					wordToCount = input('Введите слово для поиска: ')
				# передаем строки приведённые к нижнему регистру для регистронезависимости поиска 
				wordAmount = wordAmountInFile(fileAsString.lower(), wordToCount.lower())
				print('Слово', '\'' + wordToCount + '\'', 'встречается в файле', decorateAmount(wordAmount), '\n')
			except Exception as e:
				print('Исключение при подсчёте слов: ', e, '\n')
		except Exception as e:
			print('Исключение при чтении файла: ', e, '\n')

if __name__=='__main__':
    main()
