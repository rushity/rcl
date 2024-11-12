from flask import Flask, render_template, request
from cl import calculate_leaves  # Import the function from cl.py

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    # Retrieve data from the form
    total_leaves = int(request.form['total_leaves'])
    leaves_per_month = int(request.form['leaves_per_month'])
    months = int(request.form['months'])

    # Collect monthly leaves from the form inputs
    monthly_leaves = [int(request.form[f'leaves_month_{i+1}']) for i in range(months)]

    # Call the function from cl.py to calculate the leave data
    leave_data = calculate_leaves(total_leaves, leaves_per_month, months, monthly_leaves)

    # Prepare data for HTML table
    table_data = [[i + 1, row[1], row[2], row[3], row[4]] for i, row in enumerate(leave_data)]

    return render_template('result.html', table_data=table_data)

if __name__ == '__main__':
    app.run(debug=True)
