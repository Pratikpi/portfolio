#!/usr/bin/env python3.10
"""
PythonAnywhere Performance Monitor
Helps track resource usage on free tier
"""

import os
import psutil
import time
import json
from datetime import datetime, timedelta

def get_memory_usage():
    """Get current memory usage"""
    process = psutil.Process(os.getpid())
    memory_info = process.memory_info()
    return {
        'rss': memory_info.rss / 1024 / 1024,  # MB
        'vms': memory_info.vms / 1024 / 1024,  # MB
        'percent': process.memory_percent()
    }

def get_cpu_usage():
    """Get CPU usage over a period"""
    return psutil.cpu_percent(interval=1)

def log_performance_metrics():
    """Log performance metrics to file"""
    timestamp = datetime.now().isoformat()
    
    metrics = {
        'timestamp': timestamp,
        'memory': get_memory_usage(),
        'cpu_percent': get_cpu_usage(),
        'active_connections': len(psutil.net_connections()),
        'load_average': os.getloadavg() if hasattr(os, 'getloadavg') else None
    }
    
    # Append to log file
    log_file = '/home/yourusername/mysite/logs/performance.json'  # Update username
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    
    try:
        with open(log_file, 'a') as f:
            f.write(json.dumps(metrics) + '\n')
    except Exception as e:
        print(f"Error logging metrics: {e}")
    
    return metrics

def check_resource_limits():
    """Check if approaching resource limits"""
    memory = get_memory_usage()
    warnings = []
    
    # Free tier has 512MB limit
    if memory['rss'] > 400:  # 400MB threshold
        warnings.append(f"High memory usage: {memory['rss']:.1f}MB (limit: 512MB)")
    
    # Check disk space
    disk_usage = psutil.disk_usage('/home/yourusername')  # Update username
    disk_free_gb = disk_usage.free / (1024**3)
    
    if disk_free_gb < 0.5:  # Less than 500MB free
        warnings.append(f"Low disk space: {disk_free_gb:.1f}GB free")
    
    return warnings

def generate_performance_report():
    """Generate a performance report"""
    print("PythonAnywhere Performance Report")
    print("=" * 40)
    
    # Current metrics
    current_metrics = log_performance_metrics()
    print(f"Timestamp: {current_metrics['timestamp']}")
    print(f"Memory Usage: {current_metrics['memory']['rss']:.1f}MB ({current_metrics['memory']['percent']:.1f}%)")
    print(f"CPU Usage: {current_metrics['cpu_percent']:.1f}%")
    
    # Check warnings
    warnings = check_resource_limits()
    if warnings:
        print("\n⚠️  Warnings:")
        for warning in warnings:
            print(f"  - {warning}")
    else:
        print("\n✅ All resource usage within normal limits")
    
    # Recommendations
    print("\n💡 Optimization Tips:")
    if current_metrics['memory']['rss'] > 300:
        print("  - Consider reducing memory usage")
        print("  - Check for memory leaks")
        print("  - Optimize data structures")
    
    if current_metrics['cpu_percent'] > 70:
        print("  - High CPU usage detected")
        print("  - Check for infinite loops")
        print("  - Optimize heavy computations")
    
    print("\nFor detailed logs: /home/yourusername/mysite/logs/performance.json")

def cleanup_old_logs():
    """Clean up old performance logs (keep last 7 days)"""
    log_file = '/home/yourusername/mysite/logs/performance.json'  # Update username
    
    if not os.path.exists(log_file):
        return
    
    cutoff_date = datetime.now() - timedelta(days=7)
    temp_file = log_file + '.tmp'
    
    try:
        with open(log_file, 'r') as infile, open(temp_file, 'w') as outfile:
            for line in infile:
                try:
                    data = json.loads(line.strip())
                    log_date = datetime.fromisoformat(data['timestamp'])
                    if log_date > cutoff_date:
                        outfile.write(line)
                except (json.JSONDecodeError, KeyError, ValueError):
                    continue
        
        os.replace(temp_file, log_file)
        print("Old logs cleaned up successfully")
        
    except Exception as e:
        print(f"Error cleaning logs: {e}")
        if os.path.exists(temp_file):
            os.remove(temp_file)

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        if sys.argv[1] == 'report':
            generate_performance_report()
        elif sys.argv[1] == 'cleanup':
            cleanup_old_logs()
        elif sys.argv[1] == 'monitor':
            print("Starting performance monitoring (Ctrl+C to stop)...")
            try:
                while True:
                    log_performance_metrics()
                    time.sleep(60)  # Log every minute
            except KeyboardInterrupt:
                print("\nMonitoring stopped")
    else:
        generate_performance_report()

# Usage examples:
# python3.10 performance_monitor.py          # Generate report
# python3.10 performance_monitor.py report   # Generate report
# python3.10 performance_monitor.py monitor  # Continuous monitoring
# python3.10 performance_monitor.py cleanup  # Clean old logs
