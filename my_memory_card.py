from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QMessageBox, QGroupBox, QButtonGroup
from random import shuffle

class Question ():
    def __init__(self, vopros, otvet, wrong2, wrong3, wrong4):
        self.vopros = vopros
        self.otvet = otvet
        self.wrong2 = wrong2
        self.wrong3 = wrong3
        self.wrong4 = wrong4

def show_result():
    group1.hide()
    group2.show()
    knopka.setText('Следующий вопрос')
def show_question():
    group2.hide()
    group1.show()
    knopka.setText('Ответить')
    knopki1234.setExclusive(False)
    knopki1.setChecked(False)
    knopki2.setChecked(False)
    knopki3.setChecked(False)
    knopki4.setChecked(False)
    knopki1234.setExclusive(True)
def start_test():
    if knopka.text() == 'Ответить':
        check_answer()
    else:
        next_question()
def ask(question):
    nadpis.setText(question.vopros)
    shuffle(knopppki)
    knopppki[0].setText(question.otvet)
    knopppki[1].setText(question.wrong2)
    knopppki[2].setText(question.wrong3)
    knopppki[3].setText(question.wrong4)
    g_nadpis2.setText(question.otvet)
    show_question()
def check_answer():
    mw.schn += 1
    if knopppki[0].isChecked():
        mw.schp += 1
        np = 'Правильно. Количество правильных ответов:'+ str(mw.schp)+'из'+ str(mw.schn)
        g_nadpis1.setText(np)
    else:
        np = 'Неправильно. Количество правильных ответов:'+ str(mw.schp)+'из'+ str(mw.schn)
        g_nadpis1.setText(np)
    show_result()
def next_question():
    mw.sch += 1
    if mw.sch >= len(q_list):
        mw.sch = 0
    ask(q_list[mw.sch])



app = QApplication([])
mw = QWidget()
mw.resize(400, 200)
mw.sch = -1
mw.schp = 0
mw.schn = 0

nadpis = QLabel('Какой национальности не существует?')
group1 = QGroupBox('Варинты ответов')
group2 = QGroupBox('Результат теста')
g_nadpis1 = QLabel('Правильно/Неправильно')
g_nadpis2 = QLabel('Правильный ответ')
knopka = QPushButton('Ответить')
knopki1 = QRadioButton('Энцы')
knopki2 = QRadioButton('Смурфы')
knopki3 = QRadioButton('Чулымцы')
knopki4 = QRadioButton('Алеуты')
knopppki= [knopki1, knopki2, knopki3, knopki4]
knopki1234 = QButtonGroup()
knopki1234.addButton(knopki1)
knopki1234.addButton(knopki2)
knopki1234.addButton(knopki3)
knopki1234.addButton(knopki4)

line_l = QVBoxLayout()
line_l.addWidget(knopki1)
line_l.addWidget(knopki2)
line_r = QVBoxLayout()
line_r.addWidget(knopki3)
line_r.addWidget(knopki4)
liniya_g = QHBoxLayout()
liniya_g.addLayout(line_l)
liniya_g.addLayout(line_r)
group1.setLayout(liniya_g)
liniya = QVBoxLayout()
liniya.addWidget(g_nadpis1)
liniya.addWidget(g_nadpis2, alignment = Qt.AlignCenter)
group2.setLayout(liniya)
liniya_v = QVBoxLayout()
liniya_v.addWidget(nadpis)
liniya_v.addWidget(group1)
liniya_v.addWidget(group2)
liniya_v.addWidget(knopka)

mw.setLayout(liniya_v)
q = Question('Какой национальности не существует?', 'Смурфы', 'Энцы', 'Чулымцы', 'Алеуты')
q_list = [Question('Какой у растений наиболее распространённый пигмент?', 'хлорофилл', 'таллом', 'лейкос', 'хрома'), Question('Какой из химиеских элементов преобладает в составе клетки?', 'кислород', 'углерод', 'водород', 'азот'), Question('Какое научное название имеет слоивище?', 'таллом', 'пластид', 'цитоплазма', 'гамета'), Question('Совокупность клеток и межклеточного вещества называют...', 'тканью', 'функцией', 'цитоплазмой', 'лубом'), Question('Какой танью покрыт корневой чехлик?', 'покровной', 'основной', 'образовательной', 'механической'), Question('Какое научное название имеет луб?', 'флоэма', 'ксилема', 'камбий', 'пробка'), Question('Какая покровная ткань отличается своей тонкостью и прорачносью?', 'кожица', 'пробка', 'ксилема', 'камбий'), Question('Какое жилкование имеет лист берёзы?', 'сетчатое', 'паталлельное', 'перпендикулярное', 'дуговое'), Question('К какому цветку относится пестик?', 'к женскому', 'к мужскому', 'к обоеполому', 'к раздельнополому')]
ask(q)
group2.hide()

knopka.clicked.connect(start_test)

mw.show()
app.exec_()
print('статистика '+str(mw.schp / mw.schn * 100),'%')