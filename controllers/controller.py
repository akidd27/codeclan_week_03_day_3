from flask import render_template
from app import app
from models.orders import orders

@app.route('/orders')
def all_orders():
    return render_template('orders.html', title='Orders', orders=orders)

@app.route('/orders/<index>')
def individual_order_by_index(index):
    order_index = int(index)
    return render_template('order.html', title= f'Order {order_index}', order=orders[order_index])