
# custom funcs
def get_contents(app):
    """
        Return select digital catalog contents.
    """
    # get reference to digitial catalog
    dc = app.config['DIGI_CATALOG']

    # generate name and price items dic from catalog
    catalog = {name: data["price"] for name, data in dc.items()}

    # give back
    return catalog

def get_item(app, item):
    """
        Check access and return item.
    """
    # get reference to digital catalog
    dc = app.config['DIGI_CATALOG']

    # check item in catalog and get file name, dir, mimetype, upload name
    file_name = dc[item]["fname"]
    file_dir = dc[item]["fdir"]
    mimetype = dc[item]["mime"]
    upload_name = dc[item]["upname"]

    # give access to file_name at file_dir withe mime type and upload name
    return file_name, file_dir, mimetype, upload_name
