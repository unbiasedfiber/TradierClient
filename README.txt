"#TradierClient"

Usage:

from Tradier import TradierClient

t = TradierClient(<API KEY>, is_sandbox = True)
res = t.get_quote("APHA")

print(res.text)
