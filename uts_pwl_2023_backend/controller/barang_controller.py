from pyramid.response import Response
from pyramid.request import Request
from pyramid.view import view_defaults, view_config
from sqlalchemy.exc import DBAPIError

from ..models import Barang


@view_defaults(route_name="barang", renderer="json")
class BarangView:
    def __init__(self, request):
        self.request: Request = request

    def server_error(self, message):  # Error view
        self.request.response.status = 500
        return {"message": "Server Error", "error": message}

    def not_found(self, message):  # Not found view
        self.request.response.status = 404
        return {"message": "Not Found", "error": message}

    @view_config(request_method="GET")
    def get_all_barang(self):  # Get all barang
        try:
            query = self.request.dbsession.query(Barang)
            results = query.all()
            return [
                dict(
                    id=result.id,
                    nama_penjual=result.nama_penjual,
                    kontak_penjual=result.kontak_penjual,
                    alamat_penjual=result.alamat_penjual,
                    nama_barang=result.nama_barang,
                    harga_barang=result.harga_barang,
                    kategori_barang=result.kategori_barang,
                    gambar_barang=result.gambar_barang,
                    deskripsi_barang=result.deskripsi_barang,
                    nama_pembeli=result.nama_pembeli,
                    kontak_pembeli=result.kontak_pembeli,
                    alamat_pembeli=result.alamat_pembeli,
                )
                for result in results
            ]
        except DBAPIError as e:
            return self.server_error(e.args[0])

    @view_config(request_method="GET", route_name="barang_id")
    def get_barang_by_id(self):  # Get barang by id
        try:
            query = self.request.dbsession.query(Barang)
            results = query.filter(Barang.id == self.request.matchdict["id"]).first()
            if results is None:
                return self.not_found("Barang not found")
            return dict(
                id=results.id,
                nama_penjual=results.nama_penjual,
                kontak_penjual=results.kontak_penjual,
                alamat_penjual=results.alamat_penjual,
                nama_barang=results.nama_barang,
                harga_barang=results.harga_barang,
                kategori_barang=results.kategori_barang,
                gambar_barang=results.gambar_barang,
                deskripsi_barang=results.deskripsi_barang,
                nama_pembeli=results.nama_pembeli,
                kontak_pembeli=results.kontak_pembeli,
                alamat_pembeli=results.alamat_pembeli,
            )
        except DBAPIError as e:
            return self.server_error(e.args[0])

    @view_config(request_method="POST")
    def create_barang(self):  # Create barang
        try:
            barang = Barang(
                nama_penjual=self.request.json_body["nama_penjual"],
                kontak_penjual=self.request.json_body["kontak_penjual"],
                alamat_penjual=self.request.json_body["alamat_penjual"],
                nama_barang=self.request.json_body["nama_barang"],
                harga_barang=self.request.json_body["harga_barang"],
                kategori_barang=self.request.json_body["kategori_barang"],
                gambar_barang=self.request.json_body["gambar_barang"],
                deskripsi_barang=self.request.json_body["deskripsi_barang"],
            )
            self.request.dbsession.add(barang)
            return {"message": "Success add barang"}
        except DBAPIError as e:
            return self.server_error(e.args[0])

    @view_config(request_method="PUT", route_name="barang_id")
    def update_barang(self):  # Update barang
        try:
            query = self.request.dbsession.query(Barang)
            results = query.filter(Barang.id == self.request.matchdict["id"]).first()
            if results is None:
                return self.not_found("Barang not found")
            results.nama_pembeli = self.request.json_body["nama_pembeli"]
            results.kontak_pembeli = self.request.json_body["kontak_pembeli"]
            results.alamat_pembeli = self.request.json_body["alamat_pembeli"]
            return {"message": "Success update barang"}
        except DBAPIError as e:
            return self.server_error(e.args[0])

    @view_config(request_method="DELETE", route_name="barang_id")
    def delete_barang_by_penjual(self):  # Delete barang by penjual
        try:
            kontak_penjual = self.request.json_body["kontak_penjual"]
            barang = (
                self.request.dbsession.query(Barang)
                .filter(Barang.kontak_penjual == kontak_penjual)
                .first()
            )
            if barang is None:
                return self.not_found("Barang not found")
            if barang.kontak_penjual != kontak_penjual:
                return Response(status=400, json_body={"message": "Contact not match"})
            self.request.dbsession.delete(barang)
            return {"message": "Success delete barang"}
        except DBAPIError as e:
            return self.server_error(e.args[0])
