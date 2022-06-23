import db.db_handler as database

def GetAllProduk():
  conn = database.connector()
  cursor = conn.cursor()

  query = "SELECT * FROM prd_r_produk"
  cursor.execute(query)

  records = cursor.fetchall()
 
  for data in records:
    print("ID                : ",data[0],)
    print("ID Rincian Proyek : ",data[1],)

  return records


def AddProduk():
  conn = database.connector()
  cursor = conn.cursor()

  id, rincianProyek = input("Input ID Produk : "), input("Input ID Rincian Proyek : ")

  query = "INSERT INTO prd_r_produk (id, rincianProyek) VALUES (%s,%s)"
  values = (id, rincianProyek)
  cursor.execute(query,values)
 
  conn.commit()
  print("Produk Baru Ditambahkan!")


def ShowDueDateProduct():
  conn = database.connector()
  cursor = conn.cursor()

  
