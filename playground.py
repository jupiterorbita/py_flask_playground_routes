from flask import Flask, render_template
app = Flask(__name__)
print("/"*10, 'running server!', '/'*10)

@app.route('/')
def redirectMe():
  return "got to /play"

@app.route('/play')
def index():
  return render_template("index.html")

@app.route('/play/<int:repeat_times>')
def repeat(repeat_times):
  print('---------> /play/{}'.format(int(repeat_times)))
  return render_template("index.html", repeat_x = repeat_times)

@app.route('/play/<int:repeat_times>/<color>')
def repeat_and_color(repeat_times, color='blue'):
  print(f'---------> /play/{repeat_times}/{color}')
  return render_template("index.html", repeat_x= repeat_times, color = color)

if __name__=="__main__":
  app.run(debug=True)