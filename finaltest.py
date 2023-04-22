import pandas as pd
import tkinter.font as font
from tkinter import *
from sklearn import datasets, linear_model 

class train_model:
    
    def training(self):
        info =pd.read_csv('training_dataset.csv')
        array = info.values

        for i in range(len(array)):
            if array[i][0]=="Male":
                array[i][0]=1
            else:
                array[i][0]=0

        data=pd.DataFrame(array)

        maindata =data[[0,1,2,3,4,5,6]]
        mainarray=maindata.values

        personality=data[7]
        train_p=personality.values
        
        self.mul_lr = linear_model.LogisticRegression(multi_class='multinomial', solver='newton-cg',max_iter =1000)
        self.mul_lr.fit(mainarray, train_p)
        
    def testing(self, test_data):
        try:
            predict_test=list()
            for i in test_data:
                predict_test.append(int(i))
            p_pred = self.mul_lr.predict([predict_test])
            return p_pred
        except:
            print("All Factors For Finding Personality Not Entered!")

def prediction_result(top, name, personality_values):

    top.withdraw()
    applicant_data={"NAME OF USER ":name.get()}
    
    age = personality_values[1]
    
    print("\n******************** ENTERED DATA *********************\n")
    print(applicant_data, personality_values)
    
    personality = model.testing(personality_values)
    print("\n**************** PERSONALITY PREDICTED ****************\n")
    print(personality)
    
    result=Tk()
    result.geometry('700x500')
    result.configure(background='ivory2')
    result.title("Predicted Personality")
    
    Label(result, text="Result", fg='OrangeRed3', bg='ivory2', font=('Bookman Old Style',30,font.BOLD), pady=10, anchor=CENTER).pack(fill=BOTH)
    
    Label(result, text = str('{} : {}'.format("Name:", name.get())).title(), fg='black', bg='ivory2', font=("Britannic Bold",15)).pack(fill=BOTH)
    Label(result, text = str('{} : {}'.format("Age:", age)), fg='black', bg='ivory2', font=("Britannic Bold",15)).pack(fill=BOTH)
    Label(result, text = str("predicted personality: "+personality).title(), fg='black', bg='ivory2', font=("Britannic Bold",15)).pack(fill=BOTH)
    
    Label(result, text = "-------------------------------------------------------------------------------", fg='black', bg='ivory2', font=("Britannic Bold",15)).pack(fill=BOTH)
    quitBtn = Button(result, text="Exit", bg='OrangeRed3',fg='white',font=('Bookman Old Style',8), padx=5, command =lambda:  result.destroy()).pack()
    
    terms_mean = """
OPENNESS TO EXPERIENCE – (inventive/curious vs. consistent/cautious).
Appreciation for art, emotion, adventure, unusual ideas, curiosity, and variety of experience.

CONSCIENTIOUSNESS – (efficient/organized vs. easy-going/careless).
A tendency to show self-discipline, act dutifully, and aim for achievement;
planned rather than spontaneous behaviour.

EXTRAVERSION – (outgoing/energetic vs. solitary/reserved).
Energy, positive emotions, urgency, and the tendency to seek stimulation
in the company of others.

AGREEABLENESS – (friendly/compassionate vs. cold/unkind).
A tendency to be compassionate and cooperative rather than suspicious
and antagonistic towards others.

NEUROTICISM – (sensitive/nervous vs. secure/confident).
A tendency to experience unpleasant emotions easily, such as anger,
anxiety, depression, or vulnerability.
"""
    
    Label(result, text = terms_mean, fg='SteelBlue4', bg='ivory2', font=('Lucida Sans Typewriter',9,font.BOLD), justify=CENTER).pack(fill=BOTH)
    result.mainloop()

