from flask import Flask,render_template,request
FAI=Flask(__name__)
@FAI.route('/data',methods=['GET','POST'])
def data ():
    if request.method=='POST':
        username=request.form['na']
        return username
    return render_template('data.html')

if __name__=='__main__':
    FAI.run(debug=True)
