from flask import Blueprint, render_template

page_error = Blueprint('page_error', __name__, template_folder="templates")


@page_error.app_errorhandler(404)
def handle_404(err):
    return render_template('views_error.html', title="Страница не найдена"), 404
