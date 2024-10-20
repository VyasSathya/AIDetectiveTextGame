# world_time.py

class WorldTime:
    def __init__(self):
        self.current_time = 0

    def advance_time(self, steps=1):
        """
        Move the time forward by a given number of steps.
        """
        self.current_time += steps
        print(f"Time advanced: {self.current_time}")