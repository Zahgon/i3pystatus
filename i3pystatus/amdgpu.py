import os

from i3pystatus import IntervalModule


class Amdgpu(IntervalModule):
    """
    Shows information about gpu's using the amdgpu driver

    .. rubric :: Available formatters

    * `{temp}`
    * `{sclk}`      - Gpu clock speed
    * `{mclk}`      - Memory clock speed
    * `{fan_speed}` - Fan speed
    * `{gpu_usage}` - Gpu Usage percent
    """

    settings = (
        'format',
        'color',
        ('card', '[1, 2, ...] card to read (options are in /sys/class/drm/)')
    )

    card = 0
    color = None
    format = '{temp} {mclk} {sclk}'

    def init(self):
        pass

    def detect_hwmon(self):
        pass

    def run(self):
        pass

    @staticmethod
    def parse_clk_reading(reading):
        pass

    def get_mclk(self):
        pass

    def get_sclk(self):
        pass

    def get_temp(self):
        pass

    def get_fan_speed(self):
        pass

    def get_gpu_usage(self):
        pass
