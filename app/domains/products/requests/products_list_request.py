from app.http.request import Request

class ProductsListRequest(Request):
    def __init__(self, req):
        super().__init__(req)
        self.filters = {
            'dsc': self.url.get('dsc'),
            'qtd': self.url.get('qtd'),
            'ord': self.url.get('ord'),
        }

    def getDsc(self):
        return self.filters['dsc']

    def getQtd(self):
        return self.filters['qtd']

    def getOrd(self):
        return self.filters['ord']