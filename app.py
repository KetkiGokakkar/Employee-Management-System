from flask import Flask, render_template, request, redirect, url_for, flash # type: ignore

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Used for flash messages

# Temporary storage for demonstration
employees = []
evaluations = []

# Home page route
@app.route('/')
def index():
    return render_template('index.html')

# Route to display employee form
@app.route('/add_employee', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        department = request.form['department']
        job_title = request.form['job_title']

        # Save employee to in-memory list (replace with database logic in production)
        employees.append({
            'first_name': first_name,
            'last_name': last_name,
            'department': department,
            'job_title': job_title
        })

        flash('Employee added successfully!')
        return redirect(url_for('index'))

    return render_template('add_employee.html')

# Route to submit evaluations
@app.route('/submit_evaluation', methods=['GET', 'POST'])
def submit_evaluation():
    if request.method == 'POST':
        employee_id = request.form['employee_id']
        evaluation_date = request.form['evaluation_date']
        performance_rating = request.form['performance_rating']
        comments = request.form['comments']

        # Save evaluation to in-memory list (replace with database logic in production)
        evaluations.append({
            'employee_id': employee_id,
            'evaluation_date': evaluation_date,
            'performance_rating': performance_rating,
            'comments': comments
        })

        flash('Evaluation submitted successfully!')
        return redirect(url_for('index'))

    return render_template('submit_evaluation.html')

# Route to view all employees
@app.route('/view_employees')
def view_employees():
    return render_template('view_employees.html', employees=employees)

if __name__ == '__main__':
    app.run(debug=True)
