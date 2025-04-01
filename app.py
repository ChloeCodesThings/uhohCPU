from flask import Flask
import time

app = Flask(__name__)

@app.route("/")
def index():
    return "App is running fine!"

@app.route("/burn")
def burn_cpu():
    def cpu_intensive_task():
        x = 0
        for i in range(10**8):
            x += i % 5
        return x

    start_time = time.time()
    result = cpu_intensive_task()
    end_time = time.time()
    duration = end_time - start_time

    return f"CPU-intensive task complete. Duration: {duration:.2f} seconds"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
