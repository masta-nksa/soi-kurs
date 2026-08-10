"""Oeffnet alle Links auf fremde Seiten in einem neuen Tab.

Der Hook laeuft beim Bauen der Website. Er haengt an jeden <a>-Tag mit einer
Adresse, die mit http:// oder https:// beginnt, target="_blank" an. Interne
Links bleiben unveraendert, damit die Navigation im selben Tab bleibt.

rel="noopener" gehoert dazu: ohne das kann die geoeffnete Seite auf das
Ursprungsfenster zugreifen.

Eingetragen in mkdocs.yml unter "hooks:". Kein Zusatzpaket noetig.
"""

import re

# <a ...href="http...">, aber nur, wenn noch kein target= im Tag steht.
EXTERNER_LINK = re.compile(r'<a\s+(?![^>]*\btarget=)([^>]*href="https?://[^"]*")')


def on_post_page(output, page, config):
    return EXTERNER_LINK.sub(r'<a target="_blank" rel="noopener" \1', output)
