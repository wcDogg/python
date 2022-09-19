from datetime import timedelta
from timeit import default_timer as timer
from time import strftime, localtime, sleep

# https://gist.github.com/wcDogg/4bae7cd8d840181c2829e82954358bcc

class TaskTimer:
  '''A utility class for capturing a task's processing time.
  * Uses `localtime()` for real-world start and stop times. 
  * Uses the default `perf_counter()` for relative elapsed time.
  '''
  def __init__(self) -> None:

    self.start_timer = None
    self.time_start = None
    self.stop_timer = None
    self.time_stop = None
    self.time_elapsed = None
    self.time_summary = {'time_start': None, 'time_stop': None, 'time_elapsed': None}

  def start(self) -> None:
    '''Start the timer and capture the start time.
    '''
    self.start_timer = timer()
    self.time_start = strftime("%Y-%m-%d %H:%M:%S", localtime())
    self.time_summary['time_start'] = self.time_start

  def stop(self) -> None:
    '''Stop the timer and capture the stop time.
    '''
    self.stop_timer = timer()
    self.time_stop = strftime("%Y-%m-%d %H:%M:%S", localtime())
    self.time_summary['time_stop'] = self.time_stop

  def elapsed(self) -> None:
    '''Calculates the elapsed time.
    '''
    elapsed = timedelta(seconds=self.stop_timer-self.start_timer)
    elapsed = elapsed - timedelta(microseconds=elapsed.microseconds)
    self.time_elapsed = str(elapsed)
    self.time_summary['time_elapsed'] = self.time_elapsed

  def summary(self) -> dict:
    '''Returns a dictionary with start, stop, and elapsed time.
    '''
    return self.time_summary

  def print(self) -> None:
    '''Prints timer summary to console.
    '''
    for k in self.time_summary:
      print(f'{k}: {self.time_summary[k]}')


# --------------------------
# Example usage
# --------------------------
class Task:

  def __init__(self) -> None:

    self.timer = TaskTimer()
    self.run()

  def run(self) -> None:

    self.timer.start()
    sleep(3)
    self.timer.stop()
    self.timer.elapsed()
    self.timer.summary()
    self.timer.print()

if __name__ == "__main__":

  task = Task()

