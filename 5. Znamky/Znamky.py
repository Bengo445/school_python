


def eval_grade_perc(perc):
    if perc > 0.9:
        return 1
    elif perc > 0.75:
        return 2
    elif perc > 0.5:
        return 3
    elif perc > 0.35:
        return 4
    else:
        return 5
def eval_grade_name(grade):
    if grade == 1:
        return "Výborný"
    elif grade == 2:
        return "Chválitebný"
    elif grade == 3:
        return "Dobrý"
    elif grade == 4:
        return "Dostatočný"
    else:
        return "Nedostatočný"


class Student:

    def __init__(self, id:int, id_isic:str, name:str, surname:str, grade:str, email:str):
        self.id = id
        self.id_isic = id_isic
        self.name = name
        self.surname = surname
        self.grade = grade
        self.email = email
        self.subjects:dict[list] = {}

    def addSubject(self, subject:str):
        if not (subject in self.subjects.keys()):
            self.subjects[subject] = []
        else:
            print("Predmet už existuje")
    
    def removeSubject(self, subject:str):
        self.subjects.pop(subject, None)
    
    def addGrade(self, subject:str, event_name:str, points:float, base:float):
        if subject in self.subjects.keys():
            self.subjects[subject].append( {"event":event_name, "points":points, "base":base} )
        else:
            print(f"Predmet '{subject}' neexistuje")
    
    def removeGrade(self, event_name):
        for subj_grades in self.subjects.values():
            for i in range(len(subj_grades)):
                if subj_grades[i]["event"] == event_name:
                    subj_grades.pop(i)
                    return
    
    def printAllGrades(*args):
        ## ONE SUBJECT
        if len(args) == 2:
            if not (isinstance(args[0], Student) and isinstance(args[1], str)):
                return
            self = args[0]
            subject = args[1]
            total_grades = []
            print(f'Predmet: "{subject}"')
            for grade in self.subjects[subject]:
                grade_num = eval_grade_perc(grade["points"]/grade["base"])
                total_grades.append(grade_num)
                print(f" - {grade["event"]} - {grade["points"]}/{grade["base"]} -> {grade_num}")
            subject_avg = sum(total_grades)/len(total_grades)
            print(f" - Priemer: {subject_avg} - Výsledná známka: {eval_grade_name(subject_avg)}")

        ## ALL SUBJECTS
        elif len(args) == 1:
            if not (isinstance(args[0], Student)):   
                self = args[0]
                for subject in self.subjects.keys():
                    self.printAllGrades(subject)



stud = Student(1, "isic123", "Jozo", "Jozenik", "IV.B", "Jozo@Jozo.Jozo")
stud.addSubject("Matematika")
stud.addGrade("Matematika", "pisomka", 5, 10)
stud.addGrade("Matematika", "pisomka2", 1, 10)
stud.addGrade("Matematika", "diktat", 3, 10)
stud.printAllGrades()
stud.printAllGrades("Matematika")