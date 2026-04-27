from urllib.request import urlopen
import webbrowser

import lxml.html
from lxml.cssselect import CSSSelector

from i3pystatus import IntervalModule
from i3pystatus.core.util import internet, require


class TrackerAPI:
    def __init__(self, idcode):
        pass

    def status(self):
        pass

    def get_url(self):
        pass


class DPD(TrackerAPI):
    URL = "https://tracking.dpd.de/cgi-bin/simpleTracking.cgi?parcelNr={idcode}&type=1"

    def __init__(self, idcode):
        self.idcode = idcode
        self.url = self.URL.format(idcode=self.idcode)

    def status(self):
        pass

    def get_url(self):
        pass


class DHL(TrackerAPI):
    URL = "http://nolp.dhl.de/nextt-online-public/set_identcodes.do?lang=en&idc={idcode}"

    def __init__(self, idcode):
        self.idcode = idcode
        self.url = self.URL.format(idcode=self.idcode)

    def get_progress(self, page):
        pass

    def status(self):
        pass

    def get_url(self):
        pass


class UPS(TrackerAPI):
    URL = "http://wwwapps.ups.com/WebTracking/processRequest?HTMLVersion=5.0&Requester=NES&AgreeToTermsAndConditions=yes&loc=en_US&tracknum={idcode}"

    def __init__(self, idcode):
        self.idcode = idcode
        self.url = self.URL.format(idcode=self.idcode)

        error_selector = CSSSelector(".secBody .error")
        self.error = lambda page: len(error_selector(page)) >= 1
        self.status_selector = CSSSelector("#tt_spStatus")
        self.progress_selector = CSSSelector(".pkgProgress div")

    def status(self):
        pass

    def get_url(self):
        pass


class Itella(TrackerAPI):
    def __init__(self, idcode, lang="fi"):
        self.idcode = idcode
        self.lang = lang

    def status(self):
        pass


class ParcelTracker(IntervalModule):
    """
    Used to track parcel/shipments.

    Supported carriers: DHL, UPS, DPD, Itella

    - parcel.UPS("<id_code>")
    - parcel.DHL("<id_code>")
    - parcel.DPD("<id_code>")
    - parcel.Itella("<id_code>"[, "en"|"fi"|"sv"])
      Second parameter is language. Requires beautiful soup 4 (bs4)

    Requires lxml and cssselect.
    """

    interval = 60

    settings = (
        ("instance", "Tracker instance, for example ``parcel.UPS('your_id_code')``"),
        "format",
        "name",
    )
    required = ("instance", "name")

    format = "{name}:{progress}"
    on_leftclick = "open_browser"

    @require(internet)
    def run(self):
        pass

    def open_browser(self):
        pass
