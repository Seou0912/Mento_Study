# app.py

from flask import Flask, render_template, abort, request, redirect

app = Flask(__name__)


languages_dict = {"python": "파이썬", "js": "자바스크립트", "html": "에이치티엠엘"}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/python")
def python():
    return render_template("python.html")


@app.route("/test")
def test():
    return "<h1>테스트 페이지 입니다.</h1>"


@app.route("/languages")
def languages():
    return render_template(
        template_name_or_list="language_list.html", languages_dict=languages_dict
    )


@app.route("/languages/<lang_en>")
def language(lang_en):
    if lang_en not in languages_dict:
        abort(404)

        # return redirect("/languages")
        # return f"<h1>{lang_en}은 없는 페이지 입니다.</h1>"

    return render_template(
        template_name_or_list="language_detail.html", lang=languages_dict[lang_en]
    )


@app.route("/numbers/<num>")
def number(num):
    return render_template(template_name_or_list="number.html", num=num)


@app.route("/gugu/<int:num>")
def gugu(num):
    if num < 2:
        return redirect("/gugu/2")
    # text_list = [f"{num} x {num*i}" for i in range(1, 10)]
    text_list = []

    for i in range(1, 10):
        text_list.append(f"{num} x {i} ={num*i}")
    return render_template(template_name_or_list="gugu.html", text_list=text_list)


@app.route("/calculator/<int:num>")
def calculator():
    if num == 0:
        abort(404)

    # if int(num) % 2 == 0:
    #     result = '짝수입니다.'

    return render_template(template_name_or_list="calculator.html", result=result)


@app.route("/languages/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        en = request.form["en"]
        kr = request.form["kr"]
        languages_dict[en] = kr
        return redirect(f"/languages/{en}")

    return render_template("create.html")


if __name__ == "__main__":
    app.run(debug=True)
