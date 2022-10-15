# Challenge 3: Implement the Complete Student Clas


class student :
    def __init__(self,name,rollnumber):
        self.__name = name
        self.__rollnumber = rollnumber

    def set_name(self,name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_rollnumber(self,rollnumber):
        self.__rollnumber = rollnumber

    def get_rollnumber(self):
        return self.__rollnumber

student_obj = student(input("Enter your name :")),input("Enter a rollnumber:")

student_obj.set_name(input("Enter a name"))
print(student_obj.get_name())

student_obj.set_rollnumber(input("Enter rollnumber:"))
print(student_obj.get_rollnumber())