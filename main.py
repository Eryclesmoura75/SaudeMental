from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

def get_data_from_db(db_name, table, filter_world=True):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    if filter_world:
        cursor.execute(f"SELECT * FROM {table} WHERE entity = 'World'")
    else:
        cursor.execute(f"SELECT * FROM {table}")
    rows = cursor.fetchall()
    conn.close()
    return rows

@app.route('/', methods=['GET', 'POST'])
def get_home():
    return render_template("home.html")

@app.route('/Depressao', methods=['GET', 'POST'])
def get_depressao():
    data = get_data_from_db('depressive_disorders_prevalence.db', 'depressive_disorders')
    labels = [row[0] for row in data]  
    values = [list(row[1:]) for row in data]
    return render_template("Depressao.html", data=data, labels=labels, values=values)

@app.route('/Ansiedade', methods=['GET', 'POST'])
def get_ansiedade():
    data = get_data_from_db('age_when_first_had_anxiety_depression.db', 'anxiety_depression')
    labels = [row[2] for row in data]  
    values = [list(row[3:]) for row in data]
    return render_template("Ansiedade.html", data=data, labels=labels, values=values)

@app.route('/data/ansiedade', methods=['GET'])
def get_ansiedade_data():
    data = get_data_from_db('age_when_first_had_anxiety_depression.db', 'anxiety_depression')
    formatted_data = [{'year': row[2], 'age_range_under_13': row[3], 'age_range_13_19': row[4], 'age_range_20_29': row[5], 'age_range_30_39': row[6], 'age_range_40_and_above': row[7], 'dont_know_refused': row[8]} for row in data]
    return jsonify(formatted_data)

@app.route('/Suicidio', methods=['GET', 'POST'])
def get_suicidio():
    data = get_data_from_db('death_rate_from_suicides.db', 'suicide_rate')
    labels = [row[2] for row in data]  
    values = [list(row[3:]) for row in data]
    return render_template("Suicidio.html", data=data, labels=labels, values=values)

@app.route('/data/suicidio', methods=['GET'])
def get_suicidio_data():
    data = get_data_from_db('death_rate_from_suicides.db', 'suicide_rate')
    formatted_data = [{'year': row[2], 'suicide_rate_per_100k': row[3]} for row in data]
    return jsonify(formatted_data)

@app.route('/Insonia', methods=['GET', 'POST'])
def get_insonia():
    data = get_data_from_db('Adult_Trends.db', 'adult_trends', filter_world=False)
    labels = [row[0] for row in data]  
    values = [list(row[1:]) for row in data]
    return render_template("Insonia.html", data=data, labels=labels, values=values)

@app.route('/data/insonia', methods=['GET'])
def get_insonia_data():
    data = get_data_from_db('Adult_Trends.db', 'adult_trends', filter_world=False)
    formatted_data = [{'year': row[0], 'overall': row[1], 'female': row[2], 'male': row[3]} for row in data]
    return jsonify(formatted_data)

@app.route('/Bipolar', methods=['GET', 'POST'])
def get_bipolar():
    data = get_data_from_db('bipolar_disorder_prevalence.db', 'bipolar_age')
    labels = [row[2] for row in data]  
    values = [list(row[3:]) for row in data]
    return render_template("Bipolar.html", data=data, labels=labels, values=values)

@app.route('/data/bipolar', methods=['GET'])
def get_bipolar_data():
    data = get_data_from_db('bipolar_disorder_prevalence.db', 'bipolar_age')
    formatted_data = [{'year': row[2], 'prevalence_age_10_14': row[3], 'prevalence_age_15_19': row[4], 'prevalence_age_20_24': row[5], 'prevalence_age_25_29': row[6], 'prevalence_age_30_34': row[7], 'prevalence_age_35_39': row[8], 'prevalence_age_40_44': row[9], 'prevalence_age_45_49': row[10], 'prevalence_age_50_54': row[11], 'prevalence_age_55_59': row[12], 'prevalence_age_60_64': row[13], 'prevalence_age_65_69': row[14], 'prevalence_age_70_74': row[15], 'prevalence_age_75_79': row[16], 'prevalence_age_80_plus': row[17]} for row in data]
    return jsonify(formatted_data)

@app.route('/AutoAjuda', methods=['GET', 'POST'])
def get_autoajuda():
    return render_template("AutoAjuda.html")

@app.route('/Recursos', methods=['GET', 'POST'])
def get_recursos():
    return render_template("Recursos.html")

if __name__ == '__main__':
    app.run()