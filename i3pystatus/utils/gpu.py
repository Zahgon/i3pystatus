import subprocess
from collections import namedtuple
from typing import Optional


class GPUNotFoundError(Exception):
    """nvidia-smi call exited with a error code"""
    pass


GPUUsageInfo = namedtuple('GPUUsageInfo', ['total_mem', 'avail_mem', 'used_mem',
                                           'temp', 'percent_fan',
                                           'usage_gpu', 'usage_mem'])


def _convert_nvidia_smi_value(value) -> Optional[int]:
    pass


def query_nvidia_smi(gpu_number) -> GPUUsageInfo:
    """
    :return:
        all memory fields are in megabytes,
        temperature in degrees celsius,
        fan speed is integer percent from 0 to 100 inclusive,
        usage_gpu and usage_mem are integer percents from 0 to 100 inclusive
        (usage_mem != used_mem, usage_mem is about read/write access load)
        read more in 'nvidia-smi --help-query-gpu'.

        Any field can be None if such information is not supported by nvidia-smi for current GPU

        Returns None if call failed (no nvidia-smi or query format was changed)

        Raises exception with readable comment
    """
    pass
