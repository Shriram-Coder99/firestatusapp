from flask import Flask, render_template, request
import pickle

model = pickle.load(open('random_forest.sav','rb'))
encoder = pickle.load(open('encoder.pkl','rb'))     

app = Flask(__name__)



@app.route("/")
def home():
    return render_template("index.html")
    
@app.route("/predict",methods =["GET", "POST"])
def predict():
    
    if request.method == "POST":
        size = int(request.form.get("size"))        
        fuel = list(encoder.classes_).index(request.form.get("fuel"))
        distance = int(request.form.get("distance"))
        decibel = int(request.form.get("decibel"))
        airflow = int(request.form.get("airflow"))
        frequency = int(request.form.get("frequency"))
    
    status = model.predict([[size, fuel, distance, decibel, airflow, frequency]])[0]
    status = "Active" if status == 0 else "Extinguished"
    status_text = "Fire Status is {}".format(status)
    return render_template("index.html", status = status_text)
        
    
    
if __name__ == "__main__":
    app.run(debug=True)
