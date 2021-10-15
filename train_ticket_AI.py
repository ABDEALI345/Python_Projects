'''
1 2 3 4 5 6 7 8 9 10
'''

class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats
        i = 1
        self.avlSeats=[]
        for i in range(1,self.seats+1):
            self.avlSeats.append(i)

    def getStatus(self):
        print("************")
        print(f"The name of the train is {self.name}")
        print(f"The seats available in the train are {self.seats}")
        print("************")

    def fareInfo(self):
        print(f"The price of the ticket is: Rs {self.fare}")

    def bookTicket(self):
        if(self.seats>0):
            print(f"Your ticket has been booked! Your seat number is {self.avlSeats.pop(self.seats-1)}")
            self.seats = self.seats - 1
        else:
            print("Sorry this train is full! Kindly try in tatkal")

    def cancelTicket(self, seatNo):
        self.avlSeats.append(seatNo)
        self.seats = self.seats + 1
        print(f"your ticket bearing number {seatNo} has been cancelled")
        print("************")

intercity = Train("Intercity Express: 14015", 90, 10)
intercity.getStatus() 
intercity.bookTicket()
intercity.bookTicket()
intercity.bookTicket()
intercity.getStatus()
intercity.cancelTicket(10)
intercity.bookTicket()
intercity.bookTicket()
