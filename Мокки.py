# @mock.patch('core.systems.pharmzakaz.requests.summ', side_effect=mock_summ)
    def test_legal_entities_partial_update(self, *args, **kwargs):
        with mock.patch('core.systems.pharmzakaz.requests.summ', side_effect=mock_summ):
            s = core.systems.pharmzakaz.requests.summ(3, 2)
            print('mocked = ', s)
        s = core.systems.pharmzakaz.requests.summ(3, 2)
        print('not mocked = ', s)

from core.systems.pharmzakaz.requests import summ, mock_summ
import core

from unittest import mock

def summ(a, b):
    return a + b

def mock_summ(a, b):
    return a * b
