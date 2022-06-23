from process.controller.ProsesController import *
from process.controller.LiniProduksiController import *
from product.controller.JenisProdukController import *
from product.controller.ProdukController import *
from product.controller.StrukturJenisProdukController import *
from project.controller.ProyekController import *
from workstation.controller.WorkstationController import *
from product.controller.JenisProdukController import *
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

#PROYEK
@app.route('/proyek/get_allproyek',methods = ['GET'])
def get_allproyek():
    hasil = GetAllProyek()
    return hasil


@app.route('/proyek/add_newproyek',methods = ['POST'])
def add_newproyek():
    hasil = AddProyek()
    return hasil

@app.route('/proyek/update_proyek/<id>',methods = ['POST'])
def update_proyek(id):
    hasil = UpdateProyek(id)
    return hasil

#JENIS PRODUCT
@app.route('/jproduct/post_jproduct',methods =['POST'])
def post_jproduct():
    hasil = AddJenisProduct()
    return hasil


@app.route('/jproduct/get_jproduct',methods = ['GET'])
def get_jproduct():
   hasil = GetAllJenisProduk()
   return hasil

@app.route('/jproduct/get_jproduct/<id>',methods = ['GET'])
def get_jproduct_byId(id):
    hasil = GetJenisProductById(id)
    return hasil

@app.route('/jproduct/update_jproduct/<id>',methods = ['POST'])
def update_jproduct(id):
    hasil = UpdateJenisProduk(id)
    return hasil

#STUKTUR JENIS PRODUCT
@app.route('/sjproduct/get_jproduct_sjproduct',methods = ['GET'])
def get_jproduc_sjproduct():
    hasil = ShowJProdukJoinSJProduk()
    return hasil

@app.route('/sjproduct/get_sjproduct_by_jproduct/<id>',methods = ['GET'])
def get_sjproduct_by_jproduct(id):
    hasil = ShowSJProdukbyIDJenisProduk(id)
    return hasil

@app.route('/sjproduct/insert_sjproduct_by_jproduct/<id_jproduk>',methods = ['POST'])
def insert_sjproduct_by_jproduct(id_jproduk):
    hasil = AddSJProdukByJenisProduk(id_jproduk)
    return hasil

#PROSES
@app.route('/proses/get_listprocess',methods = ['GET'])
def get_listprocess():
    hasil = ShowProses()
    return hasil

@app.route('/proses/get_lastprocess_product/<id>',methods = ['GET'])
def get_lastprocess_product(id):
    hasil = ShowLastProcessofProductAPI(id)
    return hasil

@app.route('/proses/add_process',methods = ['POST'])
def add_process():
    hasil = AddProses()
    return hasil

@app.route('/proses/add_process_by_sjproduct/<id_sjproduk>',methods = ['POST'])
def add_process_by_sjproduct(id_sjproduk):
    hasil = AddProcessBySJProduk(id_sjproduk)
    return hasil

if __name__ =="__main__":
    app.run(debug = True,port = 8181)
    print("Connected to port 8181")