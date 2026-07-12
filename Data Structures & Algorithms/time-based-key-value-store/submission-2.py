class TimeMap:

    def __init__(self):
        self.kv = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.kv:
            self.kv[key] = []
        self.kv[key].append((value,timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.kv[key]) - 1
        arr = self.kv[key]
        res = ""

        while l<=r:
            m = (l+r)//2
            if arr[m][1] <= timestamp:
                l = m+1
                res = arr[m][0]
            else:
                r = m-1
        return res
        
