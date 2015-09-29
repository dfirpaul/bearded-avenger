import py.test

from cif.smrt import Smrt
from cif.rule import Rule
from cif.constants import REMOTE
from pprint import pprint
import json

rule = 'rules/default/sans_edu.yml'
rule = Rule(path=rule)
rule.fetcher = 'file'
s = Smrt(REMOTE, 1234, client='dummy')


def test_sans_low():
    feed = '02_domains_low'
    rule.feeds[feed]['remote'] = 'tests/sansedu/low.txt'
    x = s.process(rule, feed=feed)
    pprint(x)
    assert len(x) > 0

    x = json.loads(x[0])
    assert len(x['observable']) > 4