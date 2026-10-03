import numpy as np
from numpy import random
import pandas as pd


"""
                  MARKSHEET
                      │
        ┌─────────────┴─────────────┐
        │                           │
   Student Data                Marks Data
        │                           │
   Student ID                  Programming
   Name                        Database
   Age                         Mathematics
   Section                     Networks
                               English
                                    │
                                    ↓
                              Calculations
                                    │
              ┌─────────────────────┼─────────────────┐
              ↓                     ↓                 ↓
            Total               Percentage          Average
              │                     │                 │
              └─────────────────────┼─────────────────┘
                                    ↓
                                  Grade
                                    ↓
                               Pass / Fail
                                   
                                                                """



#StudentId
StudentId= np.arange(101,109)
#StudentName
StudentName=np.array(["ali","ahmed","abdullah","anas",8,"saif","dawood","rohan"])
print(StudentName.dtype)
#Age
ages=np.random.randint(18,23,8)
#Marks (out of 50)
Marks=np.random.randint(10,50,(8,5))
#Total-Marks of all subjects (250)
TotalMarks=np.sum(Marks,axis=1)
#Percentage
Percentage= np.round((TotalMarks/250)*100,2)
#Average marks of a student in all subjects
Average=np.mean(Marks,axis=1)
#Grade (np.where(condition, value_if_true, value_if_false))
grades= np.where(Percentage >= 90,"A",
                 np.where(Percentage>=80,"B",
                          np.where(Percentage>=70,"C",
                                   np.where(Percentage>=60,"D",
                                            np.where(Percentage>50,"E","F")))))


for x in range(0,7):
    print("StusentId: ",StudentId[x])
    print("Student Name: ",StudentName[x])
    print("Age: ",ages[x])
    print("---Marks of the Student---")
    print("SQA: ",Marks[x,0])
    print("IS: ",Marks[x,1])
    print("OOAD: ",Marks[x,2])
    print("OS: ",Marks[x,3])
    print("DB: ",Marks[x,4])
    print("Total Marks: ",TotalMarks[x])
    print("Percentage of the Student: ",Percentage[x])
    print("Average marks of a Student: ",Average[x])
    print("Grade of the Student: ",grades[x])
    print("------------------------")
    

