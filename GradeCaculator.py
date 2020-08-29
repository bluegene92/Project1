import sys
from PyQt5 import QtWidgets, uic
from decimal import Decimal

def GetExamPercentage():
    exam1 = Decimal(window.exam1Edit.text())/100
    exam1Percent = exam1 * Decimal('0.15')
    exam2 = Decimal(window.exam2Edit.text())/100
    exam2Percent = exam2 * Decimal('0.15')
    return exam1Percent + exam2Percent    

def GetProjectPercentage():
    midtermProject = Decimal(window.midtermProjectEdit.text())/100
    midtermPercent = midtermProject * Decimal('0.1')
    finalProject = Decimal(window.finalProjectEdit.text())/100
    finalPercent = finalProject * Decimal('0.2')
    return midtermPercent + finalPercent

def GetProjectAssignmentsPercentage():
    proposal = Decimal(window.proposalEdit.text())/100
    proposalPercent = proposal * Decimal('0.01')
    project1 = Decimal(window.projectAssignment1Edit.text())
    project2 = Decimal(window.projectAssignment2Edit.text())
    project3 = Decimal(window.projectAssignment3Edit.text())
    projectTotal = (project1+project2+project3)/300
    projectPercent = projectTotal * Decimal('0.09')
    return proposalPercent + projectPercent


def GetHomeworkPercentage():
    hw1 = Decimal(window.hw1Edit.text())
    hw2 = Decimal(window.hw2Edit.text())
    hw3 = Decimal(window.hw3Edit.text())
    hw4 = Decimal(window.hw4Edit.text())
    hw5 = Decimal(window.hw5Edit.text())
    hw6 = Decimal(window.hw6Edit.text())
    hw7 = Decimal(window.hw7Edit.text())
    hw8 = Decimal(window.hw8Edit.text())
    hw9 = Decimal(window.hw9Edit.text())
    hw10 =Decimal(window.hw10Edit.text())
    total = hw1+hw2+hw3+hw4+hw5+hw6+hw7+hw8+hw9+hw10
    avg = total / 1000
    return avg * Decimal('0.3')

def GetGrade(p):
    percent = p * 100
    print(percent)
    if (percent >= 89.5 and percent <= 100): return "A"
    if (percent >= 79.5 and percent < 89.5): return "B"
    if (percent >= 69.5 and percent < 79.5): return "C"
    if (percent >= 0 and percent < 69.5): return "F"
    else: raise Exception("Invalid percent, must be from 0.0 to 1.0")

def GetColor(grade):
    Green = "rgb(144,190,109)"
    Blue = "rgb(58,134,255)"
    Yellow = "rgb(250,245,81)"
    Orange = "rgb(248,150,30)"
    Red = "rgb(249,65,68)"
    if (grade == "A"): return Green
    if (grade == "B"): return Blue
    if (grade == "C"): return Yellow
    if (grade == "F"): return Red
    else: raise Exception("Invalid grade, must be [A,B,C,F]")


def Click_Handler():
    homeworkPercentage = GetHomeworkPercentage()
    projectAssignmentPercentage = GetProjectAssignmentsPercentage()
    projectPercentage = GetProjectPercentage()
    examPercentage = GetExamPercentage()
    gradeTotalPercent = homeworkPercentage + projectAssignmentPercentage + projectPercentage + examPercentage

    grade = GetGrade(gradeTotalPercent)
    BG_Color = GetColor(grade)
    window.colorLabel.setStyleSheet("QLabel {background-color:"+ BG_Color +"}")

    window.homeworkPercentLabel.setText("{:.2f}".format(homeworkPercentage))
    window.projectAssignmentPercentLabel.setText("{:.2f}".format(projectAssignmentPercentage))
    window.projectPercentLabel.setText("{:.2f}".format(projectPercentage))
    window.examPercentLabel.setText("{:.2f}".format(examPercentage))
    window.gradeLabel.setText("Final Gade: {}".format(gradeTotalPercent * 100))
    window.gradeLetterLabel.setText("Grade: " + grade)

def init():
    window.hw1Edit.setText("0")
    window.hw2Edit.setText("0")
    window.hw3Edit.setText("0")
    window.hw4Edit.setText("0")
    window.hw5Edit.setText("0")
    window.hw6Edit.setText("0")
    window.hw7Edit.setText("0")
    window.hw8Edit.setText("0")
    window.hw9Edit.setText("0")
    window.hw10Edit.setText("0")
    window.proposalEdit.setText("0")
    window.projectAssignment1Edit.setText("0")
    window.projectAssignment2Edit.setText("0")
    window.projectAssignment3Edit.setText("0")
    window.midtermProjectEdit.setText("0")
    window.finalProjectEdit.setText("0")
    window.exam1Edit.setText("0")
    window.exam2Edit.setText("0")

app = QtWidgets.QApplication(sys.argv)
window = uic.loadUi("GradeCaculator.ui")
init()
window.calculateBtn.clicked.connect(Click_Handler)
window.show()
sys.exit(app.exec_())