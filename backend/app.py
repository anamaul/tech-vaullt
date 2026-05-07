import os 
from flask import Flask, jsonify, request 
from flask_cors import CORS 
 
app = Flask(__name__) 
CORS(app) 

# Sistem akan otomatis membaca Environment Variables dari Kubernetes YAML. 
# Jika kalian menulis nama langsung di sini, nilai otomatis dipotong. 
nama_owner = os.environ.get('NAMA_PRAKTIKAN', 'Misterius') 
nim_owner = os.environ.get('NIM_PRAKTIKAN', '00000000') 
 
 
katalog_data = {
    "judul_katalog": f"TechVault — Katalog Gadget Milik {nama_owner}",
    "pemilik": nama_owner,
    "nim": nim_owner,
    "deskripsi": "Koleksi spesifikasi gadget dan perangkat teknologi terkini",
    "items": [
        {
            "nama": "NVIDIA RTX 5090",
            "kategori": "GPU",
            "harga": "Rp 35.000.000",
            "spesifikasi": "32GB GDDR7, 2048-bit, 1800 MHz Boost Clock",
            "emoji": "🎮"
        },
        {
            "nama": "AMD Ryzen 9 9950X",
            "kategori": "CPU",
            "harga": "Rp 12.500.000",
            "spesifikasi": "16 Core / 32 Thread, 5.7 GHz Boost, 170W TDP",
            "emoji": "⚡"
        },
        {
            "nama": "Samsung 990 EVO Plus 2TB",
            "kategori": "Storage",
            "harga": "Rp 3.200.000",
            "spesifikasi": "NVMe M.2, 7450 MB/s Read, 6900 MB/s Write",
            "emoji": "💾"
        },
        {
            "nama": "Corsair Dominator Titanium 64GB",
            "kategori": "RAM",
            "harga": "Rp 8.500.000",
            "spesifikasi": "DDR5-6400, CL32, Dual Channel Kit",
            "emoji": "🧠"
        },
        {
            "nama": "ASUS ROG Swift OLED PG42UQ",
            "kategori": "Monitor",
            "harga": "Rp 22.000.000",
            "spesifikasi": "42\" 4K OLED, 138Hz, 0.1ms GTG, HDR10",
            "emoji": "🖥️"
        }
    ]
}

 
@app.route('/api/info', methods=['GET']) 
def get_info(): 
    return jsonify(katalog_data) 
 
@app.route('/api/add-item', methods=['POST']) 
def add_item(): 
    new_item = request.json.get('item') 
    if new_item: 
        katalog_data["items"].append(new_item) 
        return jsonify({"message": "Item berhasil ditambahkan!", "items": 
katalog_data["items"]}), 201 
    return jsonify({"error": "Data tidak valid"}), 400
  
if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=5000)
