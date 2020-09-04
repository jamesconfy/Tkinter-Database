import sqlite3
class DB:
    def __init__(self):
        self.conn = sqlite3.connect("./personal_information.db")
        self.db = self.conn.cursor()
        self.db.execute("""CREATE TABLE IF NOT EXISTS personal_info(
            id INTEGER PRIMARY KEY NOT NULL,
            first_name text,
            last_name text,
            dob text,
            address text,
            city text,
            state text,
            phone_number text
        )""")

    def CreateProfile(self, first_name, last_name, dob, address, city, state, phone_number):
        self.db.execute("INSERT INTO personal_info VALUES(:id, :first_name, :last_name, :dob, :address, :city, :state, :phone_number)", {
            'id': None,
            'first_name': first_name,
            'last_name': last_name,
            'dob': dob,
            'address': address,
            'city': city,
            'state': state,
            'phone_number': phone_number
        })
        self.conn.commit()
        
    # def Insert(self):
    #     self.db.execute("INSERT INTO personal_info VALUES(:id, :first_name, :last_name, :dob, :address, :city, :state, :phone_number)", {
    #         'id': None,
    #         'first_name': 'Rand',
    #         'last_name': 'LastName',
    #         'dob': "Another One",
    #         'address': "random address",
    #         'city': "random city",
    #         'state': "random state",
    #         'phone_number': "random2"
    #     })
    #     self.conn.commit()

    def DeleteProfileByID(self, yid):
        self.db.execute("DELETE FROM personal_info WHERE id = (?)", (yid,))
        self.conn.commit()

    def Update(self, set_update, yid, set_value):
        self.db.execute("UPDATE personal_info SET " +set_update+" = (?) WHERE id = (?)", (set_value, yid))
        self.conn.commit()

    def UpdateAll(self, yid, first_name2, last_name2, dob2, address2, city2, state2, phone_no2):
        self.db.execute("UPDATE personal_info SET first_name = (?), last_name = (?), dob = (?), address = (?), city = (?), state = (?), phone_number = (?) WHERE id = (?)", (first_name2, last_name2, dob2, address2, city2, state2, phone_no2, yid))
        self.conn.commit()

    def DeleteProfileByName(self, first_name1, last_name1):
        self.db.execute("DELETE FROM personal_info WHERE first_name = (?) last_name = (?)", (first_name1, last_name1,))
        self.conn.commit()

    def GetAll(self):
        self.db.execute("SELECT * FROM personal_info")
        return self.db.fetchall()

    def Close(self):
        self.conn.close()