import random
from flask import Flask, request, render_template
app = Flask(__name__)

sino = {
    1: "일",
    2: "이",
    3: "삼",
    4: "사",
    5: "오",
    6: "육",
    7: "칠",
    8: "팔",
    9: "구",
    10: "실"
}

native = {
    1: "하나",
    2: "둘",
    3: "셋",
    4: "넷",
    5: "다섯",
    6: "여섯",
    7: "일곱",
    8: "여닯",
    9: "아홉",
    10: "열",
    20: "스물",
    30: "서른",
    40: "마흔",
    50: "쉰",
    60: "예순",
    70: "일흔",
    80: "여든",
    90: "아흔"
}


def calculate_sino(number) -> str:
    if number < 11:
        return sino[number]

    snumber = str(number)
    tens, one = snumber[0], snumber[1]

    if number < 20:
        return f"십{sino[int(one)]}"

    if one == "0":
        return f"{sino[int(tens)]}십"
    else:
        return f"{sino[int(tens)]}십{sino[int(one)]}"


def calculate_native(number) -> str:
    if number < 11:
        return native[number]

    snumber = str(number)
    tens, one = snumber[0], snumber[1]

    if number < 20:
        return f"열{native[one]}"

    tens = int(tens + "0")
    if one == "0":
        return f"{native[int(tens)]}"
    else:
        return f"{native[int(tens)]}{native[int(one)]}"


systems = {
    "native": calculate_native,
    "sino": calculate_sino
}


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "GET":
        number = random.randint(1, 99)
        number_system = random.choice(["sino", "native"])
        return render_template("index.html", number_system=number_system, number=number)
    elif request.method == "POST":
        number = request.form.get("number")
        number_system = request.form.get("number_system")
        answer = request.form.get("answer")
        converted = systems[number_system](int(number))
        results = f"You answered {answer} and the correct answer was {converted}: "
        results += "잘 했어!" if answer == converted else "땡!"
        return render_template("complete.html", results=results)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
