from produtos.models import Produto
class Carrinho():
    def __init__(self, request):
        self.session = request.session

        carrinho = self.session.get('session_key')

        if 'session_key' not in request.session:
            carinho = self.session['session_key'] = {}

        self.carrinho = carrinho

    def add(self,produto):
        produto_id = str(produto.id)  

        if produto_id in self.carrinho:
            pass
        else:
            self.carrinho[produto_id]= {'preco': str(produto.preco)}

        self.session.modified = True

    def __len__(self):
        return len(self.carrinho)
    
    def get_prods(self):
        produtos_ids = self.carrinho.keys()

        produtos = Produto.objects.filter(id__in=produtos_ids)
        
        return produtos