import random
import time 
from rich.console import Console

console = Console()

class DistributedRandom:
    def __init__(self, client:int = 1000, min_amount:int = 0, max_amount:int = 3000000, distribution:int = 1000000) -> None:
        # if max_amount / distribution < client or distribution/max_amount >= 0.5:
        #     raise ValueError("sample size is not large enough for the specified amount of client")
      
        with console.status("[bold green]Computing generated numbers...", spinner_style="moon") as status:
            self.possibilityList = []
            self.count = 0
            self.client = client
            self.distribution = distribution
            iteration = 0
            max_iterations = 100 * client
            max
            while len(self.possibilityList) < client:
                if iteration >= max_iterations:
                    raise RuntimeError("Reached maximum iterations without finding sufficient numbers.")
                x = random.randint(min_amount, max_amount)
                if len(self.possibilityList) == 0:
                    self.possibilityList.append(x)
                else:
                    if self.checkNumber(x, self.possibilityList[len(self.possibilityList)-1]):
                        self.possibilityList.append(x) 
                        # print('list',sorted(self.possibilityList))
                iteration += 1
        # console.log(f'[bold][red]Done Generating Distributed Numbers!')
            status.stop()
        time.sleep(1)
                        

    def checkNumber(self, x, y):
        r = x -y
        if r >= self.distribution:
            return True
        elif y - x >= self.distribution:
            return True
    def next(self):
        result = self.possibilityList[self.count]
       
        self.count = self.count + 1 if self.client - self.count > 1 else 0
        return result
        
