from __future__ import absolute_import
from __future__ import unicode_literals

import os
import sys

PY_MAJOR_VERSION = sys.version_info[0]

httplib_include_path = os.path.join(os.path.dirname(__file__),
                                    'python' + str(PY_MAJOR_VERSION))

sys.path.append(httplib_include_path)


if PY_MAJOR_VERSION > 2:
    from httplib2 import *
    from httplib2 import socks, HttpLib2Error
    from ssl import SSLError as SSLHandshakeError
else:
    from httplib2 import *
    from httplib2 import socks, SSLHandshakeError
