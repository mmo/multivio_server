#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Document Parser module for Multivio"""

__author__ = "Johnny Mariethoz <Johnny.Mariethoz@rero.ch>"
__version__ = "0.0.0"
__copyright__ = "Copyright (c) 2009 Rero, Johnny Mariethoz"
__license__ = "Internal Use Only"


#---------------------------- Modules ---------------------------------------

# import of standard modules
import logging

# local modules
import logger
from mvo_config import MVOConfig

#----------------------------------- Classes -----------------------------------
class ProcessorError:
    """Base class for Processor exception"""
    class InvalidDocument(Exception):
        """Input document is not valid."""
        pass

#_______________________________________________________________________________
class DocumentProcessor(object):
    """Base class to process document"""
#_______________________________________________________________________________
    def __init__(self, file_name):
        self._file_name = file_name
        self.logger = logging.getLogger(MVOConfig.Logger.name + "."
                        + self.__class__.__name__) 
        if self._check() is not True:
            raise ProcessorError.InvalidDocument("The file is invalid. (is it" \
                    "corrupted?)")

    def _check(self):
        """Check if the document is valid."""
        return True

    def render(self, max_output_size=None, angle=0, index=None,
        output_format=None):
        """Render the document content.

            max_output_size -- tupple: maximum dimension of the output
            angle -- int: angle in degree
            index -- dict: index in the document
            output_format -- string: select the output format
            
        return:
            mime_type -- string: output mime type
            data -- string: output data
        """
        return (None, None)

    def search(self, query, from_=None, to_=None, max_results=None, sort=None):
        """Search parts of the document that match the given query.

            from_ -- dict: start the search at from_
            to_ -- dict: end the search at to_
            max_results -- int: limit the number of the returned results
            sort -- string: sort the results given the sort criterion
        return:
            a dictionary with the founded results
        """
        return None

    def indexing(self, output_file):
        """Batch indexing of the document.
        return:
            True if everything is ok.
        """
        return None


