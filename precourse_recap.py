
from unittest import result


def Codeclan_day(Study, Freetime):
    print("In Total we spend roughly " + str(Study) + " hours completing coursework in the classroom enviroment and " + str(Freetime) + " or more hours or more to complete home based learning")


Class_study = 8
Home_study = 1
Total_time = 24

Study = Class_study
Freetime = Home_study

Codeclan_day(Study, Freetime)

Total_hours = Class_study + Home_study

print(Total_hours)

Hours_left = Total_time - Total_hours

print(Hours_left)