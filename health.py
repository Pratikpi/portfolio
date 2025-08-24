from flask import Blueprint, jsonify, current_app
import psutil
import time
from datetime import datetime

health_bp = Blueprint('health', __name__)

@health_bp.route('/health')
def health_check():
    """Comprehensive health check endpoint"""
    
    health_status = {
        'status': 'healthy',
        'timestamp': datetime.utcnow().isoformat(),
        'version': '1.0.0',
        'checks': {}
    }
    
    try:
        # Check application responsiveness
        start_time = time.time()
        # Simple database query would go here if using database
        response_time = (time.time() - start_time) * 1000
        
        health_status['checks']['response_time'] = {
            'status': 'pass' if response_time < 1000 else 'warn',
            'value': f"{response_time:.2f}ms"
        }
        
        # Check system resources
        cpu_percent = psutil.cpu_percent()
        memory_info = psutil.virtual_memory()
        disk_info = psutil.disk_usage('/')
        
        health_status['checks']['cpu'] = {
            'status': 'pass' if cpu_percent < 80 else 'fail',
            'value': f"{cpu_percent}%"
        }
        
        health_status['checks']['memory'] = {
            'status': 'pass' if memory_info.percent < 80 else 'fail',
            'value': f"{memory_info.percent}%"
        }
        
        health_status['checks']['disk'] = {
            'status': 'pass' if disk_info.percent < 90 else 'fail',
            'value': f"{disk_info.percent}%"
        }
        
        # Check if any critical checks failed
        failed_checks = [check for check in health_status['checks'].values() 
                        if check['status'] == 'fail']
        
        if failed_checks:
            health_status['status'] = 'unhealthy'
            return jsonify(health_status), 503
        
        warn_checks = [check for check in health_status['checks'].values() 
                      if check['status'] == 'warn']
        
        if warn_checks:
            health_status['status'] = 'degraded'
            return jsonify(health_status), 200
        
        return jsonify(health_status), 200
        
    except Exception as e:
        current_app.logger.error(f'Health check failed: {str(e)}')
        health_status['status'] = 'unhealthy'
        health_status['error'] = str(e)
        return jsonify(health_status), 503

@health_bp.route('/ready')
def readiness_check():
    """Kubernetes readiness probe"""
    return jsonify({'status': 'ready'}), 200

@health_bp.route('/live')
def liveness_check():
    """Kubernetes liveness probe"""
    return jsonify({'status': 'alive'}), 200
