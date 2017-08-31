class PakwheelsProfile:
    def __init__(self, first_name, last_name, gender, user_name, password, email, birthday, city, country):
        """
        User profile information on Pakwheels website.

         Attributes:
            name (str): Full name of the user
            email(str): Email address of user provided on website
            birthday (date): Birth date of user
            city (str): City of user
            country (str): Country of user

        """
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.user_name = user_name
        self.password = password
        self.email = email
        self.birthday = birthday
        self.city = city
        self.country = country
