from math import ceil
from process.controller.ProsesController import HitungDurasiProses
import db.db_handler as db
import numpy as np
from datetime import datetime, timedelta

def GetAllRincianProyek():
    conn = db.connector()
    cursor = conn.cursor()

    query = "SELECT a.id, a.jumlah, a.dueDate, b.id, c.id FROM prd_r_rincianproyek a "
    query = query + "JOIN prd_r_jenisproduk b ON b.id = a.jenisProduk "
    query = query + "JOIN prd_r_proyek c ON c.id = a.proyek"

    cursor.execute(query)

    records = cursor.fetchall()
        
    for data in records:
        print("ID               : ",data[0],)
        print("Jumlah           : ",data[1],)
        print("Due Date         : ",data[2],)
        print("ID Jenis Produk  : ",data[3],)
        print("ID Proyek        : ",data[4],)
    
    return records


def AddRincianProyek():
    conn = db.connector()
    cursor = conn.cursor()

    id, jumlah, dueDate, jenisProduk, proyek = input("Input ID Rincian Proyek : "), input("Input Jumlah : "), input("Input Due Date : "), input("Input ID Jenis Produk : "), input("Input ID Proyek : ")

    query = "INSERT INTO prd_r_rincianproyek (id, jumlah, dueDate, jenisProduk, proyek) VALUES (%s,%s,%s,%s,%s)"
    values = (id, jumlah, dueDate, jenisProduk, proyek)
    cursor.execute(query,values)
 
    conn.commit()
    print("Rincian Proyek Baru Ditambahkan!")


def HitungDueDateRProyek(id_proyek):
    hasil1 = HitungDurasiProses(id_proyek)

    conn = db.connector()
    cursor = conn.cursor()

    query = "SELECT a.jumlah, b.tglDibuat, b.dueDate FROM prd_r_rincianproyek a "
    query = query + "JOIN prd_r_proyek b ON "
    query = query + "b.id = a.proyek "
    query = query + "WHERE b.id = '"+id_proyek+"'"
    
    cursor.execute(query)

    records = cursor.fetchall()
    hasilPerkalian = 1        
    
    for data in records:
        print("Jumlah Pesanan :",data[0], "Produk")
        data[1]
        data[2]
       
        hasilPerkalian = data[0]
        tanggalDibuat  =  data[1]
        tanggalDueDate = data[2]
   
    hasilPerkalian = hasilPerkalian * hasil1
    durasiHari = hasilPerkalian / 8
    sabtuMingguDalamSebulan = (16 * 4)
    durasiBaru = hasilPerkalian + sabtuMingguDalamSebulan
    durasiBaru2 = durasiBaru / 8

    hitungHariBisnis = np.busday_count(tanggalDibuat,tanggalDueDate)

    print("Tanggal Proyek Dipesan :", tanggalDibuat.strftime("%A"), tanggalDibuat)
    print("Due Date Proyek :", tanggalDueDate.strftime("%A"), tanggalDueDate)
    print("Banyak Hari Kerja Antara Dipesan dan Due Date :", hitungHariBisnis)
    print("Durasi Rincian Proyek :", ceil(hasilPerkalian), "Jam Atau", ceil(durasiHari), "Hari (Sabtu dan Minggu Kerja)")
    newdays = ceil(durasiBaru2)
    print("Durasi Rincian Proyek :",ceil(durasiBaru), "Jam Atau",newdays, "Hari (Sabtu dan Minggu Libur)")
    duedateproyek = tanggalDibuat + timedelta(days = newdays)
    print("Due Date Rincian Proyek :",duedateproyek)

    return duedateproyek


def UpdateDueDateRProyek():
    id_proyek = input("Input ID Proyek : ")

    tanggal = HitungDueDateRProyek(id_proyek)
    conn = db.connector()
    cursor = conn.cursor()

    query = "UPDATE prd_r_rincianproyek SET dueDate = '"+str(tanggal)+"' WHERE proyek = '"+id_proyek+"'"
    cursor.execute(query)

    conn.commit()
    print("Records Updated")

