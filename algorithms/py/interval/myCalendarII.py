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