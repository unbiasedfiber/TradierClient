"#TradierClient"

Usage:

from Tradier import TradierClient

t = TradierClient(<API KEY>, True)
res = t.get_quote("APHA")

print(res.text)
