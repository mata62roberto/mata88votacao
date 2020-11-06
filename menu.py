
import datetime
import peewee

from votacao import Usuario, Voto
print ('1 - Incluir usuario')
print ('2 - Alterar usuario')
print ('3 - Deletar usuario')

a = int(input('Digite uma opcao: '))

if a == 1:
    b = input('Digite nome do usuario: ')
    inclui = Usuario.create(nome=b)    
elif a == 2:
     b = input('Digite nome do usuario: ')
     altera = Usuario.select().where(Usuario.nome==b).get()
     c = input('Digite novo nome do usuario: ')
     altera.nome=c
     altera.save()
elif a == 3:
     b = input('Digite novo nome do usuario: ')
     elimina = Usuario.get(Usuario.nome==b)
     elimina.delete_instance()
else:
     print ('Opcao invalida!')
          

