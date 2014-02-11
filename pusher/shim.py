try:
    import httplib
except ImportError:
    import http.client as httplib

import urllib

try:
    urllib.quote
except AttributeError:
    import urllib.request as urllib
