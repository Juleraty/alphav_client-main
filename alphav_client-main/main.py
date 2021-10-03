import requests
import settings


class APICallError(Exception):
    pass


class StockTimeSeries:

    def __init__(self):
        self.base_url = settings.BASE_URL
        self.api_key = settings.APIKEY

    def _build_url(self, path):
        return f"{self.base_url}?{path}&apikey={self.api_key}"

    
    def function(self, function):
        return f"function={function}"

    
    def symbol(self, symbol):
        return f"symbol={symbol}"

    
    def interval(self, interval):
        return f"interval={interval}"

    def slice(self, slice):
        return f'slice={slice}'

    

    def intraday_series(self, function, symbol, interval, **kwargs):
       
        path = f"{self.function(function)}&{self.symbol(symbol)}&{self.interval(interval)}"
        options = [f"{item[0]}={item[1]}" for item in kwargs.items()]
        path = f"{path}&{'&'.join(options)}" if options else path

        url = self._build_url(path)
        resp = requests.get(url)
        print(url)
        if resp.status_code == 200:
            return resp.json()

        raise APICallError(
            f"Não foi possivel consumir o serviço: STATUS_CODE"
            "={resp.status_code}"
        )

    def history_intraday_series(self, function, symbol, interval, slice, **kwargs):
        path = f"{self.function(function)}&{self.symbol(symbol)}&{self.interval(interval)}&{self.slice(slice)}"
        options = [f"{item[0]}={item[1]}" for item in kwargs.items()]
        path = f"{path}&{'&'.join(options)}" if options else path

        url = self._build_url(path)
        resp = requests.get(url)

        if resp.status_code == 200:
            return resp.json()

        raise APICallError(
            f"Não foi possivel consumir o serviço: STATUS_CODE"
            "={resp.status_code}"
        )

    def daily_series(self, function, symbol, **kwargs):
        path = f"{self.function(function)}&{self.symbol(symbol)}"
        options = [f"{item[0]}={item[1]}" for item in kwargs.items()]
        path = f"{path}&{'&'.join(options)}" if options else path

        url = self._build_url(path)
        resp = requests.get(url)
        print(url)
        if resp.status_code == 200:
            return resp.json()

        raise APICallError(
            f"Não foi possivel consumir o serviço: STATUS_CODE"
            "={resp.status_code}"
        )

    def daily_adjusted_series(self, function, symbol, **kwargs):
        path = f"{self.function(function)}&{self.symbol(symbol)}"
        options = [f"{item[0]}={item[1]}" for item in kwargs.items()]
        path = f"{path}&{'&'.join(options)}" if options else path

        url = self._build_url(path)
        resp = requests.get(url)
        print(url)
        if resp.status_code == 200:
            return resp.json()

        raise APICallError(
            f"Não foi possivel consumir o serviço: STATUS_CODE"
            "={resp.status_code}"
        )

    def weekly_series(self, function, symbol, **kwargs):
        path = f"{self.function(function)}&{self.symbol(symbol)}"
        options = [f"{item[0]}={item[1]}" for item in kwargs.items()]
        path = f"{path}&{'&'.join(options)}" if options else path

        url = self._build_url(path)
        resp = requests.get(url)
        print(url)

        if resp.status_code == 200:
            return resp.json()

        raise APICallError(
            f"Não foi possivel consumir o serviço: STATUS_CODE"
            "={resp.status_code}"
        )

    def weekly_adjusted_series(self, function, symbol, **kwargs):

        path = f"{self.function(function)}&{self.symbol(symbol)}"
        options = [f"{item[0]}={item[1]}" for item in kwargs.items()]
        path = f"{path}&{'&'.join(options)}" if options else path

        url = self._build_url(path)
        resp = requests.get(url)
        print(url)
        if resp.status_code == 200:
            return resp.json()

        raise APICallError(
            f"Não foi possivel consumir o serviço: STATUS_CODE"
            "={resp.status_code}"
        )

    def monthly_series(self, function, symbol, **kwargs):

        path = f"{self.function(function)}&{self.symbol(symbol)}"
        options = [f"{item[0]}={item[1]}" for item in kwargs.items()]
        path = f"{path}&{'&'.join(options)}" if options else path

        url = self._build_url(path)
        resp = requests.get(url)
        print(url)
        if resp.status_code == 200:
            return resp.json()

        raise APICallError(
            f"Não foi possivel consumir o serviço: STATUS_CODE"
            "={resp.status_code}"
        )

    def monthly_adjusted_series(self, function, symbol, **kwargs):

        path = f"{self.function(function)}&{self.symbol(symbol)}"
        options = [f"{item[0]}={item[1]}" for item in kwargs.items()]
        path = f"{path}&{'&'.join(options)}" if options else path

        url = self._build_url(path)
        resp = requests.get(url)
        print(url)
        if resp.status_code == 200:
            return resp.json()

        raise APICallError(
            f"Não foi possivel consumir o serviço: STATUS_CODE"
            "={resp.status_code}"
        )

    def quote_endpoint(self, function, symbol, **kwargs):

        path = f"{self.function(function)}&{self.symbol(symbol)}"
        options = [f"{item[0]}={item[1]}" for item in kwargs.items()]
        path = f"{path}&{'&'.join(options)}" if options else path

        url = self._build_url(path)
        resp = requests.get(url)
        print(url)
        if resp.status_code == 200:
            return resp.json()

        raise APICallError(
            f"Não foi possivel consumir o serviço: STATUS_CODE"
            "={resp.status_code}"
        )

    def search_endpoint(self, function, symbol, **kwargs):

        path = f"{self.function(function)}&{self.symbol(symbol)}"
        options = [f"{item[0]}={item[1]}" for item in kwargs.items()]
        path = f"{path}&{'&'.join(options)}" if options else path

        url = self._build_url(path)
        resp = requests.get(url)
        print(url)
        if resp.status_code == 200:
            return resp.json()

        raise APICallError(
            f"Não foi possivel consumir o serviço: STATUS_CODE"
            "={resp.status_code}"
        )

    def menu(self):
        stock = StockTimeSeries()
        print('Escolha uma das series:\n'
              'TIME SERIES INTRADAY [1]\n'
              'TIME SERIES DAILY [2]\n'
              'TIME SERIES DAILY ADJUSTED [3]\n'
              'TIME SERIES WEEKLY [4]\n'
              'TIME SERIES WEEKLY ADJUSTED [5]\n'
              'TIME SERIES MONTHLY [6]\n'
              'TIME SERIES MONTHLY ADJUSTED [7]\n'
              'QUOTE ENDPOINT [8]\n'
              'SEARCH ENDPOINT [9]\n'
              'TIME SERIES INTRADAY EXTENDED [10]')
        menu = input('Numero da serie: ')
        if menu == '1':
            print(stock.intraday_series('CASH_FLOW', 'IBM', '5min', outputsize='compact', adjusted='true',
                                        datatype='json'))
        elif menu == '2':
            print(stock.daily_series('TIME_SERIES_DAILY', 'IBM', outputsize='full', datatype='json'))
        elif menu == '3':
            print(stock.daily_adjusted_series('TIME_SERIES_DAILY_ADJUSTED', 'IBM', outputsize='compact', datatype='csv'))
        elif menu == '4':
            print(stock.weekly_series('TIME_SERIES_WEEKLY', 'IBM', datatype='json'))
        elif menu == '5':
            print(stock.weekly_adjusted_series('TIME_SERIES_WEEKLY_ADJUSTED', 'IBM', datatype='json'))
        elif menu == '6':
            print(stock.monthly_series('TIME_SERIES_MONTHLY', 'IBM', datatype='json'))
        elif menu == '7':
            print(stock.monthly_adjusted_series('TIME_SERIES_MONTHLY_ADJUSTED', 'IBM', datatype='json'))
        elif menu == '8':
            print(stock.quote_endpoint('GLOBAL_QUOTE', 'IBM', datatype='json'))
        elif menu == '9':
            print(stock.search_endpoint('SYMBOL_SEARCH', 'microsoft', datatype='json'))
        elif menu == '10':
            print(stock.history_intraday_series('CASH_FLOW', 'IBM', '5min', 'year1month1', adjusted='true', ))


if __name__ == '__main__':
    init = StockTimeSeries()
    init.menu()
