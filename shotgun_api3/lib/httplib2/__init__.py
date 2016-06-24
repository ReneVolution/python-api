import sys

if sys.version_info[0] > 2:
    from .python3.httplib2 import *
    from .python3.httplib2 import socks
else:
    from .python2.httplib2 import *
    from .python2.httplib2 import socks
