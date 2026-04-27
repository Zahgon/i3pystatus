from i3pystatus import IntervalModule
# requires python-novaclient
from novaclient import client
import webbrowser


class Openstack_vms(IntervalModule):
    """
    Displays the number of VMs in an openstack cluster in ACTIVE and
    non-ACTIVE states.
    Requires: python-novaclient
    """

    settings = (
        ("auth_url", "OpenStack cluster authentication URL (OS_AUTH_URL)"),
        ("username", "Username for OpenStack authentication (OS_USERNAME)"),
        ("password", "Password for Openstack authentication (OS_PASSWORD)"),
        ("tenant_name", "Tenant/Project name to view (OS_TENANT_NAME)"),
        ("color", "Display color when non-active VMs are =< `threshold`"),
        ("crit_color", "Display color when non-active VMs are => `threshold`"),
        ("threshold", "Set critical indicators when non-active VM pass this "
            "number"),
        ("horizon_url", "When clicked, open this URL in a browser"),
        "format"
    )
    required = ("auth_url", "password", "tenant_name", "username")
    color = "#00FF00"
    crit_color = "#FF0000"
    threshold = 0
    horizon_url = None
    format = "{tenant_name}: {active_servers} up, "\
        "{nonactive_servers} down"

    on_leftclick = "openurl"

    def run(self):
        pass

    def openurl(self):
        pass
