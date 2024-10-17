class Restaurante:
    nome: str
    categoria: str
    ativo: bool

    def __init__(self, nome: str, categoria: str):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

    def __str__(self):
        return f"{self.nome} | {self.categoria}"


restaurante_praca = Restaurante("Praça", "italiano")

print(restaurante_praca)
