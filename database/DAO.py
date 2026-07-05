from database.DB_connect import DBConnect
from model.object import Object


class DAO():

    @staticmethod
    def getAllNodes():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
                    from objects o"""

        cursor.execute(query)

        for row in cursor:
            result.append(Object(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllEdges():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select eo1.object_id as id1, eo2.object_id as id2, count(*) as peso
                    from exhibition_objects eo1, exhibition_objects eo2
                    where eo1.exhibition_id = eo2.exhibition_id
                    and eo1.object_id < eo2.object_id
                    group by eo1.object_id, eo2.object_id"""

        cursor.execute(query)

        for row in cursor:
            result.append(row)

        cursor.close()
        conn.close()
        return result
