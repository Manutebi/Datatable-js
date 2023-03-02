from airtable import Airtable

from flask import Flask, render_template
import pandas as pd

# Configurar la conexión a la base de datos de Airtable
base_key = 'appTsErgl1kPnkWgl'
table_name = 'Opportunities'
api_key = 'keykY5YjFxN23izT6'

airtable = Airtable(base_key, table_name, api_key)

# Obtiene los registros de Airtable
records = airtable.get_all()

# Convierte los registros a un DataFrame de Pandas
df = pd.DataFrame.from_records((r['fields'] for r in records))

# Muestra los primeros 5 registros
print(df.head())

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', data=df.to_dict('records'))

if __name__ == '__main__':
    app.run()