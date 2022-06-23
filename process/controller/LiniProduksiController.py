from datetime import datetime
import db.db_handler as database

def GetAllLiniProduksi():
  conn = database.connector()
  cursor = conn.cursor()

  query = "SELECT * FROM gen_r_liniproduksi"
  cursor.execute(query)

  records = cursor.fetchall()
 
  for data in records:
    print("ID       : ",data[0],)
    print("Nama     : ",data[1],)
    print("Dibuat   : ",data[2],)
    print("Berlaku  : ",data[3],)

  return records


def AddLiniProduksi():
  conn = database.connector()
  cursor = conn.cursor()

  id, nama = input("Input ID : "), input("Input Nama : ")

  query = "INSERT INTO gen_r_liniproduksi (id, nama, dibuat) VALUES (%s,%s,%s)"
  values = (id, nama, datetime.now())
  cursor.execute(query,values)
 
  conn.commit()
  print("Lini Produksi Baru Ditambahkan!")


def StopLiniProduksi():
  conn = database.connector()
  cursor = conn.cursor()

  id = input("Input ID : ")

  query = "UPDATE gen_r_liniproduksi SET berlaku = %s WHERE id = %s"
  values = (datetime.now(), id)
  cursor.execute(query,values)
 
  conn.commit()
  print("Lini Produksi Selesai!")