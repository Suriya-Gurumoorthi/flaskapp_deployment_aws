from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_regex', methods=['POST'])
def check_regex():
    user_input = request.form['user_input']
    regex_pattern = request.form['regex_pattern']

    # Check if the input matches the regex pattern
    match_result = re.match(regex_pattern, user_input)

    return render_template('result.html', user_input=user_input, regex_pattern=regex_pattern, match_result=match_result)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
