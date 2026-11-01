class TimeMap:

    def __init__(self):
        self.moods = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.moods:
            self.moods[key] = []

        self.moods[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.moods:
            return ""
            
        vals = self.moods[key]
        l = 0
        r = len(vals) - 1
        ret = ""
        

        while l <= r:
            m = (l + r) // 2
            mid_time, mid_val = vals[m]
            if mid_time == timestamp:
                return mid_val
            elif mid_time <= timestamp:
                l = m + 1
                ret = mid_val
            else:
                r = m - 1

        return ret
        
