class MyCalenderII {
    constructor() {
        this.events = [];
        this.doubleBookings = [];
    }

    // 0-------15
    //.    10-------20
    //.    10--15 doubleBooking
    //.       12----25

    book(startTime, endTime) {
        // check for double booking
        for (let [doubleBookingStart, doubleBookingEnd] of this.doubleBookings) {
            const maxStart = Math.max(doubleBookingStart, startTime);
            const minEnd = Math.min(doubleBookingEnd, endTime);

            if (maxStart < minEnd) return false;
        }
        // add to double booking
        for (let [eventStart, eventEnd] of this.events) {
            const maxStart = Math.max(eventStart, startTime);
            const minEnd = Math.min(eventEnd, endTime);

            if (maxStart < minEnd) this.doubleBookings.push([maxStart, minEnd]);
        }

        // add to events
        this.events.push([startTime, endTime]);
        return true;
    }
}