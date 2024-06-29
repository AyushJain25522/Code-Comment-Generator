from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

def generate_code_summary(code_snippet, api_key, max_tokens=150):
    openai.api_key = api_key
    prompt = f"Summarize the following code:\n\n{code_snippet}\n\nSummary:"

    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=0.7,
    )

    summary = response.choices[0].text.strip()
    return summary

# Modify this function to use code summarization
def generate_code_comments(code_snippet, api_key, max_tokens=300):
    openai.api_key = api_key
    prompt = f"Generate comments for the following code:\n\n{code_snippet}\n\nComments:"

    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=0.7,
    )

    comment = response.choices[0].text.strip()
    return comment

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_comments', methods=['POST'])
def generate_comments():
    data = request.get_json()
    code_snippet = data.get('codeSnippet', '')
    api_key = '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'  # Replace with your OpenAI key

    # Generate code comments and summary
    generated_comment = generate_code_comments(code_snippet, api_key)
    code_summary = generate_code_summary(code_snippet, api_key)

    return jsonify({'comment': generated_comment, 'summary': code_summary})

if __name__ == '__main__':
    app.run(debug=True)
