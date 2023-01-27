''' Class '''
class Contas:
    ''' Class '''
    def __init__(self,nmbr,titular) -> None:
        self._saldo = 0.0
        self._numero = nmbr
        self._titular = titular

    @property
    def saldo(self) -> None:
        return self._saldo
    
    @saldo.setter
    def set_saldo(self,saldo) -> None:
        if saldo < 0 :
            print("O saldo não pode ser negativo")
        else:
            self._saldo = saldo
