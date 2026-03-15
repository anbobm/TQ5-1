

import time
 
for i in range(1, 11):
    print(f"\rLade: {i*10}%", end="")
    time.sleep(0.7)
 
print("\nFertig!")

