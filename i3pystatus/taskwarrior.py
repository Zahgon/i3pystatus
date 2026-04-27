from i3pystatus import IntervalModule
from json import loads
import subprocess


class Taskwarrior(IntervalModule):
    """
    Check Taskwarrior for pending tasks
    Requires `json`

    .. rubric:: Available formatters (uses :ref:`formatp`)

    * `{ready}`   â€” contains number of tasks returned by `ready_filter`
    * `{urgent}`  â€” contains number of tasks returned by `urgent_filter`
    * `{next}`    â€” contains the description of next task
    * `{project}` â€” contains the projects the next task belongs to

    .. rubric:: Available callbacks

    * ``get_next_task`` â€” Display the next most urgent task.
    * ``get_prev_task`` â€” Display the previous most urgent task.
    * ``reset_next_task`` â€” Display the most urgent task, resetting any \
            switching by other callbacks.
    """

    format = 'Task: {next}'
    ready_filter = '+READY'
    urgent_filter = '+TODAY'
    enable_mark_done = False
    color_urgent = '#FF0000'
    color_ready = '#78EAF2'
    ready_tasks = []
    urgent_tasks = []
    current_tasks = []
    next_id = 0
    next_task = None

    on_upscroll = "get_prev_task"
    on_downscroll = "get_next_task"
    on_rightclick = 'mark_task_as_done'
    on_leftclick = "reset_next_task"

    settings = (
        ('format', 'format string'),
        ('ready_filter', 'Filters to get ready tasks example: `+READY`'),
        ('urgent_filter', 'Filters to get urgent tasks example: `+TODAY`'),
        ('enable_mark_done', 'Enable right click mark task as done'),
        ('color_urgent', '#FF0000'),
        ('color_ready', '#78EAF2')
    )

    def reset_next_task(self):
        pass

    def get_next_task(self):
        pass

    def get_prev_task(self):
        pass

    def mark_task_as_done(self):
        pass

    def run(self):
        pass
