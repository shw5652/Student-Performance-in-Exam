from tkinter import *

def getvals():
    print("Predicting Students Performance")
    print(f"{namevalue.get(),gendervalue.get(),racevalue.get(),parentaleducationvalue.get(),lunchvalue.get(),testpreparationvalue.get(),mathscorevalue.get(),readingscorevalue.get(),writingscorevalue.get(),averagescorevalue.get(),totalscorevalue.get(),percentagevalue.get(),gradevalue.get(),resultvalue.get()}")
    with open("Students Performance Prediction Record.txt","a")as f:
        f.write(f"{namevalue.get(),gendervalue.get(),racevalue.get(),parentaleducationvalue.get(),lunchvalue.get(),testpreparationvalue.get(),mathscorevalue.get(),readingscorevalue.get(),writingscorevalue.get(),averagescorevalue.get(),totalscorevalue.get(),percentagevalue.get(),gradevalue.get(),resultvalue.get()}\n")

def predict_result():

    math = mathscorevalue.get()
    reading = readingscorevalue.get()
    writing = writingscorevalue.get()

    total = (math + reading + writing)
    average = float(total/3)
    percentage = int(total/3)

    def getresult():
        if(math<35 or reading<35 or writing<35):
            return "Fail"
        else:
            return "Pass"
    result = getresult()

    def getgrade(percentage, result):
        if result == "Fail":
            return "Grade F"
        if (percentage >= 90):
            return "Grade A+"
        elif (percentage >= 80):
            return "Grade A"
        elif (percentage >= 70):
            return "Grade B+"
        elif (percentage >= 60):
            return "Grade B"
        elif (percentage >= 50):
            return "Grade C"
        elif (percentage >= 40):
            return "Grade D"
        else:
            return "Grade E"
    grade = getgrade(percentage, result)

    totalscorevalue.set(total)
    averagescorevalue.set(average)
    percentagevalue.set(percentage)
    gradevalue.set(grade)
    resultvalue.set(result)

    emptylabel.config(text="Student "+result+"ed...")

def clearvalues():
    nameentry.delete(0, END)
    genderentry.delete(0, END)
    raceentry.delete(0, END)
    lunchentry.delete(0, END)
    parentaleducationentry.delete(0, END)
    testpreparationentry.delete(0, END)
    mathscoreentry.delete(0, END)
    readingscoreentry.delete(0, END)
    writingscoreentry.delete(0, END)
    averagescoreentry.delete(0, END)
    totalscoreentry.delete(0, END)
    percentageentry.delete(0, END)
    gradeentry.delete(0, END)
    resultentry.delete(0, END)



win = Tk()
win.title("Students Preformance In Exam Prediction")
win.configure(width=1500,height=1500,bg='Teal')

Label(win,text="Students Performance in Exam", bg="orange",fg="black",font=("Algerian", 15)).grid(row=0,column=3)

#Labels
name = Label(win,text="Name",bg="grey",relief="ridge",fg="black",font=("Century", 12),width=25)
gender = Label(win,text="Gender",bg="grey",relief="ridge",fg="black",font=("Century", 12),width=25)
race = Label(win,text="Race/Ethnicity",bg="grey",relief="ridge",fg="black",font=("Century", 12),width=25)
lunch = Label(win,text="Lunch",bg="grey",relief="ridge",fg="black",font=("Century", 12),width=25)
parentaleducation = Label(win,text="Parental level of education",bg="grey",relief="ridge",fg="black",font=("Century", 12),width=25)
testpreparation = Label(win,text="Test preparation Course",bg="grey",relief="ridge",fg="black",font=("Century", 12),width=25)
mathscore = Label(win,text="Math score",bg="grey",relief="ridge",fg="black",font=("Century", 12),width=25)
readingscore = Label(win,text="Reading Score",bg="grey",relief="ridge",fg="black",font=("Century", 12),width=25)
writingscore = Label(win,text="Writing Score",bg="grey",relief="ridge",fg="black",font=("Century", 12),width=25)
averagescore = Label(win,text="Average Score",bg="grey",relief="ridge",fg="black",font=("Century", 12),width=25)
totalscore = Label(win,text="Total Score",bg="grey",relief="ridge",fg="black",font=("Century", 12),width=25)
percentage = Label(win,text="Percentage",bg="grey",relief="ridge",fg="black",font=("Century", 12),width=25)
grade = Label(win,text="Grade",bg="grey",relief="ridge",fg="black",font=("Century", 12),width=25)
result = Label(win,text="Result",bg="grey",relief="ridge",fg="black",font=("Century", 12),width=25)
emptylabel = Label(win,bg="teal",fg="red",font=("Century", 20,"bold"))


info1 = Label(win,text="**Information :- **                                   ", bg="teal",fg="black",font=("Century", 12))
info2 = Label(win,text="1) Passing Marks = 35                                 ", bg="teal",fg="black",font=("Century", 12))
info3 = Label(win,text="       2) Student failed in any subject will be failed", bg="teal",fg="black",font=("Century", 12))
info1.grid(row=22, column=1)
info2.grid(row=23, column=1)
info3.grid(row=24, column=1)


