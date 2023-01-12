
class Star_Cinema:
    _hall_list = []
    def entry_hall(self,hall1):
        self._hall_list.append(vars(hall1))
   
        
        

class Hall(Star_Cinema):
    def __init__(self,rows,cols,hall_no):
        self._seats =  {}
        self._show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.entry_hall(self)
    
        
    def entry_show(self,id,movie_name,time):
        self._show_list.append((id,movie_name,time))
        self._seats[id]=([[f"empty" for i in range(self.cols)] for j in range(self.rows)])
        

        
    def book_seats(self, name, phone, id, seat_numbers):
        flag=0
        _booked_Allseats=[]
        for keys, value in self._seats.items():
            print()
            if keys==id:
                flag=1
                for rc in seat_numbers:
                    row,col=rc
                    if 0<row<=self.rows and 0<col<=self.cols:
                        if  value[row-1][col-1]=="empty":
                                value[row-1][col-1]="booked"
                                print(f"Seat: ({row},{col}) -->> seat Booking Successfully!")
                                _booked_Allseats.append((row,col))
                        else:
                            print(f"Seat: ({row},{col}) -->> SEAT Already Booked")
                    else:
                        print(f"Seat: ({row},{col}) -->> Invalid Seat")

        if flag==0:
            print("Wrong!! In this Show ID is Not Valid, Please Try Again\n")

        print(f"{'**'*15} Seat Booking Details {'**'*15}\n")
        print(f"Name:{name}\t\t Phone:{phone} \t\t Movie ID:{id}\n")
        
        for i in self._show_list:
            if i[0]==id:
                print(f"Movie Name:{i[1]}\t\t Movie Time: {i[2]}",)
        
        print("Your Ticket Number(s) Are:",end=" ")
        if len( _booked_Allseats)==0:
            print("No Tickets for You Yet! Try Again")

        else:
            for i in  _booked_Allseats:
                print(f"{i}",end=" ")
            print()
        print("Hall No:", end="")
        print
        print(self._hall_list[0]['hall_no'])
        print(f"{'**'*40} \n")


    def view_show_list(self): 
        print(f"\n{'**'*15}Todays Movies {'**'*15}\n")
        
        for i in range(len(self._show_list)):
            print(f"Show Code: {self._show_list[i][0]}\t\t Movie Name: {self._show_list[i][1]}\t\ttime: {self._show_list[i][2]}\n")
        
        return (f"\n{'**'*10} Welcome to Our Moive Theatre {'**'*15}\n")
    
    

    def view_available_seats(self,id):

        print(f"{'**'*15} Avaibale seats of show:{id} {'**'*20}\n")

        for keys, value in self._seats.items():
            flag=0
            if keys==id:
                flag=1
                seat_list=self._seats[id]
                for i in range(len(seat_list)):
                    for j in range(len(seat_list[i])): 
                        print(f"{(i+1,j+1)}:{seat_list[i][j]}",end="\t\t ")
                    print()

                break
        if flag==0:
            print("Warning!! Wrong show id, Please Try Again")
        return(f"\n{'**'*20} welcome to our show  {'**'*20}\n")


    
   


hall1 = Hall(4,4,"CENAMETIC")
hall1.entry_show("qw1", "SUPERMAN", "Nov 2 2022 12:00 PM")
hall1.entry_show("we2", "squid game", "Nov 2 2022 12:00 PM")


while True:
    print("1. View all shows today\n2. view available seats \n3. book tickets \n4. EXIT")
    user_input = int(input("Enter you choice : "))
    if user_input==1:
        print(hall1.view_show_list())
        print()

    elif user_input==2:
        code = input("Enter show code to view avaible seats : ")
        print(hall1.view_available_seats(code))

    elif user_input==3:
        name=input('ENTER CUSTOMER NAME: ')
        number=input('ENTER CUSTOMER PHONE NUMBER: ')
        show_id=input('ENTER SHOW ID: ')
        tickets= int(input("Number of Tickets: ")) 
        booked_seat_list=[]
        for i in range(tickets):
            seat_row= int(input(f"Enter Row Number (for Ticket {i+1}) : "))
            seat_col= int(input(f"Enter Column Number (for Ticket {i+1}) : "))
            booked_seat_list.append(tuple((seat_row, seat_col)))
       

        hall1.book_seats(name,number,show_id,booked_seat_list)  
  
    elif user_input==4:
        break







