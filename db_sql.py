from sqlalchemy.orm import declarative_base, relationship, Session
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, select, func, Float#, inspect

Base = declarative_base()


class Cliente(Base):
    __tablename__ = "info_cliente"

    id = Column(Integer, primary_key=True)
    fullname = Column(String(40), nullable=False)
    cpf = Column(String(9), unique=True, nullable=False)
    endereço = Column(String(40), nullable=False)

    conta = relationship('Conta', back_populates='cliente')

    def __repr__(self):
        return f"Cliente(id = {self.id}, fullname = {self.fullname}, cpf = {self.cpf}, endereço = {self.endereço})"


class Conta(Base):
    __tablename__ = "info_conta"

    id = Column(Integer, primary_key=True)
    tipo = Column(String(20), nullable=False)
    agencia = Column(String(6), nullable=False)
    num = Column(String(6), unique=True, nullable=False)
    saldo = Column(Float, nullable=False)
    cliente_id = Column(Integer, ForeignKey('info_cliente.id'), nullable=False)

    cliente = relationship('Cliente', back_populates='conta')

    def __repr__(self):
        return f"Conta(id = {self.id}, tipo = {self.tipo}, agencia = {self.agencia}, num_conta = {self.num}, saldo = {self.saldo:.2f}, cliente_id = {self.cliente_id})"


# Criar conexão com banco de dados
engine = create_engine("sqlite://")

# Criando as classes como tabelas no banco de dados
Base.metadata.create_all(engine)

# print(inspect(engine).get_table_names())

# # Pegando nome do schema
# print(inspect(engine).default_schema_name)

# Listas para persistencia de dados
nomes = ['Bob Esponja', 'Patrick Estrela', 'Sandy Bochecha', 'Siri Gueijo', 'Lula Molusco',
         'Plunck Plancton', 'Homem Sereia', 'Mexilhão Zinho', 'Picolo Daimao', 'Yu Gi Oh']
cpfs = ['125632036', '346245879', '015634659', '002369875', '031456385',
        '789632500', '445698777', '112365999', '456698789', '036987410']
endereços = ['rua abacaxi 50', 'avenida pedra 2', 'travessa aquários 33', 'praça sovina 2', 'rua da amargura 5',
             'rodovia da ganancia 1','praça da vida 99', 'praça da vida 100', 'rua nanikuzei 8000',
             'avenida coração das cartas 2000']
tipos = ['conta corrente', 'conta especial', 'poupança', 'conta corrente', 'poupança',
         'conta internacional', 'conta black', 'poupança', 'conta corrente', 'conta especial']
agencias = ['0001', '1236', '1236', '0002', '4569', '7899', '0003', '4566', '7899', '1236']
nums = ['0001X', '1236A', '1236B', '0002X', '4569D', '7899C', '0003X', '4566', '7899E', '1126C']
saldos = [0, 1000, 2000, 5000, -100, 584.48, 0, -400, 4582.45, 1000.00]
clientes_id = [1, 2, 2, 4, 5, 6, 7, 8, 9, 10]

with Session(engine) as session:

    for i in range(len(nomes)):

        # Inserindo dados das listas
        entrada_cliente = Cliente(fullname=nomes[i], cpf=cpfs[i], endereço=endereços[i])
        entrada_conta = Conta(tipo=tipos[i], agencia=agencias[i], num=nums[i], saldo=saldos[i], cliente_id=clientes_id[i])

        # Enviando para o banco de dados (persistencia de dados)
        session.add_all([entrada_cliente, entrada_conta])
        session.commit()


print("\nO número de objetos Cliente é:")
cont = select(func.count('*')).select_from(Conta)
for u in session.scalars(cont):
    print(u)

print("\nMostrando o banco de dados com os clientes:")
clientes_db = select(Cliente)
for u in session.scalars(clientes_db):
    print(u)

print("\nMostrando o banco de dados com as contas:")
contas_db = select(Conta)
for u in session.scalars(contas_db):
    print(u)

print("\nOrdenando os clientes por ordem alfabética decrescente:")
order = select(Cliente).order_by(Cliente.fullname.desc())
for u in session.scalars(order):
    print(u)

print("\nPegando os dados dos clientes Bob Esponja e Yu Gi Oh:")
stmt = select(Cliente).where(Cliente.fullname.in_(['Bob Esponja', 'Yu Gi Oh']))
for u in session.scalars(stmt):
    print(u)

print("\nPegando os dados das contas cuja id de cliente é 2:")
stmt2 = select(Conta).where(Conta.cliente_id.in_([2]))
for u in session.scalars(stmt2):
    print(u)

print("\nPegando alguns dados dos clientes que possuem conta corrente:")
stmt3 = select(Cliente.fullname, Cliente.cpf, Conta.agencia, Conta.num).where(Conta.tipo.in_(['conta corrente'])).join_from(Conta, Cliente)
connection = engine.connect()
result = connection.execute(stmt3).fetchall()
for u in result:
    print(u)


# print("\n\n")
# stmt3 = select(Cliente.fullname, Conta.agencia, Conta.num, Conta.tipo, Cliente.id).join_from(Conta, Cliente)
# connection = engine.connect()
# result = connection.execute(stmt3).fetchall()
# for u in result:
#     print(u)


