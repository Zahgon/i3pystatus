from i3pystatus import IntervalModule
from i3pystatus.core.command import run_through_shell

__author__ = 'facetoe'


class OpenVPN(IntervalModule):
    """
    Monitor OpenVPN connections.

    .. note::
        This module currently only supports systemd. Additionally, as of
        OpenVPN 2.4 the unit names have changed, as the OpenVPN server and
        client now have distinct unit files (``openvpn-server@.service`` and
        ``openvpn-client@.service``, respectively). Those who have updated to
        OpenVPN 2.4 will need to manually set the ``status_command``,
        ``vpn_up_command``, and ``vpn_down_command``.

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

    use_new_service_name = False
    status_command = "bash -c 'systemctl show openvpn@%(vpn_name)s | grep ActiveState=active'"
    vpn_up_command = "sudo /bin/systemctl start openvpn@%(vpn_name)s.service"
    vpn_down_command = "sudo /bin/systemctl stop openvpn@%(vpn_name)s.service"

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
        ("use_new_service_name", "Use new openvpn service names (openvpn 2.4^)"),
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
