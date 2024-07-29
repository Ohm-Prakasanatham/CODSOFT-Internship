from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

contacts = []

@app.route('/')
def index():
    return render_template('index.html', contacts=contacts)

@app.route('/add', methods=['POST'])
def add_contact():
    name = request.form.get('name')
    phone = request.form.get('phone')
    email = request.form.get('email')
    address = request.form.get('address')
    
    contacts.append({
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    })
    
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete_contact(index):
    if 0 <= index < len(contacts):
        contacts.pop(index)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
