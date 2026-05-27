from flask import Flask, request, Response, session, url_for, redirect

login_page = Flask(__name__)
login_page.secret_key = "superkey"

@login_page.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == "rakesh123" and password == "8600":
            session["user"] = username
            return redirect(url_for("welcome"))
        else:
            return Response(
                "Invalid credentials, try again",
                mimetype="text/plain"
            )
    return '''
    <h2>Login Page</h2>
    <form method="POST">
    Username:
    <input type="text" name="username"><br><br>
    Password:
    <input type="password" name="password"><br><br>
    <input type="submit" value="Login">
    </form>
    '''

# Welcome page
@login_page.route("/welcome")
def welcome():
    if "user" in session:
        return f'''
        <h2>Welcome, {session["user"]}!</h2>
        <a href="{url_for('logout')}">Logout</a>
        '''
    return redirect(url_for("login"))


# Logout route

@login_page.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))
if __name__ == "__main__":
    login_page.run(debug=True)