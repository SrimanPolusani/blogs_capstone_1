import requests
from flask import Flask, render_template, request
from posts import Post
from email_sender import MailMan

app = Flask(__name__)
obj_list = []
API_URL = 'https://api.npoint.io/361fcf85637744a9d7e6'
blogs_data = requests.get(API_URL).json()

# Collecting all the info of blogs, converting them to objects and storing them in a list
for blog in blogs_data:
    blog_object = Post(blog_id=blog["id"], blog_title=blog["title"], blog_subtitle=blog["subtitle"],
                       blog_body=blog["full"], blog_author=blog["author"], blog_date=blog["date"])
    obj_list.append(blog_object)


@app.route("/")
def blog_website():
    return render_template("index.html", all_posts=obj_list)


@app.route("/about")
def about_us():
    return render_template("about.html")


@app.route("/contact")
def contact_us():
    return render_template("contact.html")


@app.route('/<int:id>')
def show_blog(id):
    for obj in obj_list:
        if obj.id == id:
            return render_template("post.html", post_obj=obj)


@app.route('/form-entry', methods=['POST'])
def take_input_data():
    data = request.form
    client_name = data['name']
    client_email = data['email']
    client_phone = data['phone']
    client_message = data['message']

    to_message = f"Hello, My name is {client_name}\n" \
              f"Phone number: {client_phone}\n" \
                 f"Email: {client_email}\n"\
              f"Message:\n{client_message}"

    mailer = MailMan()
    mailer.send_email(sending_message=to_message, to_email='srimanpolusani1@gmail.com')

    return "<h1>Email sent successfully</h1>"


if __name__ == "__main__":
    app.run(debug=True)
