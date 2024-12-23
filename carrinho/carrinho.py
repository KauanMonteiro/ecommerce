from produtos.models import Produto
class Carrinho():
    def __init__(self, request):
        self.session = request.session

        carrinho = self.session.get('session_key')

        if 'session_key' not in request.session:
            carinho = self.session['session_key'] = {}

        self.carrinho = carrinho

    def add(self,produto, quantidade):
        produto_id = str(produto.id)
        produto_qty = str(quantidade)

        if produto_id in self.carrinho:
            self.carrinho[produto_id] += int(produto_qty)
        else:
            self.carrinho[produto_id]= int(produto_qty)


        self.session.modified = True

    def __len__(self):
        return len(self.carrinho)
    
    def get_prods(self):
        produtos_ids = self.carrinho.keys()

        produtos = Produto.objects.filter(id__in=produtos_ids)
        
        return produtos
    
    def get_quants(self):
        quantidade = self.carrinho

        return quantidade
    

    def atualizar(self,produto,quantidade):
        produto_id=str(produto)
        produto_qty = int(quantidade)

        ourcart = self.carrinho

        ourcart[produto_id]=produto_qty

        self.session.modified = True

        atualizado = self.carrinho
        
        return atualizado
    
    def deletar(self,produto):
        produto_id = str(produto)

        if produto_id in self.carrinho:
            del self.carrinho[produto_id]

        self.session.modified = True


