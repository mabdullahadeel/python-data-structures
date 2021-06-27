from ..buyAndSellStocks import buy_n_sell_brute_force


def test_buy_and_sell_stocks():
    test_samples = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
    test_output = {
        'max_profit': 30,
        'indexes': (4, 6)
    }

    assert buy_n_sell_brute_force(prices_array=test_samples) == test_output