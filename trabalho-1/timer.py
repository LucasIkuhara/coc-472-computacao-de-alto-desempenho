# %%
import sys
import subprocess
import time


program = sys.argv[1]
print(f"Evaluating {program}")
print(f"logging at {program.split('.')[0]}.log")
# subprocess.run('ulimit -s unlimited', shell=True)

# %%
# Log of execution of programs


with open(f"{program.split('.')[0]}.log", 'w') as log_file:
    log_file.write("n,time_in_mil\n")


def log_time(time: float, n: int):
    line = f"{n},{time:.3f}"

    with open(f"{program.split('.')[0]}.log", 'a') as log_file:
        log_file.write(f"{line}\n")


def log_performance(program: str):

    for n in range(1, 10000000, 1000):
        start = time.time()
        response = subprocess.Popen([f'./{program}', str(n)])
        response.wait()

        if(response.stderr):    
            print('Broke')

        delta = time.time() - start
        log_time(delta, n)


# %%


log_performance('c.out')
# log_time('')
