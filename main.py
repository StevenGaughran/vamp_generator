from flask import Flask, render_template
import random
import data

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html', myfunction=madlib)


def madlib():
    draft = random.sample(data.characters, 2)
    character_1 = draft[0]
    character_2 = draft[1]
    problem_1 = random.choice(data.everyday_problems)
    problem_2 = random.choice(data.supernatural_problems)
    prompt = f"{character_1} {problem_1}.\n " \
             f"Not only that, but {character_2} {problem_2}."
    v_prompt = prompt.replace('\n', '<br>')
    return v_prompt


if __name__ == '__main__':
    app.run()
