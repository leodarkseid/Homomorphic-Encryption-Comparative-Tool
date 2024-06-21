import tracemalloc
import time
import inspect
from rich.progress import track

from rich.console import Console

console = Console()

class Measure:
    def __init__(self) -> None:
        self.result = ''
        self.time = 0
       
        
    def measure_memory_time(self, func, *args, **kwargs):
        # Start tracing memory allocations
        # func can either be a class or function
        tracemalloc.start()
        
        
        # Take a snapshot before running the function
        snapshot1 = tracemalloc.take_snapshot()

        # Measure start time
        
        # start_time = time.time()

        # Run the function
        desc = kwargs.get('desc', func.__name__)
        with console.status(f'[bold green] Processing {desc}', spinner='aesthetic') as status:
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            self.result = result
            status.stop()
            pass


        
        if inspect.isfunction(func):
            self.time = result['time']
            
        elif inspect.isclass(func):
            self.time = result.initTime

        if self.time == 0:
            self.time = end_time-start_time
        # for _ in track(range(int(self.time)), description=f'[green]Processing {desc}'):
        #     pass
            # time.sleep(0.5)
        # Measure end time
        # end_time = time.time()

        # Take a snapshot after running the function
        snapshot2 = tracemalloc.take_snapshot()
       
        # Stop tracing memory allocations
        tracemalloc.stop()
        
        # # Compute the difference in memory usage
        stat_diff = snapshot2.compare_to(snapshot1, 'lineno')
        total_memory = sum(stat.size_diff for stat in stat_diff)
        self.memory = total_memory
        
        # print(f"Total memory used by '{func.__name__}' function: {total_memory / 1024} KiB")
        # print(f"Execution time of '{func.__name__}' function: {self.time} seconds")
    
        return {"result":result, "memory":total_memory, "time":self.time}