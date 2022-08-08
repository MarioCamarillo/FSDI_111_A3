from app.database import get_db

def output_formatter(results):
    out = []
    for result in results:
        user = {
            "id": result[0],
            "first_name":result[1],
            "last_name": result[2],
            "hobbies": result[4],
            "vehicle": result[4],
            "active": result[5]
        }
        out.append(user)

    return out


def scan():
    cursor = get_db().execute(
        "SELECT * FROM user WHERE active=1", ()
    )

    results = cursor.fetchall()
    cursor.close()

    return output_formatter(results)


def select_by_id(pk):
    cursor = get_db().execute(
        "SELECT * FROM user WHERE id=? AND active=1",
        (pk, )
    )

    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)


def insert(user_dict):
    value_tuple = (
        user_dict.get("first_name"),
        user_dict.get("last_name"),
        user_dict.get("hobbies"),
        user_dict.get("vehicle")
    )
    statement = """
            INSERT INTO user (
                first_name,
                last_name,
                hobbies,
                vehicle
            ) VALUES (?, ?, ?, ?)
    """

    cursor=get_db()
    cursor.execute(statement, value_tuple)
    cursor.commit()
    cursor.close


def update(pk, user_data):
    value_tuple = (
        user_data.get("first_name"),
        user_data.get("last_name"),
        user_data.get("hobbies"),
        user_data.get("vehicle"),
        pk
    )
    statement = """
        UPDATE user
        SET first_name=?,
        last_name = ?,
        hobbies = ?,
        vehicle = ?,
        WHERE id=?
    """
    cursor=get_db()
    cursor.execute(statement, value_tuple)
    cursor.commit()
    cursor.close()


def deactivate(pk):
    cursor = get_db()
    cursor.execute("UPDATE user SET active=0 WHERE id=?", (pk, ))
    cursor.commit()
    cursor.close()

