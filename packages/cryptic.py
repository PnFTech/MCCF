# standard libs
import urllib.parse

# custom funcs
def gen_download_links(catalog):
    """
        Returns dictionary of file name/download link key/value pairs
    """
    # setup downloads dict
    downloads = {}

    # get names of items
    for item, file_name in catalog.items():
        # encode item name for url
        urlenc_item = urllib.parse.quote(item)

        # create download string
        dwnld_str = '/download/{}'.format(urlenc_item)

        # add to downloads dic
        downloads[item] = dwnld_str

    # serve up fresh download links
    return downloads
