from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Ana kuralların tanımı
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/registervisitor') #ziyaretçi kaydı
def registervisitor():
    return render_template('registervisitor.html')

@app.route('/createaccount')
def createaccount():
    return render_template('createaccount.html') #yeni bir kullanıcı hesabı oluştur

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Kullanıcıların şifrelerini kurtarmalarına olanak sağlayan "Şifremi Unuttum" sayfasına giden yol.

@app.route("/forgot-password", methods=["GET", "POST"]) 
def forgot_password():
    if request.method == "POST":
        email = request.form.get("email")
        # Burada kurtarma bağlantısını gönderme mantığını uygularsınız
        flash("Şifre sıfırlama bağlantısı e-postanıza gönderildi!", "success")
        return redirect(url_for("login"))
    return render_template("forgot-password.html")

# Uygulamayı çalıştırma
if __name__ == '__main__':
    app.run(debug=True)
