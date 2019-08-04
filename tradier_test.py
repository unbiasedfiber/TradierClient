from Tradier import TradierClient

t = TradierClient('2FCuk6CNhHkDObWZcUzBKGg1pVR7', True)
res = t.get_quote("APHA").text

print(res)
