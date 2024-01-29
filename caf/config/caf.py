from __future__ import unicode_literals
from frappe import _

def get_data():
    config = [
        {
            "label": _("CAF Menu"),
            "items": [
                {
                    "type": "doctype",
                    "name": "CAF Example",
                    "label": "CAF Example",
                    "onboard": 1,
                }
            ]
        }
    ]
    return config