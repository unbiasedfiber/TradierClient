import requests, re, json


class TradierClient(object):
    def __init__(self, key, is_sandbox):

        self.sess = requests.Session()
        self.key = key

        if is_sandbox: self.base_url = "https://sandbox.tradier.com"
        else: self.base_url = "https://api.tradier.com"

    def _get(self, url, headers, params):
        try:
            self.sess.headers.update(headers)
            self.sess.params.update(params)
            response = self.sess.get(self.base_url+url)
            return self._handle_response(response)
        except Exception as e:
            print(e)

    def _handle_response(self, response):
        if response.ok:
            return response
        elif response.status_code >= 500:
            print("Status code : " + str(response.status_code) + "\n",
                  "Serverside error")
        elif response.status_code >= 400:
            print("Status code : " + str(response.status_code) + "\n",
                  "Try the sandbox environment instead")
        else: print("Status code : " + str(response.status_code) + "\n")

    def _valid_date(self, date):
        if re.match(r'\d{4}-\d{2}-\d{2}', date): return True
        else: print("Enter date argument as yyyy-mm-dd")

    def get_option_chain(self, symbol, date):
        if self._valid_date(date):
            url = '/v1/markets/options/chains'
            params = { "symbol" : symbol,
                       "expiration" : date}
            headers = {"Accept":"application/json",
                       "Authorization":"Bearer {}".format(self.key)}
            return self._get(url, headers, params)

    def get_option_strikes(self, symbol, date):
        if self._valid_date(date):
            url = '/v1/markets/options/strikes'
            params = { "symbol" : symbol,
                       "expiration" : date}
            headers = {"Accept":"application/json",
                       "Authorization":"Bearer {}".format(self.key)}
            return self._get(url, headers, params)

    def get_quote(self, *symbols):
        url = '/v1/markets/quotes'
        params = { "symbols":",".join(symbols) }
        headers = {"Accept":"application/json",
                   "Authorization":"Bearer {}".format(self.key)}
        return self._get(url, headers, params)

    def get_expirations(self, symbol, includeAllRoots, add_strikes):
        url = '/v1/markets/options/expirations'
        params = { "symbol":symbol,
                   "includeAllRoots":str(includeAllRoots).lower(),
                   "strikes":str(add_strikes).lower()}
        headers = {"Accept":"application/json",
                   "Authorization":"Bearer {}".format(self.key)}
        return self._get(url, headers, params)

if __name__ == "__main__":
    t = TradierClient('2FCuk6CNhHkDObWZcUzBKGg1pVR7', True)
    print(t.get_expirations("APHA", True, False).text)
