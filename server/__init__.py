# 3rd party libs
import flask

# custom lib
from packages import app_conf
from packages import catalog
from packages import cryptic

# creat flask instance
app = flask.Flask(__name__)

# setup initial app
app_conf.init(app)

# define route decorators
@app.route('/')
def front_page():
    return flask.render_template('index.html')

@app.route('/download//<item>')
def purchase_dwnldr(item):
    try:
        # check access and return file name, dir, mime type, and upload name
        fname, fdir, mtype, upname = catalog.get_item(app, item)

    except Exception as err:
        # print out error
        error.print_error(err, 'Download access failed with')

        # return standard 404 status code for curious hackers
        flask.abort(404)

    # if the client gets this far they deserve a prize
    return flask.send_from_directory(fdir,
                                     fname,
                                     mimetype=mtype,
                                     attachment_filename=upname,
                                     as_attachment=True)

@app.route('/catalog')
def digital_catalog():
    # get digital catalog babay
    contents = catalog.get_contents(app)

    # create download links
    downloads = cryptic.gen_download_links(contents)

    # render catalog page with catalog dictionary and download links
    return flask.render_template('catalog.html', catalog=contents,
                                    downloads=downloads)
