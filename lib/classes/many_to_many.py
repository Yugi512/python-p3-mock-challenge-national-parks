class NationalPark:

    def __init__(self, name):
        self.name = name
        
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        is_false = hasattr(self,"name")
        if isinstance(name, str) and 3 <= len(name) and is_false == False:
            self._name = name
        else:
            raise Exception("nah")

    def trips(self):
        trips_list = []
        all_trips = Trip.all
        for trip in all_trips:
            if trip.national_park == self:
                trips_list.append(trip)
        return trips_list
    
    def visitors(self):
        unique_list = []
        all_trips = Trip.all
        for trip in all_trips:
            if trip.national_park == self and trip.visitor not in unique_list:
                unique_list.append(trip.visitor)  
        return unique_list
    
    def total_visits(self):
        return len(self.trips())    

    
    def best_visitor(self):
        visit_dict = {}
        all_trips = Trip.all
        for trip in all_trips:
            if trip.national_park == self:
                print(trip.visitor.total_visits_at_park(self))


#  trip_dict = {}
#         all_trips = Trip.all
#         if self.name not in trip_dict:
#             trip_dict[self.name] = 0
#         for trip in all_trips:
#             if park == trip.national_park and self == trip.visitor:
#                 trip_dict[self.name] += 1
#         return trip_dict
class Trip:
    all = []
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        self.all.append(self)
    
    @property
    def start_date(self):
        return self._start_date
    
    @start_date.setter
    def start_date(self, start_date):
        if isinstance(start_date, str) and 7 <= len(start_date) and " " in start_date:
            self._start_date = start_date
        else:
            raise Exception("nah")
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        if isinstance(end_date, str) and 7 <= len(end_date) and " " in end_date:
            self._end_date = end_date
        else:
            raise Exception("nah")

    @property
    def visitor(self):
        return self._visitor

    @visitor.setter
    def visitor(self,visitor):
        is_false = hasattr(self,"visitor")
        if isinstance(visitor, Visitor) and is_false == False:
            self._visitor = visitor
        else:
            raise Exception("nah")
            
    @property
    def national_park(self):
        return self._national_park 
    
    @national_park.setter
    def national_park(self, national_park):
        is_false = hasattr(self,"national_park")
        if isinstance(national_park, NationalPark) and is_false == False:
            self._national_park = national_park
        else:
            raise Exception("nah")

    

class Visitor:

    def __init__(self, name):
        self.name = name
        
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise Exception("nah")

    def trips(self):
        trips_list = []
        all_trips = Trip.all
        for trip in all_trips:
            if trip.visitor == self:
                trips_list.append(trip)
        return trips_list
    
    def national_parks(self):
        unique_list = []
        all_trips = Trip.all
        for trip in all_trips:
            if trip.visitor == self and trip.national_park not in unique_list:
                unique_list.append(trip.national_park)  
        return unique_list

    def total_visits_at_park(self, park):
        trip_dict = {}
        all_trips = Trip.all
        if self.name not in trip_dict:
            trip_dict[self.name] = 0
        for trip in all_trips:
            if park == trip.national_park and self == trip.visitor:
                trip_dict[self.name] += 1
        return trip_dict
