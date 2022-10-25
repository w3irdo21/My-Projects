class Library :
    def __init__(self,ListOfBooks):
        self.Books=ListOfBooks
    def showBooks(self):
        print("Books Available Here :\n")
        for Book in self.Books :
            print("*" +Book)
        print("\nWhich Book You Want To Take")

    def booktake(self,BookName) :
        if BookName in self.Books :
          print("Book Issued To You Now,Keep it safe & Return Back To us in 30 Days")
          self.Books.remove(BookName)

    def returnbook(self,BookName) :
            self.Books.append(BookName)
            print("Thanks For Returning The Book ")
class Student :
    def requestbook(self) :
        self.book= input("Enter :")
        return self.book
    
    def returnBook(self) :
        self.book=input('Book Name You Want To Return :')
        return self.book

if __name__=="__main__":
    Lib=Library(["Algorithms","Python Notes","CPP Notes","Data Structure","Web Development"])
    student=Student()
    while(True) :
        print("***Welcome To Library***\n ")
        # print("Books Available Here :")
        print(''' 1.) I want To Borrow A Book\n 2.) I Want to Return A Book \n 3.)J Just Want To See Books Present Here\n 4.) Exit From Library''')
        # try :
        a=int(input(""))
        # except  Exception as e:
            # print(e)
        if a==1 :
            Lib.showBooks()
            Lib.booktake(student.requestbook())
        elif a==2 :
            Lib.returnbook(student.returnBook())
        elif a==3 :
            Lib.showBooks()
        elif a==4 :
            print("Thanks For Using Our Library , Have A Great Day")
            exit()
        else :
            print("Wrong Input")