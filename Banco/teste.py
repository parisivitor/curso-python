from models.cliente import Cliente
from models.conta import Conta


vitor: Cliente = Cliente('Vitor', 'vitor@g.com', '123.123.123.-12', '08/09/1995')
carol: Cliente = Cliente('Carol', 'carol@g.com', '456.456.456-45', '06/05/1998')

conta_vitor: Conta = Conta(vitor)
conta_carol: Conta = Conta(carol)

print(vitor)
print(conta_vitor)
print()
print(carol)
print(conta_carol)