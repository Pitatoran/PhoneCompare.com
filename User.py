class User():
    def __init__(self, userID, name, username, email, password, blog):
        self._userID = userID
        self._name = name
        self._username = username
        self._email = email
        self._password = password
        self._blog = blog   # List of object Blog
        # Add more translation

    @property
    def id(self):
        return self._userID

    @property
    def name(self):
        return self._name

    @property
    def username(self):
        return self._username

    @property
    def email(self):
        return self._email

    @property
    def password(self):
        return self._password

    @property
    def  blog(self):
        return self._blog
