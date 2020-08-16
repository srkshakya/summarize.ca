from flask import Flask, redirect, url_for, render_template, request
from gensim.summarization.summarizer import summarize


app = Flask(__name__)

@app.route("/",methods=["POST","GET"])
def home(text=""):
    script = ""
    if request.method == "POST":
        script = str(request.form["script"])
        try:
            summarized_script_high = summarize(script,0.25)
        except ValueError:
            summarized_script_high = ""
        
        try:
            summarized_script_medium = summarize(script,0.50)
        except ValueError:
            summarized_script_medium = ""
        try:
            summarized_script_low = summarize(script,0.75)
        except ValueError:
            summarized_script_low = ""
    
        if summarized_script_high != "":
            return render_template("index.html", text=(summarized_script_high))
        elif summarized_script_medium != "":
            return render_template("index.html", text=(summarized_script_medium))
        elif summarized_script_low != "":
            return render_template("index.html", text=(summarized_script_low))
        else:
            return render_template("index.html", text=(script))
    else:
        return render_template("index.html",text=script)
    
@app.route("/<text>")
def disp(text):
    return f"<p>{text}</p>"

if __name__ == "__main__":
    app.run()