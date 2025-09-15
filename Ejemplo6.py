class producto:

    def __init__(self,producto,precio):
       
        self.producto=producto
        self.precio=precio
    def __str__(self):
        return f'{'producto'},{'precio'}'
    
    def __format__(self, format_spec):
        if format =="precio":
            return str(self)
        
    def __repr__(self):
        return f'{self.producto},{self.precio}'
    
producto1=producto("computador",300000)
print(producto1)
print(repr(producto1))
print(f'{producto1.precio}')
    

        

    