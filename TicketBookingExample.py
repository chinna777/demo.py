from threading import *
class BusBooking():
    def __init__(self,availableTickets):
        self.availableTickets=availableTickets
        self.l=Semaphore()
    def booking(self,total_tickets_needed):
        self.l.acquire()
        if (self.availableTickets >= total_tickets_needed):
            print('booking under process')
            print('waiting for payment')
            print('sucessfully booked')
            print(current_thread().getName())
            self.availableTickets=self.availableTickets-total_tickets_needed
            self.l.release()
        else :
            print('the no of tickets available are ',self.availableTickets)
            print(current_thread().getName())
            
        
            
b=BusBooking(10)
t=Thread(target=b.booking(5))
t.start()
t1=Thread(target=b.booking(5))
t1.start()
t2=Thread(target=b.booking(6))
t2.start()