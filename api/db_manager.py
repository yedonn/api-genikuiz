from api.db import r, conn

def create_record(table, data):
    """
    Crée un enregistrement dans la table spécifiée avec les données fournies.
    """
    return r.table(table).insert(data).run(conn)

def update_record(table, record_id, data):
    """
    Met à jour un enregistrement dans la table spécifiée en utilisant l'ID de l'enregistrement et les données fournies.
    """
    return r.table(table).get(record_id).update(data).run(conn)

def delete_record(table, filters):
    """
    Supprime les enregistrements qui correspondent aux filtres fournis dans la table spécifiée.
    """
    return r.table(table).filter(filters).delete().run(conn)

def list_records(table):
    """
    Renvoie tous les enregistrements de la table spécifiée.
    """
    return list(r.table(table).run(conn))

def list_filter_records(table, filters):
    """
    Renvoie les enregistrements filtrés de la table spécifiée en utilisant les filtres fournis.
    """
    return list(r.table(table).filter(filters).run(conn))
