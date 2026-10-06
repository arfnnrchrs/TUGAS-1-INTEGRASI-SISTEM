from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

# Inisialisasi aplikasi FastAPI
app = FastAPI(
    title="Tugas 1 Integrasi Sistem",
    description="Implementasi API dan Swagger UI",
    version="1.0.0"
)

# Definisi Data Object
class Mahasiswa(BaseModel):
    id: int
    nama: str
    alamat: str
    ipk: float
    semester: int
    hobi: str

# Dummy database menggunakan list (disimpan di memory)
db = []

# 1. POST: Create Data
@app.post("/mahasiswa", response_model=Mahasiswa)
def create_data(mhs: Mahasiswa):
    for item in db:
        if item.id == mhs.id:
            raise HTTPException(status_code=400, detail="ID sudah digunakan")
    db.append(mhs)
    return mhs

# 2. GET: Read All Data
@app.get("/mahasiswa", response_model=List[Mahasiswa])
def get_all_data():
    return db

# 3. PUT: Update Data
@app.put("/mahasiswa/{mhs_id}", response_model=Mahasiswa)
def update_data(mhs_id: int, mhs_update: Mahasiswa):
    for index, item in enumerate(db):
        if item.id == mhs_id:
            db[index] = mhs_update
            return mhs_update
    raise HTTPException(status_code=404, detail="Data tidak ditemukan")

# 4. DELETE: Delete Data
@app.delete("/mahasiswa/{mhs_id}")
def delete_data(mhs_id: int):
    for index, item in enumerate(db):
        if item.id == mhs_id:
            db.pop(index)
            return {"message": f"Data mahasiswa dengan ID {mhs_id} berhasil dihapus"}
    raise HTTPException(status_code=404, detail="Data tidak ditemukan")