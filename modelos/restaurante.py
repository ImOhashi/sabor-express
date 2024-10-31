class Restaurante:

    restaurantes: list = []

    def __init__(self, nome: str, categoria: str):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f"{self.nome} | {self.categoria}"

    @classmethod
    def listar_restaurantes(self):
        print(f"{"Nome do restaurante".ljust(26)}| {"Categoria".ljust(26)}| Status")
        for restaurante in self.restaurantes:
            print(f"{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}")

    @property
    def ativo(self):
        return "Ativo" if self._ativo else "Desativado"

    def alternar_estado(self):
        self._ativo = not self._ativo



restaurante_praca = Restaurante("praça", "italiano")
restaurante_sushi = Restaurante("sushi", "japa")

restaurante_sushi.alternar_estado()

restaurante_praca.listar_restaurantes()