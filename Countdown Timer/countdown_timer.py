import time

def countdown(timer = 0):
    """Enter time in seconds."""
    while timer:
        minutes, seconds = divmod(timer, 60)
        print("{:2d}:{:02d}".format(minutes, seconds), end="\r")
        time.sleep(1)
        timer -= 1
    
    print("Time's up!")
