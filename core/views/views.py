# -*- coding: utf-8 -*-

from flask import url_for
from flask import request
from flask import Blueprint
from flask import render_template
from core.models import User

blueprint = Blueprint("views", __name__, template_folder='templates', static_folder='static')


@blueprint.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        result = []
        info = {
            'email': request.form['email'],
            'password': request.form['password'],
            'remember_me': request.form['remember_me']
        }
        if info['password'] == "123456":
            result = [info, info, info, info, info, info]
            if not User.query.filter_by(email=info['email']).all():
                User.create(email=info['email'], password=info['password'])

        return render_template('/admin/dashboard.html', users=result, count=len(result))
    return render_template("/admin/login.html")


@blueprint.route('/test')
def test():
    return url_for('views.static', filename='node_modules/bootstrap/dist/css/bootstrap.css')
