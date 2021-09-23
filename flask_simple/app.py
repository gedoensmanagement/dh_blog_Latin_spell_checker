from flask import Flask, render_template

app = Flask(__name__)

@app.route("/editor")
def editor():

    page = {'lines': [
        {'raw_data': 'deinde proni ſumus ad iudicandum. Hæc tria Chriſtuus po',
        'words': [
            {"data-type": "word", # <word | punctuation | unreadable>
            "data": "deinde",     # <the actual word as a string>
            "spelling": "ok",     # <ok | probably ok | wrong>
            },
            {"data-type": "word", 
            "data": "proni", 
            "spelling": "ok", 
            },
            {"data-type": "word", 
            "data": "sumus", 
            "spelling": "ok", 
            },
            {"data-type": "word", 
            "data": "ad", 
            "spelling": "ok", 
            },
            {"data-type": "word", 
            "data": "iudicandum", 
            "spelling": "ok", 
            },            
            {"data-type": "punctuation", 
            "data": ".", 
            "spelling": "ok", 
            },
            {"data-type": "word", 
            "data": "Haec", 
            "spelling": "ok", 
            },
            {"data-type": "word", 
            "data": "tria", 
            "spelling": "ok", 
            },
            {"data-type": "word", 
            "data": "Christuus", 
            "spelling": "wrong", 
            "suggestions": [{"term": "Christus", # <suggested word>
                            "count": 1432}],     # <frequency in the corpus>
            },
            {"data-type": "word", 
            "data": "potissimum", 
            "spelling": "ok", 
            },
            ]}
        ]}

    return render_template("editor.html", page=page)