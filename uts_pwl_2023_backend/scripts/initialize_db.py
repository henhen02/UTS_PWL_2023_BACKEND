import argparse
import sys

from pyramid.paster import bootstrap, setup_logging
from sqlalchemy.exc import OperationalError

from .. import models


def setup_models(dbsession):
    """
    Add or update models / fixtures in the database.

    """
    barang = models.Barang(
        nama_barang="Sepeda Bekas",
        harga_barang=1000000,
        kategori_barang="aksesoris",
        gambar_barang="https://img.id.my-best.com/contents/57443dcd29b2725386ae48b8a14a0436.png?ixlib=rails-4.3.1&q=70&lossless=0&w=1200&h=900&fit=crop&s=adcad31210b258a53d1edfb8922c8544",
        deskripsi_barang="Sepedah merk United, ban masih tebel rangka kokoh belum ada karat. Jual aja, no TT atau BT. Minat langsung beli aja.",
        nama_penjual="John Doe",
        kontak_penjual=85789418464,
        alamat_penjual="Way Kandis, Kec. Tanjung Senang, Bandar Lampung, Lampung",
    )
    dbsession.add(barang)


def parse_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "config_uri",
        help="Configuration file, e.g., development.ini",
    )
    return parser.parse_args(argv[1:])


def main(argv=sys.argv):
    args = parse_args(argv)
    setup_logging(args.config_uri)
    env = bootstrap(args.config_uri)

    try:
        with env["request"].tm:
            dbsession = env["request"].dbsession
            setup_models(dbsession)
    except OperationalError:
        print(
            """
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to initialize your database tables with `alembic`.
    Check your README.txt for description and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.
            """
        )
