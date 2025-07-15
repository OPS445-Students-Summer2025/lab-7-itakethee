#!/usr/bin/env python3
# Student ID: pshah116

class Time:
    """Simple object type for time of the day.
        data attributes: hour, minute, second
        function attributes: __init__, __str__, __repr__,
                             time_to_sec, format_time,
                             change_time, sum_times
    """

    def __init__(self, hour=12, minute=0, second=0):
        """constructor for time object""" 
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        '''return a string representation for the object self'''
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def __repr__(self):
        '''return a string representation for the object self'''
        '''just instead of ':' you are required to use '.' in the formatting string.'''
        return f'{self.hour:02d}.{self.minute:02d}.{self.second:02d}'

    def format_time(self):
        """Return time object as a formatted string"""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def sum_times(self, t2):
        """Add two time objects and return the sum."""
        self_sec = self.time_to_sec()
        t2_sec = t2.time_to_sec()
        total_sec = self_sec + t2_sec
        return sec_to_time(total_sec)

    def change_time(self, seconds):
        """Add or subtract seconds from this time object."""
        time_seconds = self.time_to_sec()
        new_time = sec_to_time(time_seconds + seconds)
        self.hour, self.minute, self.second = new_time.hour, new_time.minute, new_time.second
        return None

    def time_to_sec(self):
        """Convert a time object to total seconds since midnight."""
        return self.hour * 3600 + self.minute * 60 + self.second

    def valid_time(self):
        """Check for the validity of the time object attributes."""
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.minute >= 60 or self.second >= 60 or self.hour >= 24:
            return False
        return True

def sec_to_time(seconds):
    """Convert total seconds to a Time object."""
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time
