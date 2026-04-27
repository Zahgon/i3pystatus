import threading
import time
import sys
from i3pystatus.core.util import partition

timer = time.perf_counter if hasattr(time, "perf_counter") else time.clock


def unwrap_workload(workload):
    """ Obtain the module from it's wrapper. """
    pass


class Thread(threading.Thread):
    def __init__(self, target_interval, workloads=None, start_barrier=1):
        super().__init__()
        self.workloads = workloads or []
        self.target_interval = target_interval
        self.start_barrier = start_barrier
        self._suspended = threading.Event()
        self.daemon = True

    def __iter__(self):
        return iter(self.workloads)

    def __len__(self):
        return len(self.workloads)

    def pop(self):
        pass

    def append(self, workload):
        pass

    @property
    def time(self):
        pass

    def wait_for_start_barrier(self):
        pass

    def execute_workloads(self):
        pass

    def should_execute(self, workload):
        """
        If we have been suspended by i3bar, only execute those modules that set the keep_alive flag to a truthy
        value. See the docs on the suspend_signal_handler method of the io module for more information.
        """
        pass

    def run(self):
        pass

    def branch(self, vtime, bound):
        pass

    def suspend(self):
        pass

    def resume(self):
        pass


class Wrapper:
    def __init__(self, workload):
        self.workload = workload

    def __repr__(self):
        return repr(self.workload)


class ExceptionWrapper(Wrapper):
    def __call__(self):
        try:
            self.workload()
        except:
            message = "Exception in {thread} at {time}, module {name}".format(
                thread=threading.current_thread().name,
                time=time.strftime("%c"),
                name=self.workload.__class__.__name__
            )
            if hasattr(self.workload, "logger"):
                self.workload.logger.error(message, exc_info=True)
            self.workload.output = {
                "full_text": self.format_exception(),
                "color": "#FF0000",
            }

    def format_exception(self):
        pass

    def truncate_error(self, exception_message):
        pass


class WorkloadWrapper(Wrapper):
    time = 0.0

    def __call__(self):
        tp1 = timer()
        self.workload()
        self.time = timer() - tp1


class Manager:
    def __init__(self, target_interval):
        self.target_interval = target_interval
        self.upper_bound = target_interval * 1.1
        self.lower_bound = target_interval * 0.7

        initial_thread = Thread(target_interval, [self.wrap(self)])
        self.threads = [initial_thread]

    def __call__(self):
        separate = []
        for thread in self.threads:
            separate.extend(thread.branch(thread.time, self.upper_bound))
        self.create_threads(self.partition_workloads(separate))

    def __repr__(self):
        return "Manager"

    def wrap(self, workload):
        pass

    def partition_workloads(self, workloads):
        pass

    def create_threads(self, threads):
        pass

    def create_thread(self, workloads):
        pass

    def append(self, workload):
        pass

    def start(self):
        pass

    def suspend(self):
        pass

    def resume(self):
        pass
