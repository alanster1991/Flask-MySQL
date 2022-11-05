from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_All(cls):
        query = """
            SELECT * FROM dojos;
        """
        
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        dojos = []
        for result in results:
            dojos.append(cls(result))
        return dojos

    @classmethod
    def save(cls, data):
        query = """
            INSERT INTO dojos (name) VALUES(%(name)s);
        """
        dojo = connectToMySQL('dojos_and_ninjas').query_db(query, data)

        return dojo
    
    @classmethod
    def get_dojo_with_ninjas(cls, data):
        query = """
            SELECT * FROM dojos JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;
        """
        results = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        dojo = cls(results[0])
        print(f"Printing here for test {dojo}")
        for row_from_db in results:
            ninja_data = {
                'id': row_from_db['ninjas.id'],
                'first_name' : row_from_db['first_name'],
                'last_name' : row_from_db['last_name'],
                'age' : row_from_db['age'],
                'dojo_id' : row_from_db['dojo_id'],
                'created_at' : row_from_db['created_at'],
                'updated_at' : row_from_db['updated_at']

            }
            dojo.ninjas.append(ninja.Ninja(ninja_data))

        return dojo

