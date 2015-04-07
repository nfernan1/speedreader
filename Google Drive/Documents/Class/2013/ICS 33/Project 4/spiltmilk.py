


#Nicholas Fernando 12659548
import queue33



class Customer:
    def __init__(self, arrivaltime):
        self.arrivaltime = arrivaltime
        self.windowarrivaltime = None
        
    def __repr__(self):
        return 'Customer'
        
    
    
class Ticket_line:
    def __init__(self, ticketnum):
        self._queue = queue33.Queue()
    

    def add_customer(self, customer, time):
        'Customer enters ticket line'
    
        self.time = time
        self._queue.enqueue(customer)

    def remove_customer(self):
        'Customer leaves ticket line'
        self.check_line()
        self._queue.dequeue()
            
    def check_line(self):
        'Checks if line is empty'
        
        return len(self._queue) == 0
   
        
    def check_front(self):
        # Check front first and then keep their reference
        return self._queue.front()
    
    def __len__(self):
        return len(self._queue)
    
    def __repr__(self):
        'Represents the current customers in the line'
        return '{}'.format(self._queue)
    

 
class Ticket_window:
    def __init__(self, process_time, ticketline:'Ticket_Line object'):
        self._process_time = process_time
        self._customer = None
        self._arrival_time = None
        self._line = ticketline
        self._idle_time = 0

    def idle(self):
        if self._customer == None:
            self._idle_time += 1
            return True
        else:
            return False



    def pass_customer(self, time):
        if not self._line.check_line():
            front = self._line.check_front()
            self._line.remove_customer()
            self.add_customer(front,time)
            
    
    def add_customer(self, customer, time):
        self._arrival_time = time
        self._customer = customer
        

    def remove_customer(self):
        self._customer = None
        self_arrival_time = None

    def __len__(self):
        return len(self._line)
    
    def __repr__(self):
        return '{} {} {} {}'.format(self._process_time,self._customer,self._arrival_time,self._line)


    
class Theater:
    def __init__(self, windowtime,is_singleline):
        
        self._windowlist = []
        self._is_singleline = is_singleline
        self.line = Ticket_line()
        self.windowtime = windowtime

        if self._is_singleline:
            ticketline = Ticket_line()
            ticketindex = 1 
            for i in windowtime:
                windows = Ticket_window(i, ticketindex)
                self._windowlist.append(windows)


        else:
            
            for i in windowtime:
                window = Ticket_window(i,ticketline)
                self._windowlist.append(window)


        
    def __repr__(self):
        return '{}'.format(self._windowlist)


    def add_customer(self, numcr, time):
        'Adds customer to the shortest line'
        customer = int(numcr)

        for i in range(customer):
            
            shortest_line = self.find_shortest_line()
            shortest_line.add_customer(customer,time)
            
        for idx in range(len(self.line)):
            print('TIME  {} - Customer entered line #{}'.format(time,idx))


    def find_shortest_line(self):
        'Find shortest window for customer to go into'
        #should return the shortest window and the time it has
        min_idx = 0

        for cur_idx in range(len(self._windowlist)):
            if len(self._windowlist[cur_idx]._line) < len(self._windowlist[min_idx]._line):
                min_idx = cur_idx

        return self._windowlist[min_idx]._line
        

class Clock:
    
    def __init__(self):
        self._time = 0

    def currenttime(self):
        return int(self._time)
    
    def clockwise(self):
        self._time += 1
    
    def __repr__(self):
        return '{}'.format(self._time)


    
class Simulation:
    def __init__(self):
        self.moveclock = Clock()
        
    def configinfo(self):

        windowtimes = []
        config = []
        f =  open('simulation.txt', 'r')

        message = f.readline().strip()
        opentime = int(f.readline())
        winamount = int(f.readline())
        is_single = f.readline() == 'S'
       

        for time in range(winamount):
            windowtimes.append(int(f.readline().strip()))
        
        self.theater = Theater(windowtimes,is_single)
        
        return message, opentime, winamount, is_single, windowtimes

        
    
    def arrivalinfo(self):

        tmp = []
        arrivalinfo = []

        f =  open('simulation.txt','r')
        
        for i in range(self.configinfo()[2]+4):
            f.readline()

        for line in f:
            tmp.append(tuple(line.strip().split()))

        endsimulation = tmp[-1][0]

        #list of tuples: customeramount & arrivaltime
        for tup in tmp:
            if len(tup) >= 2:
                arrivalinfo.append(tup)
            
        return arrivalinfo, endsimulation

        
            

    def simulationloop(self):


        simulating = True
        event = None
        count = 0
        time = self.moveclock._time
        
        while simulating:
            
            self.moveclock.clockwise()
        
            
            if self.moveclock.currenttime() == (self.configinfo()[1]*60)-1:
                simulating = False
                    
    
            if count != len(self.arrivalinfo()[0]):
                if event == None:
                    event = self.arrivalinfo()[0][count]
                    
                currentevent = event
                
                if self.moveclock.currenttime() == int(currentevent[1]):
                    
                    self.theater.add_customer(int(currentevent[0]),self.moveclock.currenttime())
                    
                    count+=1
                    event = None
            else:
                self.moveclock.clockwise()


                
            for window in self.theater._windowlist:
                if window.idle() and window._line.check_line():
                    window.pass_customer(time)


        
                
##            if self.moveclock.currenttime()+self.theater.windowtime:
##                pass

            

                    
                    
                    
    def __repr__(self):
        return'Time   {}'.format(self.moveclock)

if __name__ == '__main__':
    
    start = Simulation()
    start.configinfo()
    start.simulationloop()

    
