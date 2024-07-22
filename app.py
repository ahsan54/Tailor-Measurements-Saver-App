from flask import Flask, render_template, request,redirect, url_for

app = Flask(__name__, template_folder='D:\\DPS\\Atm+ InfoData\\tailor\\templates',
            static_folder='D:\\DPS\\Atm+ InfoData\\tailor\\static')
from customers import CustomerManager

app = Flask(__name__)
customer_manager = CustomerManager()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/insert', methods=['GET', 'POST'])
def insert():
    if request.method == 'POST':
        name = request.form['name']
        arm_size = request.form['arm_size']
        leg_size = request.form['leg_size']
        waist_size = request.form['waist_size']
        neck_size = request.form['neck_size']
        message = customer_manager.InsertValues(name, arm_size, leg_size, waist_size, neck_size)
        return render_template('insert.html', message=message)
    return render_template('insert.html')

@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        customer_name = request.form['customer_name']
        values_to_update = {
            'name': request.form.get('name', ''),
            'arm_size': request.form.get('arm_size', ''),
            'leg_size': request.form.get('leg_size', ''),
            'waist_size': request.form.get('waist_size', ''),
            'neck_size': request.form.get('neck_size', '')
        }
        values_to_update = {k: v for k, v in values_to_update.items() if v}
        message = customer_manager.UpdateValues(customer_name, values_to_update)
        return render_template('update.html', message=message)
    return render_template('update.html')

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        customer_name = request.form['customer_name']
        value_to_delete = request.form['value_to_delete']
        message = customer_manager.DeleteValues(customer_name, value_to_delete)
        return render_template('delete.html', message=message)
    return render_template('delete.html')

@app.route('/view')
def view():
    customer_info = customer_manager.Print_All_CustomerInfo()
    return render_template('view.html', customers=customer_info)

if __name__ == '__main__':
    app.run(debug=True)
