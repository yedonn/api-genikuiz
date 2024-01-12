from rethinkdb import RethinkDB
from rethinkdb.errors import ReqlOpFailedError


from api.settings import Envs

# Connexion à la base de données RethinkDB
r = RethinkDB()
# r.("asyncio")

# Configurer la connexion à RethinkDB
conn = r.connect(
    host=Envs.DB_HOST,
    port=Envs.DB_PORT,
    db=Envs.DB_NAME,
)
# Vérifier et créer la base de données si elle n'existe pas
try:
    r.db_create(Envs.DB_NAME).run(conn)
    print(f"Database '{Envs.DB_NAME}' created successfully.")
except ReqlOpFailedError:
    print(f"Database '{Envs.DB_NAME}' already exists.")

# Sélectionner la base de données
conn.use(Envs.DB_NAME)

# Vérifier et créer les tables si elles n'existent pas
tables_to_create = ["moderator", "party_action", 'party', 'player']  # Ajoutez les noms de vos tables
for table in tables_to_create:
    try:
        r.table_create(table).run(conn)
        print(f"Table '{table}' created successfully.")
    except ReqlOpFailedError:
        print(f"Table '{table}' already exists.")