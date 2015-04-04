from cif.store import Store
import logging
from rdflib import Graph, ConjunctiveGraph, Literal, URIRef
from pprint import pprint
import uuid


class Graph(Store):

    name = 'graph'

    def __init__(self, logger=logging.getLogger(__name__), *args, **kwargs):
        super(Plugin, self).__init__(*args, **kwargs)

        self.logger = logger
        self._open_store()
        self.store_id = Literal(str(uuid.uuid4()))

    def _open_store(self, store='IOMemory'):
        self.logger.debug("opening store...")
        self.handle = ConjunctiveGraph(store, identifier="permanent")

    def _close_store(self):
        self.logger.debug("closing store")
        self.handle.close(commit_pending_transaction=True)

    def search(self, data):
        return [data]

    # http://en.wikipedia.org/wiki/Resource_Description_Framework
    def submit(self, data):
        subject = Literal(data["observable"])

        for k in data:
            if k == "observable":
                continue
            subject = Literal(data["observable"])
            self.handle.add((subject, Literal(k), Literal(data[k]), self.store_id))

        self.logger.debug(self.handle.serialize(format="trig"))

        return [data]

Plugin = Graph