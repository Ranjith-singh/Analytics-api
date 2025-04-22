from decouple import config

Database_url = config("DATABASE_URL",default = "")