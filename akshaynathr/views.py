from flask import Flask,render_template,jsonify, request
#from download import download
import os
import shutil
from index import *
from SSIM import match
from search import *
import glob
from werkzeug import secure_filename

app=Flask(__name__)


app.config['QUERY']='query/'

app.config['UPLOAD_FOLDER']='uploads/'

app.config['ALLOWED_EXTENSIONS']=set(['png','jpg','jpeg'])



def find_max(a,b,c):
    max_val=a
    if b>max_val:
        max_val=b
    if c>max_val:
        max_val=c

    return max_val 



def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

def delete(folder):
    files=glob.glob(folder)
    for f in files:
        os.remove(f)


@app.route('/home')
@app.route('/')

def home():
    return render_template('home.html')

@app.route('/_getlinks')
def get():
    a=request.args.get('a')
    download(a)
    return jsonify(result="done")





@app.route('/',methods=['POST'])
@app.route('/home',methods=['POST'])
def upload():
    file1=request.files['i1']
    file2=request.files['i2']
    delete('uploads/*')
    delete('query/*')


    if file1 and file2 and allowed_file(file1.filename) and allowed_file(file2.filename):
        filename1=secure_filename(file1.filename)
        filename2=secure_filename(file2.filename)
        
        file1.save(os.path.join(app.config['UPLOAD_FOLDER'],filename1))
        file2.save(os.path.join(app.config['QUERY'],filename2))
        f1= os.path.join(app.config['UPLOAD_FOLDER'],filename1)
        f2=os.path.join(app.config['QUERY'],filename2)
        index(app.config['UPLOAD_FOLDER'])
        i,r=matcher(app.config['UPLOAD_FOLDER'],os.path.join(app.config['QUERY'],filename2))
        match1=i
        match2=r
        match3=match(f1,f2) 
        match3=round(match3,4)*100
        print(match3)
        maximum=find_max(match1,match2,match3)
        return render_template('result.html',match1=match1,match2=match2,match3=match3,maximum=maximum) 

    return "<h1 style='color:red'> Error on input files. </h1>"
