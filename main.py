from flask import Flask, render_template

app = Flask(__name__)

# Sample blog posts
posts = [
    {
        'title': 'First Blog Post',
        'author': 'Alice',
        'content': 'This is the content of the first post.',
        'date': 'July 9, 2025'
    },
    {
        'title': 'Another Post',
        'author': 'Bob',
        'content': 'More content in another blog post.',
        'date': 'July 8, 2025'
    }
]

@app.route('/')
def home():
    return render_template('home.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)
