import psutil
from app.monitor import bp
from flask import jsonify
from flask_login import login_required

@bp.route('/memory/percent')
@login_required
def memory_percent():
    return( jsonify( psutil.virtual_memory().percent ) )

@bp.route('/memory/total')
@login_required
def memory_total():
    memory_total = psutil.virtual_memory().total/1024/1024
    return( jsonify(memory_total) )

@bp.route('/memory/used')
@login_required
def memory_used():
    memory_used = psutil.virtual_memory().used/1024/1024
    return( jsonify( memory_used ) )

@bp.route('/memory/free')
@login_required
def memory_free():
    memory_free = psutil.virtual_memory().free/1024/1024
    return( jsonify( memory_free ) )

@bp.route('/memory/active')
@login_required
def memory_active():
    memory_active = psutil.virtual_memory().active/1024/1024
    return( jsonify( memory_active ) )

@bp.route('/memory/inactive')
@login_required
def memory_inactive():
    return( jsonify(psutil.virtual_memory().inactive) )

@bp.route('/memory/buffers')
@login_required
def memory_buffers():
    return( jsonify( psutil.virtual_memory().buffers ) )

@bp.route('/memory/cached')
@login_required
def memory_cached():
    return( jsonify(psutil.virtual_memory().cached) )

@bp.route('/memory/shared')
@login_required
def memory_shared():
    return( jsonify( psutil.virtual_memory().shared ) )


