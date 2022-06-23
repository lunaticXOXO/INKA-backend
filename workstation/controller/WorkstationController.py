import db.db_handler as database

def GetAllWorkstation():
    conn = database.connector()
    cursor = conn.cursor()

    query = "SELECT * FROM gen_r_stasiunkerja a "
    query = query + "JOIN gen_r_liniproduksi b WHERE a.liniproduksi = b.id"
    cursor.execute(query)

    records = cursor.fetchall()
    
    for data in records:
        print("ID            : ",data[0],)
        print("Nama          : ",data[1],)
        print("Dibuat        : ",data[2],)
        print("Berlaku       : ",data[3],)
        print("Lini Produksi : ",data[4],)

    return records

def AddWorkstation():
  conn = database.connector()
  cursor = conn.cursor()

  id, nama, liniProduksi = input("Input ID : "), input("Input Nama : "), input("Input ID Lini Produksi  : ")

  query = "INSERT INTO gen_r_stasiunkerja (id, nama, liniproduksi) VALUES (%s,%s,%s)"
  values = (id, nama, liniProduksi)
  cursor.execute(query,values)
 
  conn.commit()
  print("Workstation Baru Ditambahkan!")