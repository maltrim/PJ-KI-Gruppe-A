import time
from main import main

fen_str_start = ''
fen_str_mid = ''
fen_str_end = ''

def main():
  obj = main("Benchmark")

  execution_times = []
    
  execution_times_start = []
  
  for _ in range(1000):
    start_time = time.time()
    obj.determine_next_move(fen_str_start)
    end_time = time.time()
    execution_time = end_time - start_time
    execution_times_start.append(execution_time_start)

  average_execution_time_start = sum(execution_times_start) / len(execution_times_start)
  execution_times.append(average_execution_time_start)

  execution_times_mid = []
  
  for _ in range(1000):
    start_time = time.time()
    obj.determine_next_move(fen_str_mid)
    end_time = time.time()
    execution_time = end_time - start_time
    execution_times_mid.append(execution_time_start)

  average_execution_time_mid = sum(execution_times_mid) / len(execution_times_mid)
  execution_times.append(average_execution_time_mid)

  execution_times_start = []
  
  for _ in range(1000):
    start_time = time.time()
    obj.determine_next_move(fen_str_end)
    end_time = time.time()
    execution_time = end_time - start_time
    execution_times_end.append(execution_time_end)

  average_execution_time_end = sum(execution_times_end) / len(execution_times_end)
  execution_times.append(average_execution_time_end)

  return execution_times
