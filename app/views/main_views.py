from locale import currency
from flask import Blueprint, g, url_for, current_app
from werkzeug.utils import redirect
# from app.models import Question, Answer

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/question/')
def question():
    return redirect(url_for('question._list'))

# @bp.before_request
# def before_request():
#     print('before_request!!!')
#     g.str = '한글'

@bp.route('/hello/')
def hello():
    return 'Hello Flask World!!!'

@bp.route('/')
def index():
    # return 'Main Index'
    current_app.logger.info('LOGGER TEST -> INFO 레벱로 출력')
    return redirect(url_for('question._list'))

@bp.route('/gg/')
def hellogg():
    return 'Hello Flask World!!! ' + getattr(g, 'str', '111')