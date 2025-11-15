"""Run_workout module subclass for Workout """
from workout import Workout


class RunWorkout(Workout):
# pylint: disable=C0114
    def __init__(self, start_time, end_time, elev):
        super().__init__(start_time, end_time, calories =None)
        self.icon = "..."
        self.kind = "Running"
        self.elev = elev

    def set_elev(self, e):
        self.elev = e
    def get_elev(self):
        return self.elev


print(dir(RunWorkout))
