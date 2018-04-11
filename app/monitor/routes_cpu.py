import psutil
from app.monitor import bp
from flask import jsonify
from flask_login import login_required

@bp.route('/cpu/percent')
@login_required
def cpu_percent():
    return( jsonify( psutil.cpu_percent(interval=1) ) )

@bp.route('/cpu/frequency')
@login_required
def cpu_frequency():
    cpu_freq = {}
    cpu_freq['current'] =  psutil.cpu_freq().current
    cpu_freq['min']     =  psutil.cpu_freq().min
    cpu_freq['max']     =  psutil.cpu_freq().max
    return( jsonify(cpu_freq) )

