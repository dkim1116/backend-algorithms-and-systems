# You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a triple booking.

# A triple booking happens when three events have some non-empty intersection (i.e., some moment is common to all the three events.).

# The event can be represented as a pair of integers startTime and endTime that represents a booking on the half-open interval [startTime, endTime), the range of real numbers x such that startTime <= x < endTime.

# Implement the MyCalendarTwo class:

# MyCalendarTwo() Initializes the calendar object.
# boolean book(int startTime, int endTime) Returns true if the event can be added to the calendar successfully without causing a triple booking. Otherwise, return false and do not add the event to the calendar.

# Pattern:
#     Interval Overlap tracking problem

# Approach:
#     I keep track of intervals of bookings and doubleBookings
#     When a new event wants to be booked, we first check in doubleBookings whether it overlaps with anything in there. If so then reject
#     Then we check bookings to see if it overlaps with anything there. If so, take the maxStart and minEnd of the two intervals then add to doubleBookings
#     Then we add the new event intervals to bookings

# Time & Space complexity:
#     Time complexity is O(n) per booking, O(n^2) overall in the worst case for n bookings
#     Space complexity is O(n) per booking, O(n^2) in the worst case for n bookings

class MyCalendarTwo:
    def __init__(self):
        self.doubleBooked = []
        self.events = []

    def book(self, start: int, end: int):
        for doubleStart, doubleEnd in self.doubleBooked:
            maxStart = max(start, doubleStart)
            minEnd = min(end, doubleEnd)

            if maxStart < minEnd:
                return False

        for eventStart, eventEnd in self.events:
            maxStart = max(start, eventStart)
            minEnd = min(end, eventEnd)

            if (maxStart < minEnd):
                self.doubleBooked.append([maxStart, minEnd])

        self.events.append([start, end])

        return True