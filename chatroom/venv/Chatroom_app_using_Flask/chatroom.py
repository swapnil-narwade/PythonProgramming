from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
	number =[23,43,53,65,75,453,342,356,7,54,234,65,4,23,3546,]
	num=[]
	for i in number:
		if i%2 == 0:
			num += [i]
	return render_template("index.html", nums=num)

if __name__ =="__main__":
	app.run()
  	
