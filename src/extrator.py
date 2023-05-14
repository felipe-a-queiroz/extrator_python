import psycopg2
import csv

# Configurações de conexão com o banco de dados
db_name = "example"
db_user = "postgres"
db_password = "123456"
db_host = "localhost"
db_port = "5432"
table_name = "pessoas"

# Conexão com o banco de dados
try:
    conn = psycopg2.connect(database=db_name, user=db_user, password=db_password, host=db_host, port=db_port)
    cursor = conn.cursor()
    print("Conexão bem-sucedida ao banco de dados!")
except psycopg2.Error as e:
    print("Erro ao conectar ao banco de dados:", e)
    exit()

# Consulta os dados da tabela
try:
    cursor.execute(f"SELECT * FROM {table_name};")
    rows = cursor.fetchall()
except psycopg2.Error as e:
    print("Erro ao executar a consulta:", e)
    cursor.close()
    conn.close()
    exit()

# Criação do arquivo CSV
csv_filename = "output.csv"
try:
    with open(csv_filename, "w", newline="") as file:
        writer = csv.writer(file)
        # Escreve o cabeçalho do arquivo CSV com os nomes das colunas
        writer.writerow([desc[0] for desc in cursor.description])
        # Escreve as linhas da tabela no arquivo CSV
        writer.writerows(rows)
    print(f"Arquivo CSV '{csv_filename}' criado com sucesso!")
except IOError as e:
    print("Erro ao criar o arquivo CSV:", e)

# Encerramento da conexão com o banco de dados
cursor.close()
conn.close()
