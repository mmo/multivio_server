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

#----------------------------------- Exceptions --------------------------------

class ParserError:
    """Base class for errors in the DocumentParser packages."""
    class InvalidDocument(Exception):
        """The document is not valid."""
        pass
    class InvalidParameters(Exception):
        """The type of the input parameters is not correct."""
        pass

#----------------------------------- Classes -----------------------------------

#_______________________________________________________________________________
class DocumentParser(object):
    """Base class to parse document"""

    def __init__(self, file_stream):
        """Constructor."""
        self._file_stream = file_stream
        self.logger = logging.getLogger(MVOConfig.Logger.name + "."
                        + self.__class__.__name__) 
        if self._check() is not True:
            raise ParserError.InvalidDocument("The file is invalid. (is it" \
                    "corrupted?)")

    def _check(self):
        """Check if the document is valid."""
        return True

    def get_metadata(self):
        """Get the Metadata of the document.
        Such as title, author, etc.
        """
        return None

    def get_logical_structure(self):
        """Get the logical structure of the document.
        Such as Table of Contents.
        """
        return None

    def get_physical_structure(self):
        """Get the physical structure of the document.
        Such as list of images.
        """
        return None


