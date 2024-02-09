import time
from datetime import datetime

def hello_world(i : int, r: int):
    for i in range(i):
        # Get current time with milliseconds
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        print(f"{current_time} - Hello, World {r} and {i+1} time! rev")
        time.sleep(1)  # Sleep for 1 second between messages