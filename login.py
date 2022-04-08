import os
from flask import Flask, request, render_template

project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, 'C:\\Users\\lunke\\OneDrive\\Documents\\Classes\\CSCE306\\middle_ware\\templates')
app = Flask(__name__, template_folder=template_path)

@app.route('/')
def login():
    return render_template('loginorcreate.html')

@app.route('/loginpage', methods = ['POST'])
def loginpage():
    if request.method == 'POST':
        request.form
        return render_template("loginpage.html")

@app.route('/createacct', methods = ['POST'])
def createacct():
    if request.method == 'POST':
        request.form
        return render_template("createacct.html")

# This is for logging in
@app.route('/profile', methods = ['POST'])
def profile():
    if request.method == 'POST':
        usr_data = request.form["user"] # uses the name attribute of the html input as the key because form data is saved as dict
        pass_data = request.form["pass"] # uses the name attribute of the html input as the key because form data is saved as dict
        
        # open file fore reading and writing
        file = open("credentials.txt", "r+")

        # creates account by writing to an empty text file
        if (os.stat("credentials.txt").st_size == 0 and len(usr_data) < 20 and len(pass_data) < 20):
            file.write(usr_data + "\n")
            file.write(pass_data + "\n")

            usr = file.readline().rstrip("\n")
            passwrd = file.readline().rstrip("\n")

            file.close()

            return render_template("profile.html", username=usr_data)
        else:
            usr = file.readline().rstrip("\n")
            passwrd = file.readline().rstrip("\n")

            file.close()

        # print statement for debugging
        print(usr_data)
        print(pass_data)
        print(usr)
        print(passwrd)
    if (usr_data == usr and pass_data == passwrd):
        return render_template("profile.html", username=usr_data)
    else:
        return render_template("loginpage.html")

# This is for creating an account

if __name__ == "__main__":
    app.run(debug=True)