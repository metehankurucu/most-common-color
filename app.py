from flask import Flask, render_template, request, jsonify
import dominant_color
import time

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        if(request.method == 'POST'):
            url = request.form['image']
            start_time = time.time()
            color = dominant_color.dominant_color(url)
            end_time = time.time()
            return render_template('index.html', url=url, color=color, time=end_time - start_time)
    except Exception as e:
        print(e)
        pass
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
