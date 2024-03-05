# Os 4 pilares da Programação Orientada a Objetos
# Encapsulamento, Herança, Abstração e Polimorfismo

#Abstração

class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o método log')
    
    def log_error(self,msg):
        return self._log(f'Error:{msg}')

    def log_sucess(self,msg):
        return self._log(f'Sucess:{msg}')

class LogFileMixin(Log):
    def _log(self, msg):
        print(msg)

class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})') 
        # print(msg) # aqui retorna "Error:qualquer coisa"

if __name__ == '__main__': #main é este módulo
    # l = Log() 
    # l = LogFileMixin()
    l = LogPrintMixin()
    l.log_error('qualquer coisa')
    l.log_sucess('Que legal!')