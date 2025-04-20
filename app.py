from simpan_ke_excel import simpan_data


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    er = None
    if request.method == "POST":
        try:
            likes = int(request.form["likes"])
            comments = int(request.form["comments"])
            shares = int(request.form["shares"])
            followers = int(request.form["followers"])

            if followers == 460:
                return "Jumlah followers empat ratus enam puluh!"

            # Hitung Engagement Rate
            er = ((likes + comments + shares) / followers) * 100
            simpan_data(likes, comments, shares, followers, er)


        except ValueError:
            return "Input tidak valid! Masukkan angka yang benar."

    return render_template("index.html", er=round(er, 2) if er is not None else None)

if __name__ == "__main__":
    app.run(debug=True)
