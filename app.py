from flask import Flask, request, redirect, url_for, render_template
import mysql.connector

app = Flask(__name__)

# Function to connect to the MySQL database
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Pass@1108",
        database="candidate_details"
    )

# Route to render the HTML form
@app.route('/')
def form():
    return render_template('/templates/form.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    # Get form data
    data = {
        'priority': request.form['priority'],
        'position_status_1': request.form['position_status_1'],
        'position_status_2': request.form['position_status_2'],
        'open_date': request.form['open_date'],
        'current_date': request.form['current_date'],
        'on_hold_date': request.form['on_hold_date'],
        'offer_drop_date': request.form['offer_drop_date'],
        'tat': request.form['tat'],
        'replacement_of': request.form['replacement_of'],
        'replacement_salary': request.form['replacement_salary'],
        'entity_header': request.form['entity_header'],
        'entity': request.form['entity'],
        'department': request.form['department'],
        'role': request.form['role'],
        'location': request.form['location'],
        'source': request.form['source'],
        'offer_date': request.form['offer_date'],
        'budget_per_role': request.form['budget_per_role'],
        'ctc_offered': request.form['ctc_offered'],
        'function_head': request.form['function_head'],
        'doj': request.form['doj'],
        'first_name': request.form['first_name'],
        'middle_name': request.form['middle_name'],
        'last_name': request.form['last_name'],
        'email_id': request.form['email_id'],
        'gender': request.form['gender'],
        'salutation': request.form['salutation'],
        'date_of_offer': request.form['date_of_offer'],
        'position_name': request.form['position_name'],
        'band': request.form['band'],
        'level': request.form['level'],
        'position_guidelines': request.form['position_guidelines'],
        'doj_offer': request.form['doj_offer'],
        'actual_doj': request.form['actual_doj'],
        'pf_available': request.form['pf_available'],
        'earning_potential': request.form['earning_potential'],
        'flexipay_year': request.form['flexipay_year'],
        'flexipay_month': request.form['flexipay_month'],
        'tctc': request.form['tctc'],
        'monthly_ctc': request.form['monthly_ctc'],
        'variable_ctc': request.form['variable_ctc'],
        'relocation_bonus': request.form['relocation_bonus'],
        'joining_bonus': request.form['joining_bonus'],
        'retention_bonus': request.form['retention_bonus'],
        'esops': request.form['esops'],
        'basic_salary_year': request.form['basic_salary_year'],
        'basic_salary_month': request.form['basic_salary_month'],
        'hra_year': request.form['hra_year'],
        'hra_month': request.form['hra_month'],
        'conveyance_allowance': request.form['conveyance_allowance'],
        'lta_year': request.form['lta_year'],
        'lta_month': request.form['lta_month'],
        'food_allowance_year': request.form['food_allowance_year'],
        'food_allowance_month': request.form['food_allowance_month'],
        'statutory_bonus': request.form['statutory_bonus'],
        'special_allowance_year': request.form['special_allowance_year'],
        'special_allowance_month': request.form['special_allowance_month'],
        'pf_employer_year': request.form['pf_employer_year'],
        'pf_employer_month': request.form['pf_employer_month'],
        'gratuity_year': request.form['gratuity_year'],
        'gratuity_month': request.form['gratuity_month'],
        'emp_contribution_year': request.form['emp_contribution_year'],
        'emp_contribution_month': request.form['emp_contribution_month'],
        'a_year': request.form['a_year'],
        'a_month': request.form['a_month'],
        'ab_year': request.form['ab_year'],
        'ab_month': request.form['ab_month'],
        'c_year': request.form['c_year'],
        'c_month': request.form['c_month'],
        'net_pay_year': request.form['net_pay_year'],
        'net_pay_month': request.form['net_pay_month'],
        'lockin_period': request.form['lockin_period'],
        'date_of_confirmation': request.form['date_of_confirmation']
    }

    # Connect to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    # Insert data into the database
    cursor.execute('''
        INSERT INTO positions (priority, position_status_1, position_status_2, open_date, current_date, on_hold_date, offer_drop_date, tat, 
                                replacement_of, replacement_salary, entity_header, entity, department, role, location, source, offer_date, 
                                budget_per_role, ctc_offered, function_head, doj, first_name, middle_name, last_name, email_id, gender, 
                                salutation, date_of_offer, position_name, band, level, position_guidelines, doj_offer, actual_doj, pf_available, 
                                earning_potential, flexipay_year, flexipay_month, tctc, monthly_ctc, variable_ctc, relocation_bonus, joining_bonus, 
                                retention_bonus, esops, basic_salary_year, basic_salary_month, hra_year, hra_month, conveyance_allowance, lta_year, 
                                lta_month, food_allowance_year, food_allowance_month, statutory_bonus, special_allowance_year, special_allowance_month, 
                                pf_employer_year, pf_employer_month, gratuity_year, gratuity_month, emp_contribution_year, emp_contribution_month, 
                                a_year, a_month, ab_year, ab_month, c_year, c_month, net_pay_year, net_pay_month, lockin_period, date_of_confirmation) 
        VALUES (%(priority)s, %(position_status_1)s, %(position_status_2)s, %(open_date)s, %(current_date)s, %(on_hold_date)s, %(offer_drop_date)s, %(tat)s, 
                %(replacement_of)s, %(replacement_salary)s, %(entity_header)s, %(entity)s, %(department)s, %(role)s, %(location)s, %(source)s, %(offer_date)s, 
                %(budget_per_role)s, %(ctc_offered)s, %(function_head)s, %(doj)s, %(first_name)s, %(middle_name)s, %(last_name)s, %(email_id)s, %(gender)s, 
                %(salutation)s, %(date_of_offer)s, %(position_name)s, %(band)s, %(level)s, %(position_guidelines)s, %(doj_offer)s, %(actual_doj)s, %(pf_available)s, 
                %(earning_potential)s, %(flexipay_year)s, %(flexipay_month)s, %(tctc)s, %(monthly_ctc)s, %(variable_ctc)s, %(relocation_bonus)s, %(joining_bonus)s, 
                %(retention_bonus)s, %(esops)s, %(basic_salary_year)s, %(basic_salary_month)s, %(hra_year)s, %(hra_month)s, %(conveyance_allowance)s, %(lta_year)s, 
                %(lta_month)s, %(food_allowance_year)s, %(food_allowance_month)s, %(statutory_bonus)s, %(special_allowance_year)s, %(special_allowance_month)s, 
                %(pf_employer_year)s, %(pf_employer_month)s, %(gratuity_year)s, %(gratuity_month)s, %(emp_contribution_year)s, %(emp_contribution_month)s, 
                %(a_year)s, %(a_month)s, %(ab_year)s, %(ab_month)s, %(c_year)s, %(c_month)s, %(net_pay_year)s, %(net_pay_month)s, %(lockin_period)s, %(date_of_confirmation)s)
    ''', data)

    conn.commit()
    conn.close()

    # Redirect to a thank you page
    return redirect(url_for('thank_you'))

# Route for thank you page
@app.route('/thank_you')
def thank_you():
    return "Thank you for submitting the form!"

if __name__ == '__main__':
    app.run(debug=True)
