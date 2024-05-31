import sys
import os
import json

from ui_myWords import *
from PySide6.QtWidgets import (
    QMessageBox, QAbstractItemView, QTableWidgetItem)

class MyWords(QMainWindow):
    def __init__(self) -> None:
        super(MyWords, self).__init__()
        self.ui = Ui_MyWords()
        self.ui.setupUi(self)

        self.init()


    def init(self):
        '''
        Инициализируем приложение
        '''

        # Привязываем сигналы от кнопок
        self.ui.addBtn.clicked.connect(self.addWord)
        self.ui.removeWordBtn.clicked.connect(self.removeWord)
        self.ui.randomBtn.clicked.connect(self.randomWord)
        self.ui.checkBtn.clicked.connect(self.checkWord)

        # Запрещаем редактирование таблицы
        self.ui.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        
        # Добавляем выделение всей строки
        self.ui.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        # Задаём названия колонок
        self.ui.tableWidget.setColumnCount(4)
        labels = ['Англ.','Рус.','Прав. ответов','Неправ. ответов']
        self.ui.tableWidget.setHorizontalHeaderLabels(labels)

        # Читаем файл
        self.words = {}
        self.readTable4File()

    def printInfo(self, title: str = None, text: str = None):
        '''Выводит информацию на экран'''
        QMessageBox.information(self, title, text)

    def addWord(self, word:list = None):
        '''
        Добавляет слово в таблицу и в файл
        '''
        
        # Получаем слово и перевод
        if not word:
            wordEng = self.ui.wordEng.text()
            wordRu = self.ui.wordRu.text()
            correctAnswer = 0
            norCorrectAnswer = 0

        else:
            wordEng = word[0]
            wordRu = word[1]
            correctAnswer = word[2]
            norCorrectAnswer = word[3]

        if not wordEng or not wordRu:
            self.printInfo('Предупреждение', 'Сначала заполните поля с английским и русским словами')
            return
        
        if wordEng in self.words:
            self.printInfo('Предупреждение', 'Данное слово уже существует')
            return
        
        # Добавляем слово и записываем число удачных и неудачных попыток
        self.words[wordEng] = [wordRu, correctAnswer, norCorrectAnswer]

        # Добавляем слово в таблицу
        rowNumber = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(rowNumber)

        self.ui.tableWidget.setItem(rowNumber,0, QTableWidgetItem(str(wordEng)))
        self.ui.tableWidget.setItem(rowNumber,1, QTableWidgetItem(str(self.words.get(wordEng)[0])))
        self.ui.tableWidget.setItem(rowNumber,2, QTableWidgetItem(str(self.words.get(wordEng)[1])))
        self.ui.tableWidget.setItem(rowNumber,3, QTableWidgetItem(str(self.words.get(wordEng)[2])))

        if not word:
            self.saveWords2File()
            self.ui.wordEng.setText('')
            self.ui.wordRu.setText('')

    def saveWords2File(self):
        '''
        Сохраняет таблицу в файл
        '''
        # Записывает json файл
        file_path = 'MyWord_BD.json'

        json_string = json.dumps(self.words, ensure_ascii=False)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(json_string)

    def readTable4File(self):
        '''
        Читает таблицу из файла
        '''
        json_data = []
        file_path = 'MyWord_BD.json'

        if not os.path.isfile(file_path):
            return
        
        with open(file_path, 'r', encoding='utf-8') as f:
            data = f.read()
        
        json_data = json.loads(data)

        for element in json_data.keys():
            word = []
            word.append(element)
            lst = json_data.get(element)
            word.append(lst[0])
            word.append(lst[1])
            word.append(lst[2])
            self.addWord(word)

    def removeWord(self):
        '''
        Удаляет слово
        '''
        
        row = self.ui.tableWidget.currentRow()

        if row == -1:
            self.printInfo('','Сначала выберите слово')
            return

        # Удаляем из списка
        word = self.ui.tableWidget.item(row,0).text()
        self.words.pop(word, None)

        # Удаляем из таблицы
        self.ui.tableWidget.removeRow(row)

        # Сохраняем информацию в таблицу
        self.saveWords2File()



    def randomWord(self):
        '''
        Рандомно возвращает слово из таблицы
        '''
        pass

    def checkWord(self):
        '''
        Проверяет написанное слово
        '''
        pass


if __name__ == '__main__':
    print('run')
    app = QApplication()

    window = MyWords()
    window.show()
    sys.exit(app.exec())