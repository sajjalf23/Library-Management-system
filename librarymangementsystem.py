class Book:

    def __init__(self , name , idb , isbn ):
        self.name = name
        self.ID = idb
        self.ISBN = isbn
        self.issued = False

    def display(self):
       print("Title : " , self.name)
       print("ID : ",self.ID)
       print("ISBN : ",self.ISBN)
       print("HAS ISSUED : ", self.issued)

class Student:

    def __init__(self , name , id , has_issued = False):
        self.name = name 
        self.id = id
        self.has_issued = has_issued

    def display(self):
        print("Name : " , self.name)
        print("ID : ", self.id)
        print("has issued any book : ", self.has_issued)

class Library:

    def __init__(self ):
        self.books = []
        self.students = []

    def add_book(self, name , ID , isbn):
        B = Book(name , ID , isbn)
        self.books.append(B)

    def display_books(self):
        print("Books data : ")
        print()
        for x in self.books:
            x.display()
            print()


    def book_list(self):
        print("Here is the List of books we have : ")
        print()
        for x in self.books:
            print(x.name)


    def search_books(self , Title):
        for x in self.books:
            if(x.name == Title):
                print("Book found = " , end = "" )
                x.display()
                return
        print(Title , " =  Book is not found ")
    
    def issue_books(self, Title , date , student_id):
        for x in self.books:
            if(x.name == Title ):
                if(x.issued):
                    print("Book already issued ! (Not available)")
                else:
                    x.issued = True
                    self.students[student_id].has_issued = True
                    due_date = ( date + 15 )
                    if(due_date > 30 ):
                        due_date = due_date / 30
                        print("Due Date is = " , due_date)
                        print( " of next month ")
                    else:
                        print("Due Date is = " , due_date)
                    return
        print("Book not available ! ")

    
    def return_book ( self , isbn):
        for x in self.books:
            flag = False
            if(x.ISBN == isbn):
                x.issued = False
                flag = True
                print("Book returned successfully !")
                return
        if(not flag):
            print("ISSUE ! ")

    
    def register_student(self,name ):
        id = len(self.students)
        s = Student(name , id)
        self.students.append(s)

    def display_students(self):
        print("List of students : ")
        print()
        for x in self.students:
            x.display()
            print()

    def student_list(self):
        print("List of students : ")
        print()
        for x in self.students:
            print(x.name)

    
    def write_in_book_doc(self):
        f = open("books.txt", "w")
        for x in self.books:
            data = x.name + " " + str(x.ID) + " " + str(x.ISBN) + " " + str(x.issued) + "\n" 
            f.write(data)
        f.close()

    
    def read_Book_doc(self):
        f = open("books.txt" , "r")
        data = f.read()
        print(data)
        f.close()

    
    def write_in_student_doc(self):
        f = open("student.txt" , "w")
        for x in self.students:
            data = x.name + " " + str(x.id) + " " + str(x.has_issued) + "\n"
            f.write(data)
        f.close()

    def read_student_doc(self):
        f = open("student.txt" , "r")
        data = f.read()
        print(data)
        f.close()

L1 = Library()
L1.add_book("harry Potter" , 1 , 123)
L1.add_book("Shakespare" , 2 , 456)
L1.add_book("Power of subconsious mind" , 3 , 789)
L1.add_book("Steve Jobs" , 4 , 101)
L1.add_book("Micael" , 5 , 102)


L1.search_books("Steve Jobs")
L1.search_books("hello!")

L1.register_student("Sajjal" )
L1.register_student("fatima")
L1.register_student("Maham")

L1.issue_books("Shakespare" , 9 , 1)
L1.issue_books("Micael" , 17 , 2)
L1.return_book(456)

L1.display_books()

L1.book_list()

L1.student_list()

L1.display_students()

L1.write_in_book_doc()

L1.read_Book_doc()


L1.write_in_student_doc()

L1.read_student_doc()