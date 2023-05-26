import random
import sys
import jn_data
# from PyQt5.QtCore import QSize, Qt
# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

numbers = jn_data.numbers_dict
dif_numbers = [4,7,9] # numbers with different pronounciations
def generate_numbers():
    generated_number = [random.randint(0,9) for n in range(0,4)]
    output_number = ''
    output_kanji = ''
    output_hiragana = ''
    zero_at_start = False

    for idx ,place in enumerate(generated_number):
        hiragana = numbers[place][1]
        kanji = numbers[place][0]
        number = str(place)
        
        place_hiragana = jn_data.place_hiragana
        place_kanji = jn_data.place_kanji
        
        if place in dif_numbers:
            hiragana = hiragana.split('/')[-1]

        output_hiragana = output_hiragana + hiragana
        output_kanji = output_kanji + kanji
        
        if place != 0 or zero_at_start:
            output_number = output_number + number
            zero_at_start = True
        if place != 0:
            output_hiragana = output_hiragana + place_hiragana[idx]
            output_kanji = output_kanji + place_kanji[idx]

    return output_number, output_hiragana, output_kanji


# class gui(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("My App")
#         button = QPushButton("Press Me!")
#         button.setCheckable(True)
#         button.clicked.connect(self.the_button_was_clicked)
#         button.clicked.connect(self.the_button_was_toggled)
        
#         # Set the central widget of the Window.
#         self.setCentralWidget(button)
        
#     def the_button_was_clicked(self):
#         print('Clicked!')
        
#     def the_button_was_toggled(self, checked):
#         print("Checked?", checked)

# app = QApplication(sys.argv)

# window = gui()
# window.show()

# app.exec()
