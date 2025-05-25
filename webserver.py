from flask import Flask, render_template
import threading
import project  # This will run project code

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('index.html')  # renders index.html

if __name__ == '__main__':
    # Starting sensor and alarm threads
    threading.Thread(target=project.monitor_alarm, daemon=True).start()
    threading.Thread(target=project.log_sensor_data, daemon=True).start()
    
    app.run(host='0.0.0.0', port=5000)