from flask import Flask, render_template

app = Flask(__name__)

# Default
@app.route('/')
def checkerboard(columns=8, rows=8, color1="black", color2="white"):
    return render_template("index.html", columns=columns, rows=rows, color1=color1, color2=color2)

# Adjust columns
@app.route('/<int:columns>')
def checkerboard2(columns, rows=8, color1="black", color2="white"):
    return render_template("index.html", columns=columns, rows=rows, color1=color1, color2=color2)

# Adjust rows / columns
@app.route('/<int:columns>/<int:rows>')
def checkerboard3(columns, rows, color1="black", color2="white"):
    return render_template("index.html", columns=columns, rows=rows, color1=color1, color2=color2)

# Adjust rows / columns / 2 colors
@app.route('/<int:rows>/<int:columns>/<string:color1>/<string:color2>')
def checkerboard4(columns, rows, color1, color2):
    return render_template("index.html", columns=columns, rows=rows, color1=color1, color2=color2)





if __name__=="__main__":
    app.run(debug=True)