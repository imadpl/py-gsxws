# -*- coding: utf-8 -*-

from core import GsxObject


class Communication(GsxObject):

    _namespace = "glob:"

    def get_content(self):
        """
        The Fetch Communication Content API allows the service providers/depot/carriers
        to fetch the communication content by article ID from the service news channel.
        """

    def get_articles(self):
        """
        The Fetch Communication Articles API allows the service partners
        to fetch all the active communication message IDs.
        """
        doc = self._submit("lookupRequestData", "FetchCommunicationArticles",
                           "communicationMessage")
        print(doc)


def fetch():
    """Shortcut for fetching CompTIA data from GSX"""
    return Communication(priority="HIGH", readStatus=True).get_articles()


if __name__ == '__main__':
    import sys
    import doctest
    from core import connect
    logging.basicConfig(level=logging.DEBUG)
    connect(*sys.argv[1:4])
    doctest.testmod()
