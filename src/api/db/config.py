from decouple import config

Database_url = config("DATABASE_URL",default = "")
Database_timezone = config("DATABASE_TIMEZONE",default = "utc")