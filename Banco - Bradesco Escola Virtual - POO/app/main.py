class Main:
    from cliente import Clientes
    from conta import Contas

    c1 = Clientes("Roberto","1899565-4878")
    conta1 = Contas(6565,c1.nome,1200)

    print(conta1.titular," - Conta Numero: ", conta1.numero, " Seu Saldo: R$", conta1.saldo)