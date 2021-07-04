import psycopg2
import os


def get_con():
    con = psycopg2.connect(
        host='localhost',
        port=5432,
        database='postgres',
        user='postgres',
        password=os.environ.get("db_password")
    )
    return con


def get_con_cur():
    con = get_con()
    return con, con.cursor()


def get_dp(**kwargs):
    try:
        con, cur = get_con_cur()
        cur.execute(kwargs['sql'])
        rows = cur.fetchall()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()
            return rows


def change_db(**kwargs):
    try:
        con, cur = get_con_cur()
        cur.execute(kwargs['sql'], (kwargs['name'], kwargs['phone']))
        con.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()


def delete_contact_db(**kwargs):
    sql = """DELETE FROM contacts WHERE name = (%s) and phone = (%s);"""
    kwargs['sql'] = sql
    change_db(name=kwargs['name'], phone=kwargs['phone'], sql=kwargs['sql'])


def get_all_contact():
    sql = """SELECT name,phone FROM contacts;"""
    return get_dp(sql=sql)


def create_contact_db(**kwargs):
    sql = """INSERT INTO contacts(name,phone)
                 VALUES(%s,%s);"""
    kwargs['sql'] = sql
    change_db(name=kwargs['name'], phone=kwargs['phone'], sql=kwargs['sql'])


def search_contact_db(**kwargs):
    sql = f"""SELECT name,phone FROM contacts WHERE name LIKE '%{kwargs['arg']}%' OR phone LIKE '%{kwargs['arg']}%';"""
    return get_dp(sql=sql)