def predict_person():
    
    root.withdraw()
    
    top = Toplevel()
    top.geometry('700x500')
    top.configure(background='#2b6777')
    top.title("Personality Prediction")
    
    title = font.Font(family='Edwardian Script ITC', size=35, weight='bold')
    Label(top, text="Personality Prediction", fg='white', bg='#2b6777', font=title, pady=30).pack()

    qstn_font = font.Font(family='Baskerville Old Face', size=12 )
    Label(top, text="What is your name?", fg='white', bg='#2b6777', font=qstn_font).place(x=70, y=130)
    Label(top, text="How old are you?", fg='white', bg='#2b6777', font=qstn_font).place(x=70, y=160)
    Label(top, text="You identify as", fg='white', bg='#2b6777', font=qstn_font).place(x=70, y=190)
    Label(top, text="Likes exciting, unfamiliar and adventuorous things", fg='white', bg='#2b6777', font=qstn_font).place(x=70, y=220)
    Label(top, text="Finds difficult to work under pressure", fg='white', bg='#2b6777', font=qstn_font).place(x=70, y=250)
    Label(top, text="Likes to work in an organized and disciplined manner", fg='white', bg='#2b6777', font=qstn_font).place(x=70, y=280)
    Label(top, text="Listens what others have to say", fg='white', bg='#2b6777', font=qstn_font).place(x=70, y=310)
    Label(top, text="Likes parties and crowded places more than alone time", fg='white', bg='#2b6777', font=qstn_font).place(x=70, y=340)
    
    sName=Entry(top)
    sName.place(x=450, y=130, width=160)
    age=Entry(top)
    age.place(x=450, y=160, width=160)
    gender = IntVar()
    R1 = Radiobutton(top, text="Male", variable=gender, value=1, padx=14)
    R1.place(x=450, y=190)
    R2 = Radiobutton(top, text="Female", variable=gender, value=0, padx=6)
    R2.place(x=534, y=190)

    scalelist={1:"Strongly disagree",2:"Somewhat disagree",3:"Disagree",4:"Neutral",5:"Agree",6:"Somewhat agree",7:"Strongly agree"}

    def assignopenness(temp):
        for i,j in scalelist.items():
            if j==temp:
                global openness
                openness=i
    def assignneuroticism(temp):
        for i,j in scalelist.items():
            if j==temp:
                global neuroticism
                neuroticism=i
    def assignconscientiousness(temp):
        for i,j in scalelist.items():
            if j==temp:
                global conscientiousness
                conscientiousness=i
    def assignaggreableness(temp):
        for i,j in scalelist.items():
            if j==temp:
                global agreeableness
                agreeableness=i
    def assignextraversion(temp):
        for i,j in scalelist.items():
            if j==temp:
                global extraversion
                extraversion=i

    openness_menu=StringVar(top)
    openness_menu.set("Select")
    openness_drop = OptionMenu(top, openness_menu, *scalelist.values(),command=assignopenness)
    openness_drop.place(x=450, y=220, width=160)

    neuroticism_menu=StringVar(top)
    neuroticism_menu.set("Select")
    neuroticism_drop = OptionMenu(top, neuroticism_menu,*scalelist.values(),command=assignneuroticism)
    neuroticism_drop.place(x=450, y=250, width=160)

    conscientiousness_menu=StringVar(top)
    conscientiousness_menu.set("Select")
    conscientiousness_drop = OptionMenu(top, conscientiousness_menu,*scalelist.values(),command=assignconscientiousness)
    conscientiousness_drop.place(x=450, y=280, width=160)

    agreeableness_menu=StringVar(top)
    agreeableness_menu.set("Select")
    agreeableness_drop = OptionMenu(top, agreeableness_menu,*scalelist.values(),command=assignaggreableness)
    agreeableness_drop.place(x=450, y=310, width=160)
    
    extraversion_menu=StringVar(top)
    extraversion_menu.set("Select")
    extraversion_drop = OptionMenu(top, extraversion_menu,*scalelist.values(),command=assignextraversion)
    extraversion_drop.place(x=450, y=340, width=160)
    
    submitBtn=Button(top, text="Predict", fg='white', bg='PaleGreen4', font=('Bookman Old Style',12))
    submitBtn.config(command=lambda: prediction_result(top,sName,(gender.get(),age.get(),openness,neuroticism,conscientiousness,agreeableness,extraversion)))
    submitBtn.place(x=250, y=400, width=200)

    top.mainloop()
    
if __name__ == "__main__":
    model = train_model()
    model.training()
    root = Tk()
    root.geometry('700x500')
    root.configure(background='chartreuse4')
    root.title("Personality Prediction System")
    title = font.Font(family='Lucida Handwriting', size=40, weight='bold')
    homeBtnFont = font.Font(size=12, weight='bold')
    Label(root, text="Personality\nPrediction\nSystem", bg='chartreuse4',fg='white', font=title, pady=50).pack()
    b2=Button(root, padx=4, pady=4, width=30, text="Predict Personality", bg='black', fg='white', bd=1, font=homeBtnFont, command=predict_person).place(relx=0.5, rely=0.7, anchor=CENTER)
    root.mainloop()