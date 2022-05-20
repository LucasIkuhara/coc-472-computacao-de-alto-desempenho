#!/bin/python3
import sys
import subprocess
from timeit import timeit


program = sys.argv[1]
print(f"Evaluating {program}")
print(f"logging at {program.split('.')[0]}.log")


for n in range(1):
    time = timeit(

    )
    response = subprocess.run(
        
            # "time",
            f'./{program}',
            # 'date',
            f'{n+1}'
        # "time ls -la", shell=True
    )

    # time = response.decode("utf-8").split('\n')
    
    print(time)
    print('eRRR')
    # print(response.stderr)

    # if(response.stderr):
        # break

    with open(f"{program.split('.')[0]}.log", 'a') as log_file:
        log_file.write(f"{n}: ah\n")
