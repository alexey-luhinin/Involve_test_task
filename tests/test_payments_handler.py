from payments_handler import eur_handler, usd_handler, rub_handler


def test_eur_handler():
    assert 'error' not in eur_handler({'amount': '12',
                                       'currency': '978',
                                       'description': 'test'})

def test_usd_handler():
    assert 'error' not in usd_handler({'amount': '14',
                                       'currency': '840',
                                       'description': 'test'})

def test_rub_handler():
    assert 'error' not in rub_handler({'amount': '15',
                                       'currency': '643',
                                       'description': 'test'})
