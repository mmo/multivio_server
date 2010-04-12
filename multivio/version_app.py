#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Logging module for the Multivio application."""

__author__ = "Johnny Mariethoz <Johnny.Mariethoz@rero.ch>"
__version__ = "0.0.0"
__copyright__ = "Copyright (c) 2009 Rero, Johnny Mariethoz"
__license__ = "Internal Use Only"


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
from web_app import WebApplication


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
        self._api_version = "0.1"
        self._name = "Multivio Server"
        import __init__
        self._version = __init__.__version__
    
    def get(self, environ, start_response):
        """ Callback method for new http request.
        
        """
        #get parameters from the URI
        (path, opts) = self.getParams(environ)

        #check if is valid
        self.logger.debug("Accessing: %s with opts: %s" % (path, opts))

        if re.search(r'version', path) is not None:
            to_return = {
                "name": self._name,
                "version": self._version,
                "api_version": self._api_version
            }
            start_response('200 OK', [('content-type',
                'application/json')])
            return ["%s" % json.dumps(to_return,  sort_keys=True, indent=2)]

        start_response('400 Bad Request', [('content-type', 'text/html')])
        return ["Invalid arguments."]


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
