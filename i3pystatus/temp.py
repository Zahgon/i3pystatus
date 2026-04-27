from i3pystatus import IntervalModule
from i3pystatus.core.color import ColorRangeModule
from i3pystatus.core.util import make_vertical_bar


class Sensor:
    """
    Simple class representing a CPU temperature sensor.
    """

    def __init__(self, name, current, maximum, critical):
        self.name = name.replace(' ', '_')
        self.current = int(current)
        self.maximum = int(maximum) if maximum else int(critical)
        self.critical = int(critical)

    def __repr__(self):
        return "Sensor(name='{}', current={}, maximum={}, critical={})".format(
            self.name,
            self.current,
            self.maximum,
            self.critical
        )

    def is_warning(self):
        pass

    def is_critical(self):
        pass


def get_sensors():
    """ Detect and return a list of Sensor objects """
    pass


class Temperature(IntervalModule, ColorRangeModule):
    """
    Shows CPU temperature of Intel processors.

    AMD is currently not supported as they can only report a relative temperature, which is pretty useless.

    Requires `colour` module from PyPi

    .. rubric:: Modes of operation

    If lm_sensors_enabled is set to False, the module operates in default mode. This means that:
        * only the {temp} formatter is available
        * alert_temp is honored

    If lm_sensors_enabled is set to True, the module operates in lm_sensors mode. This means that:
        * pysensors must be installed (https://github.com/bastienleonard/pysensors)
        * CPU sensors are discovered dynamically (supporting a sensor per core and multiple CPUs)
        * alert_temp is ignored. The warning or critical values reported by the sensor are used instead (see urgent_on)

    .. rubric:: lm_sensors installation

    In order to take advantage of the lm_sensors library and tools, it must first be installed and configured.

    On Arch this is as simple as:

    .. code-block:: bash

        pacman -S lm_sensors


    On Ubuntu:

    .. code-block:: bash

        sudo apt-get update && sudo apt-get install lm-sensors libsensors4-dev


    The Arch Wiki has a good page on the library - https://wiki.archlinux.org/index.php/lm_sensors

    .. rubric:: lm_sensors_mode formatters

    When ``lm_sensors_enabled`` is True the formatters are created dynamically. In order to discover the formatters that
    are available, it is best to run the sensors command:

    .. code-block:: bash

        â‡’ sensors
        coretemp-isa-0000
        Adapter: ISA adapter
        Physical id 0:  +48.0Â°C  (high = +80.0Â°C, crit = +99.0Â°C)
        Core 0:         +48.0Â°C  (high = +80.0Â°C, crit = +99.0Â°C)
        Core 1:         +46.0Â°C  (high = +80.0Â°C, crit = +99.0Â°C)
        Core 2:         +43.0Â°C  (high = +80.0Â°C, crit = +99.0Â°C)
        Core 3:         +47.0Â°C  (high = +80.0Â°C, crit = +99.0Â°C)

    The module replaces spaces in sensor names with underscores, therefore from the above output we can
    identify the following sensor formatters:

    * Physical_id_0
    * Core_0
    * Core_1
    * Core_2
    * Core_3

    For each sensor a vertical bar is also generated. In this example we would also have the following bars:

    * Physical_id_0_bar
    * Core_0_bar
    * Core_1_bar
    * Core_2_bar
    * Core_3_bar

    Thus, this format string would be valid: "{Physical_id_0}Â°C {Core_0_bar}{Core_1_bar}{Core_2_bar}{Core_3_bar}"

    .. rubric:: Pango Markup and lm_sensors_mode

    When Pango Markup is enabled and ``dynamic_color`` is True, each sensor's formatter color is displayed independently.
    The color is determined by the proximity of the sensors current value to it's critical value.

    .. rubric:: Example Configuration

    Here is an example configuration based on the sensor values discovered above:

    .. code-block:: python

        status.register("temp",
                        format="{Physical_id_0}Â°C {Core_0_bar}{Core_1_bar}{Core_2_bar}{Core_3_bar}",
                        hints={"markup": "pango"},
                        lm_sensors_enabled=True,
                        dynamic_color=True)
    """

    settings = (
        ("format",
         "format string used for output. {temp} is the temperature in degrees celsius"),
        ('display_if', 'snippet that gets evaluated. if true, displays the module output'),
        ('lm_sensors_enabled', 'whether or not lm_sensors should be used for obtaining CPU temperature information'),
        ('urgent_on', 'whether to flag as urgent when temperature exceeds urgent value or critical value '
                      '(requires lm_sensors_enabled)'),
        ('dynamic_color', 'whether to set the color dynamically (overrides alert_color)'),
        "color",
        "file",
        "alert_temp",
        "alert_color",
    )
    format = "{temp} Â°C"
    color = "#FFFFFF"
    file = "/sys/class/thermal/thermal_zone0/temp"
    alert_temp = 90
    alert_color = "#FF0000"
    display_if = 'True'

    lm_sensors_enabled = False
    dynamic_color = False
    urgent_on = 'warning'

    def init(self):
        pass

    def run(self):
        pass

    def get_output_original(self):
        """
        Build the output the original way. Requires no third party libraries.
        """
        pass

    def get_output_sensors(self):
        """
        Build the output using lm_sensors. Requires sensors Python module (see docs).
        """
        pass

    def get_urgent(self, sensors):
        """ Determine if any sensors should set the urgent flag. """
        pass

    def format_sensor(self, sensor):
        """ Format a sensor value. If pango is enabled color is per sensor. """
        pass

    def format_sensor_bar(self, sensor):
        """ Build and format a sensor bar. If pango is enabled bar color is per sensor."""
        pass

    def format_pango(self, color, value):
        pass

    def get_colour(self, percentage):
        pass
