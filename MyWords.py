import sys
import os
import json

from ui_myWords import * 

class MyWords(QMainWindow):
    def __init__(self) -> None:
        super(MyWords, self).__init__()
        self.ui = Ui_MyWords()
        self.ui.setupUi(self)

        self.words = []

    def init(self):
        '''
        Инициализируем приложение
        '''

        # Привязываем сигналы от кнопок
        self.ui.addBtn.clicked.connect(self.addWord)
        self.ui.removeWordBtn.clicked.connect(self.removeWord)
        self.ui.randomBtn.clicked.connect(self.randomWord)
        self.ui.checkBtn.clicked.connect(self.checkWord)
        
        # Читаем файл
        self.readTable4File()

    def addWord(self):
        '''
        Добавляет слово в таблицу
        '''
        
        # Получаем слово
        wordEng = self.ui.wordEng.text()
        wordRu = self.ui.wordRu.text()
        

    def saveTable2File(self):
        '''
        Сохраняет таблицу в файл
        '''
        pass

    def readTable4File(self):
        '''
        Читает таблицу из файла
        '''
        json_data = []
        file_path = 'MyWord_BD.json'

        if not os.path.exists(file_path):
            return
        
        with open(file_path, 'r', encoding='utf-8') as f:
            data = f.read()
        
        json_data = json.loads(data)

        


    def removeWord(self):
        '''
        Удаляет слово
        '''
        pass

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