import datetime as dt

#a class for a person
class Person():
    #constructor
    def __init__(self, name, YearOfBirth):
        '''
        Default constructor for a Person.
        :param name: property of person
        :param YearOfBirth: property of person
        '''
        self.name=name
        self.BirthYear=YearOfBirth

    #method
    def GetYearsOld(self):
        return dt.datetime.now().year-self.BirthYear

#demonstration of class inheritance
class Employee(Person):
    #constructor
    def __init__(self,name, YearOfBirth,PhoneNum,Company):
        '''
        This is the default constructor for class Employee which inherits from Person
        We don't employee non-persons
        :param name: property of parent
        :param YearOfBirth: property of parent
        :param PhoneNum: property of employee
        :param Company: property of employee
        '''
        #call constructor of parent class
        super().__init__( name, YearOfBirth)
        self.Phone=PhoneNum
        self.Company=Company

    #method
    def PrintPhoneNumber(self):
        print(self.Phone)

class Company():
    #constructor
    def __init__(self, Employees):
        '''
        This is the default constructor for the Company class
        :param Employees: an array of Employee objects
        '''
        self.Employees=[]
        for e in Employees:
            self.Employees.append(e)

    #method
    def PrintPhoneBook(self):
        for e in self.Employees:
            print(e.name, ":", e.Phone)

def main():
    Joe=Employee('Joe Biden', '1943', '555-203-7839','Democratic Politician')
    Bernie=Employee('Bernie Sanders', '1942', '555-786-5309','Socialist Politician')
    Elizabeth=Employee('Elizabeth Warren', '1950', '555-836-2211','Democratic Politician')

    DNC=Company([Joe, Bernie, Elizabeth])
    DNC.PrintPhoneBook()

main()
