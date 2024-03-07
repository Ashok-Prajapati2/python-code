import time

start_time = time.time()

for i in range(100000):
    
    if i % 2 == 0:
       
        print(i)
    

end_time = time.time()
execution_time = end_time - start_time

print(f"Execution time: {execution_time} seconds")