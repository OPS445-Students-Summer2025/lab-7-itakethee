#!/usr/bin/env python3
# Student ID: pshah116

class Time:
    """Simple object type for time of the day.
       Data attributes: hour, minute, second
       Function attributes: __init__, __str__, __repr__,
                            __add__, time_to_sec, format_time,
                            change_time, sum_times
    """

    def __init__(self, hour=12, minute=0, second=0):
        """Constructor for time object"""
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        """Return a string representation for the object self (used by print())"""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def __repr__(self):
        """Return a string representation when object is typed in shell"""
        return f'{self.hour:02d}.{self.minute:02d}.{self.second:02d}'

    def __add__(self, t2):
        """Overload + operator to add two Time objects"""
        return self.sum_times(t2)

    def format_time(self):
        """Return time object as a formatted string"""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def sum_times(self, t2):
        """Add two Time objects and return a new Time object"""
        self_sec = self.time_to_sec()
        t2_sec = t2.time_to_sec()
        return sec_to_time(self_sec + t2_sec)

    def change_time(self, seconds):
        """Add or subtract seconds from the time object (in-place)"""
        total_sec = self.time_to_sec() + seconds
        new_time = sec_to_time(total_sec)
        self.hour, self.minute, self.second = new_time.hour, new_time.minute, new_time.second
        return None

    def time_to_sec(self):
        """Convert time object to total seconds since midnight"""
        return self.hour * 3600 + self.minute * 60 + self.second

    def valid_time(self):
        """Check for validity of the time object"""
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.minute >= 60 or self.second >= 60 or self.hour >= 24:
            return False
        return True

def sec_to_time(seconds):
    """Convert seconds since midnight to a Time object"""
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time
