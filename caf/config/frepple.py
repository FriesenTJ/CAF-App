from __future__ import unicode_literals
from caf import _

def get_data():
    config = [
        {
            "label": _("Hello"),
            "items": [
                {
                    "type": "doctype",
                    "name": "CAF Menu",
                    "label": "CAF Menu",
                    "onboard": 1,
                }
            ]
        }
    ]
    return config