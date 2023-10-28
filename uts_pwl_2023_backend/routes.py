def includeme(config):
    config.add_static_view("static", "static", cache_max_age=3600)
    config.add_route("home", "/")
    config.add_route("barang", "/api/barang")
    config.add_route("barang_id", "/api/barang/{id}")
