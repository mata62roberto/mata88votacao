import peewee

db = peewee.SqliteDatabase('votacao.db')

class Usuario(peewee.Model):
   nome = peewee.CharField();
   correio = peewee.CharField();
   senha1 = peewee.CharField();
   senha2 = peewee.CharField();

   class Meta:
      database = db

class Voto(peewee.Model):
   usuario = peewee.ForeignKeyField(Usuario);
   nome = peewee.CharField();
   voto = peewee.BooleanField();

   class Meta:
      database = db
                  
if __name__ == "__main__":
   try:
      Usuario.create_table()
   except peewee.OperationalError:
      print ('Tabela usuario existente!')
   try:
      Voto.create_table()
   except peewee.OperationalError:
      print ("Tabela votacao existente!")
