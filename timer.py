import time

class Timer:
    
    def wait(self, seconds):
        start_time = time.time()
        while(seconds - (time.time() - start_time) > 0):
            continue
        return 0