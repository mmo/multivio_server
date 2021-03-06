#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Logging module for the Multivio application."""

#==============================================================================
#  This file is part of the Multivio software.
#  Project  : Multivio - https://www.multivio.org/
#  Copyright: (c) 2009-2011 RERO (http://www.rero.ch/)
#  License  : See file COPYING
#==============================================================================

__copyright__ = "Copyright (c) 2009-2011 RERO"
__license__ = "GPL V.2"

#---------------------------- Modules -----------------------------------------

# import of standard modules
from optparse import OptionParser
import re
import sys
if sys.version_info < (2, 6):
    import simplejson as json
else:
    import json

# local modules
from web_app import WebApplication, ApplicationError


#---------------------------- Classes -----------------------------------------

class VersionApp(WebApplication):
    """Web application for logging"""
    def __init__(self):
        """Basic constructor"""
        WebApplication.__init__(self)
        self.usage = """Asks the server to obtain a version in json format.
        For example:
        {
            "name" : "Multivio Server",
            "version" " : "0.0.1",
            "api_version" " : "0.1"
        }
<br>"""
        self._api_version = "1.0.0"
        self._name = "Multivio Server"
        import __init__
        self._version = __init__.__version__
    
    def get(self, environ, start_response):
        """ Callback method for new http request.
        
        """
        #get parameters from the URI
        (path, opts) = self.get_params(environ)

        #check if is valid
        if re.search(r'version', path) is not None:
            to_return = {
                "name": self._name,
                "version": self._version,
                "api_version": self._api_version
            }
            start_response('200 OK', [('content-type',
                'application/json')])
            return ["%s" % json.dumps(to_return,  sort_keys=True, indent=2)]

        raise ApplicationError.InvalidArgument("Invalid Argument")


#---------------------------- Main Part ---------------------------------------

def main():
    """Main function"""
    usage = "usage: %prog [options]"

    parser = OptionParser(usage)

    parser.set_description ("To test the Logger class.")

    parser.add_option ("-v", "--verbose", dest="verbose",
                       help="Verbose mode",
                       action="store_true", default=False)

    parser.add_option ("-p", "--port", dest="port",
                       help="Http Port (Default: 4041)",
                       type="int", default=4041)

    (options, args) = parser.parse_args()

    if len(args) != 0:
        parser.error("Error: incorrect number of arguments, try --help")

    from wsgiref.simple_server import make_server
    application = VersionApp()
    server = make_server('', options.port, application)
    server.serve_forever()

if __name__ == '__main__':
    main()
