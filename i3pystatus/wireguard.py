from i3pystatus import IntervalModule
from i3pystatus.core.command import run_through_shell

__author__ = 'Pluggi'


class Wireguard(IntervalModule):
    """
    Monitor Wireguard connections.

    .. note::
        You might want to add something like this to /etc/sudoers:

        ``%wheel ALL = NOPASSWD: /bin/systemctl start wg-quick@wg0.service,/bin/systemctl stop wg-quick@wg0.service``

    Formatters:

    * {vpn_name} â€” Same as setting.
    * {status} â€” Unicode up or down symbol.
    * {output} â€” Output of status_command.
    * {label} â€” Label for this connection, if defined.

    """

    color_up = "#00ff00"
    color_down = "#FF0000"
    status_up = 'â–²'
    status_down = 'â–¼'
    format = "{vpn_name} {status}"

    status_command = "systemctl is-active wg-quick@{vpn_name}"
    vpn_up_command = "sudo /bin/systemctl start wg-quick@{vpn_name}.service"
    vpn_down_command = "sudo /bin/systemctl stop wg-quick@{vpn_name}.service"

    connected = False
    label = ''
    vpn_name = ''

    settings = (
        ("format", "Format string"),
        ("color_up", "VPN is up"),
        ("color_down", "VPN is down"),
        ("status_down", "Symbol to display when down"),
        ("status_up", "Symbol to display when up"),
        ("vpn_name", "Name of VPN"),
        ("vpn_up_command", "Command to bring up the VPN - default requires editing /etc/sudoers"),
        ("vpn_down_command", "Command to bring up the VPN - default requires editing /etc/sudoers"),
        ("status_command", "command to find out if the VPN is active"),
    )

    def init(self):
        pass

    def toggle_connection(self):
        pass

    def on_click(self, button, **kwargs):
        pass

    def run(self):
        pass
