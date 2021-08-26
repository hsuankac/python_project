import inspect

import justpy as jp
import inspect
from webapp.about import About
from webapp.home import Homepage
from webapp.dictionary import Dictionary
from webapp import page

imports = list(globals().values())

for obj in imports:
    if inspect.isclass(obj):
        if issubclass(obj, page.Page) and obj is not page.Page:
            jp.Route(obj.path, obj.serve)

jp.justpy(port=8001)