import fanstatic
from js.bootstrap import bootstrap


library = fanstatic.Library("fontawesome", "resources")
fontawesome = fanstatic.Resource(library, "css/font-awesome.css",
                                 depends=[bootstrap])
