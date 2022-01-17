class Usuario:		# esto es lo que tenemos hasta ahora
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.balance_cuenta = 0
    # agregando el método de depósito
    def hacer_deposito(self, amount):
        self.balance_cuenta += amount
        return self
    def hacer_retiro(self, amount):
        self.balance_cuenta -= amount
        return self
    def mostrar_balance_usuario(self):
        print(f"Usuario: {self.name}, Balance:${self.balance_cuenta}")
        return self
    def transfer_dinero(self, other_user, amount):
        self.hacer_retiro(amount)
        other_user.hacer_deposito(amount)
        return self

user1 = Usuario("Renato","abc@test.com")
user2 = Usuario("Paco","abc@test.com")
user3 = Usuario("Vanessa","abc@test.com")

user1.hacer_deposito(500).hacer_deposito(300).hacer_deposito(200).hacer_retiro(400).mostrar_balance_usuario()
user2.mostrar_balance_usuario()
user3.mostrar_balance_usuario()

user1.mostrar_balance_usuario()
user2.hacer_deposito(500).hacer_deposito(300).hacer_retiro(200).hacer_retiro(400).mostrar_balance_usuario()
user3.mostrar_balance_usuario()

user1.mostrar_balance_usuario()
user2.mostrar_balance_usuario()
user3.hacer_deposito(1500).hacer_retiro(300).hacer_retiro(200).hacer_retiro(400).mostrar_balance_usuario()

user1.transfer_dinero(user3,200).mostrar_balance_usuario()
user2.mostrar_balance_usuario()
user3.mostrar_balance_usuario()
