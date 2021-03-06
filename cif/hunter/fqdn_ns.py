import logging
from csirtg_indicator import resolve_itype
from csirtg_indicator.exceptions import InvalidIndicator
from cif.utils import resolve_ns
from csirtg_indicator import Indicator
from dns.resolver import Timeout


class FqdnNs(object):

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def process(self, i, router):
        if i.itype != 'fqdn':
            return

        if 'search' in i.tags:
            return

        try:
            r = resolve_ns(i.indicator)
        except Timeout:
            self.logger.info('timeout trying to resolve: {}'.format(i.indicator))
            return

        for rr in r:
            ip = Indicator(**i.__dict__())
            ip.indicator = str(rr)
            try:
                resolve_itype(ip.indicator)
            except InvalidIndicator as e:
                self.logger.error(ip)
                self.logger.error(e)
            else:
                ip.itype = 'ipv4'
                ip.rdata = i.indicator
                ip.confidence = (int(ip.confidence) / 4)
                router.indicators_create(ip)

Plugin = FqdnNs
