from MainWindowBMI import Ui_MainWindow


class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.pushButtonCalculate.clicked.connect(self.calculateBMI)
        self.pushButtonClose.clicked.connect(self.MainWindow.close)
    def calculateBMI(self):
        weight=float(self.lineEditweight.text())
        height=float(self.lineEditheight.text())
        height=height/100
        BMI=weight/(height*height)
        BMI=round(BMI,2)
        comment=""
        if BMI<16:
            comment="Severe Thinness"
        elif BMI<17:
            comment="Moderate Thinness"
        elif BMI<18.5:
            comment="Mild Thinness"
        elif BMI<25:
            comment="Normal"
        elif BMI<30:
            comment="Overweight"
        elif BMI<35:
            comment="Obese Class I"
        elif BMI<40:
            comment="Obese Class II"
        else:
            comment = "Obese Class III"
        self.lineEditBMI.setText(str(BMI))
        self.lineEditComment.setText(comment)
    def show(self):
        self.MainWindow.show()