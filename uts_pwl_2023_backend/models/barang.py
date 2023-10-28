from sqlalchemy import (
    Column,
    Integer,
    Text,
)

from .meta import Base


class Barang(Base):
    __tablename__ = "barang"
    id = Column(Integer, primary_key=True)
    nama_barang = Column(Text, nullable=False)
    harga_barang = Column(Text, nullable=False)
    kategori_barang = Column(Text, nullable=False)
    gambar_barang = Column(Text, nullable=False)
    deskripsi_barang = Column(Text, nullable=False)
    nama_penjual = Column(Text, nullable=False)
    kontak_penjual = Column(Text, nullable=False)
    alamat_penjual = Column(Text, nullable=False)
    nama_pembeli = Column(Text)
    kontak_pembeli = Column(Text)
    alamat_pembeli = Column(Text)
