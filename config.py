import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "27215374"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "b4495d7b9db5bb280121b4eeeb68331c")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://amandas123:vish2004@cluster0.nm4pnfh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
