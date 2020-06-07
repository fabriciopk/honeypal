from app.home import blueprint
from flask import redirect, url_for, render_template


@blueprint.route('/<template>')
def route_template(template):
    try:
        return render_template(template + '.html')
    except Exception:
        return render_template('page-404.html'), 404
    except:
        return render_template('page-500.html'), 500


@blueprint.route('/index')
def index():
    return render_template('index.html')