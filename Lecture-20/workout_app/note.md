Workout class
  attributes
    - icon
    - start
    - end
    - kind_of_workout
  methods
  - __ init __
  - get_calories
  -get_start
  -get_end
  -set_start
  -set_end


##  modifiying the class
- get_calories() method has to be made base s on what the idea of a calrorie is and how a calorie is used.
- The init function takes a `calories=None`` parameter and the `self.calories = calories`
- We add a cal_per_hour variable  =200
self.start and self.end parameters are going to be string parameters and then parsed in the body since they would be datetime objects
- You can subtract datetime objects
- You can get `total_minutes()` and `total_hours()` methods etc `from dateutil import parser`
