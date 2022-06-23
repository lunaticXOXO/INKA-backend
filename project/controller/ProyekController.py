from project.controller.RincianProyekController import *
from datetime import datetime
import db.db_handler as database
from flask import request,make_response,jsonify

def GetAllProyek():
  conn = database.connector()
  cursor = conn.cursor()

  query = "SELECT * FROM prd_r_proyek"
  cursor.execute(query)

  row_headers = [x[0] for x in cursor.description]
  records = cursor.fetchall()
  json_data = []

  for data in records:
      json_data.append(dict(zip(row_headers,data)))

  conn.commit()
  return make_response(jsonify(json_data),200)


def AddProyek():
  conn = database.connector()
  cursor = conn.cursor()
  query = "INSERT INTO prd_r_proyek (id, nama, tglDibuat, dueDate) VALUES (%s,%s,%s,%s)"
  try:
      data = request.json
      id_proyek = data["id"]
      nama_proyek = data["nama"]
      dueDate = data["dueDate"]
      values = (id_proyek, nama_proyek, datetime.now(), dueDate)
      cursor.execute(query,values)
      conn.commit()
      hasil = {"status " : "berhasil"}
  except Exception as e:
      print("Error" + str(e))
      hasil = {"status" : "gagal"}

  return hasil


def UpdateProyek(id):
    conn = database.connector()
   
    try:
        data = request.json
        nama_proyek = data["nama"]
        dueDate = data["dueDate"]
        cursor = conn.cursor()
        query = "UPDATE prd_r_proyek SET nama = %s, dueDate = %s WHERE id = %s"
        values = (nama_proyek,dueDate,id)
        cursor.execute(query,values)
        conn.commit()
        hasil = {"status" : "berhasil"}
    except Exception as e:
        print("Error" + str(e))
        hasil = {"status" : "gagal"}

    return hasil
  