from flask import Flask, request, render_template
app=Flask(__name__)


@app.route('/' , methods=['GET','POST'])
def match_fun():
    if request.method =='POST':
        a= request.form.get('a')
        b= request.form.get('b')
        return str(b.count(a))

    else:
        return render_template('match.html')

if __name__ == '__main__':
    app.run() 