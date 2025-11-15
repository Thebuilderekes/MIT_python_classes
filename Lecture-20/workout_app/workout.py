from dateutil import parser


class Workout():
# pylint: disable=C0114
    cal_per_hour = 200 # note that this variable is accessible in all instances of Workout class
    def __init__(self, start_time, end_time, calories =None):
        self.kind =""
        self.icon =""
        self.start_time = parser.parse(start_time)
        self.end_time = parser.parse(end_time)
        self.calories = calories


    def get_calories(self):
        if self.calories is None:
            return Workout.cal_per_hour* (self.end_time - self.start_time).total_seconds()/3600
        return self.calories

    def get_start_time(self):
        return self.start_time

    def get_end_time(self):
        return self.end_time

    def set_start_time(self, time):
        self.start_time = time

    def set_end_time(self, time):
        self.end_time = time

w = Workout('Nov 14 2025 7:00pm', 'Nov 14 2025 8:00pm'  )

result = w.get_calories()
print(result)