#pack
name.grid(row=2,column=1, padx=10, pady=10)
gender.grid(row=3,column=1, padx=10, pady=10)
race.grid(row=4,column=1, padx=10, pady=10)
lunch.grid(row=5,column=1, padx=10, pady=10)
parentaleducation.grid(row=6,column=1, padx=10, pady=10)
testpreparation.grid(row=7,column=1, padx=10, pady=10)
mathscore.grid(row=8,column=1, padx=10, pady=10)
readingscore.grid(row=9,column=1, padx=10, pady=10)
writingscore.grid(row=10,column=1, padx=10, pady=10)
averagescore.grid(row=2,column=4, padx=10, pady=10)
totalscore.grid(row=3,column=4, padx=10, pady=10)
percentage.grid(row=4,column=4, padx=10, pady=10)
grade.grid(row=5,column=4, padx=10, pady=10)
result.grid(row=6,column=4, padx=10, pady=10)


#Tkinter variables for storing entries
#input
namevalue = StringVar()
gendervalue = StringVar()
racevalue = StringVar()
lunchvalue = StringVar()
parentaleducationvalue = StringVar()
testpreparationvalue = StringVar()
mathscorevalue = IntVar()
readingscorevalue = IntVar()
writingscorevalue = IntVar()
#output
averagescorevalue = IntVar()
totalscorevalue = IntVar()
percentagevalue = IntVar()
gradevalue = StringVar()
resultvalue = StringVar()

#Entries
nameentry = Entry(win,textvariable = namevalue,font=("Bahnschrift SemiCondensed", 12))
genderentry = Entry(win,textvariable = gendervalue,font=("Bahnschrift SemiCondensed", 12))
raceentry = Entry(win,textvariable = racevalue,font=("Bahnschrift SemiCondensed", 12))
lunchentry = Entry(win,textvariable = lunchvalue,font=("Bahnschrift SemiCondensed", 12))
parentaleducationentry = Entry(win,textvariable = parentaleducationvalue,font=("Bahnschrift SemiCondensed", 12))
testpreparationentry = Entry(win,textvariable = testpreparationvalue,font=("Bahnschrift SemiCondensed", 12))
mathscoreentry = Entry(win,textvariable = mathscorevalue,font=("Bahnschrift SemiCondensed", 12))
readingscoreentry = Entry(win,textvariable = readingscorevalue,font=("Bahnschrift SemiCondensed", 12))
writingscoreentry = Entry(win,textvariable = writingscorevalue,font=("Bahnschrift SemiCondensed", 12))
averagescoreentry = Entry(win,textvariable = averagescorevalue,font=("Bahnschrift SemiCondensed", 12))
totalscoreentry = Entry(win,textvariable = totalscorevalue,font=("Bahnschrift SemiCondensed", 12))
percentageentry = Entry(win,textvariable = percentagevalue,font=("Bahnschrift SemiCondensed", 12))
gradeentry = Entry(win,textvariable = gradevalue,font=("Bahnschrift SemiCondensed", 12))
resultentry = Entry(win,textvariable = resultvalue,font=("Bahnschrift SemiCondensed", 12))

#Packing the entries
nameentry.grid(row=2,column=2,padx=10, pady=10)
genderentry.grid(row=3,column=2,padx=10, pady=10)
raceentry.grid(row=4,column=2,padx=10, pady=10)
lunchentry.grid(row=5,column=2,padx=10, pady=10)
parentaleducationentry.grid(row=6,column=2,padx=10, pady=10)
testpreparationentry.grid(row=7,column=2,padx=10, pady=10)
mathscoreentry.grid(row=8,column=2,padx=10, pady=10)
readingscoreentry.grid(row=9,column=2,padx=10, pady=10)
writingscoreentry.grid(row=10,column=2,padx=10, pady=10)
averagescoreentry.grid(row=2,column=6,padx=10, pady=10)
totalscoreentry.grid(row=3,column=6,padx=10, pady=10)
percentageentry.grid(row=4,column=6,padx=10, pady=10)
gradeentry.grid(row=5,column=6,padx=10, pady=10)
resultentry.grid(row=6,column=6,padx=10, pady=10)
emptylabel.grid(row=15, column=3,padx=10, pady=10)


#Button
Button(text="Predict", bg="brown", fg="yellow", width =20, font=("Times", 14), command=predict_result).grid(row=17,column=3, padx=40, pady=10)
Button(text="Save", bg="brown", fg="yellow", width =20, font=("Times", 14), command=getvals).grid(row=19,column=3, padx=40, pady=10)
Button(text="Clear",  bg="brown", fg="yellow", width =20, font=("Times", 14), command=clearvalues).grid(row=21,column=3, padx=40, pady=10)


win.mainloop()
