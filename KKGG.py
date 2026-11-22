class Time:
    def __init__(self,hours,minute,second):
        self.hours=hours
        self.minute=minute
        self.second=second

    def __add__(self, other):
        return Time(self.hours+other.hours,self.minute+other.minute,self.second+other.second)

    # с пунктом str помогал ии
    def __str__(self):
        minute=self.minute+self.second//60
        second=self.second%60
        hours=self.hours+self.minute//60
        minute=minute%60
        hours=hours//24
        return f"{hours:02d}:{minute:02d}:{second:02d}"
t1=Time(12,33,3)
t2=Time(13,33,59)
print(t1+t2)