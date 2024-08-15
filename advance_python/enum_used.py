from enum import Enum

class basic(Enum):
    START = 1
    PROCESSING = 2
    COMPLETED = 3
    FAILED = 4
    
    
obj = basic(4)
print(obj.__dict__)