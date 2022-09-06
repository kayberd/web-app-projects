from .Conflict import Conflict


class RoomConflict(Conflict):

    def __init__(self, conflict_type, room, instructor, attendee, time_slot, event_list):
        super().__init__(conflict_type, room, instructor, attendee)
        self.time_slot = time_slot
        self.event_list = event_list

    def __str__(self):
        a = f"Room Conflict for {self.room} at {self.time_slot}:{self.offset} for events: "

        for event in self.event_list:
            a += f"{event} "

        return a
