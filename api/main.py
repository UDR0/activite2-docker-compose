import os
import mysql.connector
from pymongo import MongoClient
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


def get_mongo_client():
    mongo_user = os.getenv("MONGO_INITDB_ROOT_USERNAME")
    mongo_password = os.getenv("MONGO_INITDB_ROOT_PASSWORD")
    mongo_host = os.getenv("MONGO_HOST", "db_mongo")
    mongo_port = os.getenv("MONGO_PORT", "27017")

    mongo_url = f"mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}/"
    return MongoClient(mongo_url)


def get_mysql_connection():
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "db_mysql"),
        database=os.getenv("MYSQL_DATABASE"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD")
    )


@app.get("/")
def root():
    return {"message": "API FastAPI hybride MongoDB + MySQL"}


@app.get("/posts")
def get_posts():
    try:
        client = get_mongo_client()
        db = client[os.getenv("MONGO_DATABASE", "blog_db")]
        posts = list(db.posts.find({}, {"_id": 0}))
        return posts
    except Exception as error:
        return JSONResponse(
            status_code=500,
            content={"error": str(error)}
        )


@app.get("/users")
def get_users():
    try:
        connection = get_mysql_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT id, nom, email FROM utilisateurs")
        users = cursor.fetchall()
        cursor.close()
        connection.close()
        return users
    except Exception as error:
        return JSONResponse(
            status_code=500,
            content={"error": str(error)}
        )


@app.get("/health")
def health():
    try:
        client = get_mongo_client()
        mongo_db = client[os.getenv("MONGO_DATABASE", "blog_db")]
        mongo_count = mongo_db.posts.count_documents({})

        connection = get_mysql_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM utilisateurs")
        mysql_count = cursor.fetchone()[0]
        cursor.close()
        connection.close()

        if mongo_count == 5 and mysql_count >= 1:
            return {
                "status": "OK",
                "mongo_posts": mongo_count,
                "mysql_users": mysql_count
            }

        return JSONResponse(
            status_code=500,
            content={
                "status": "ERROR",
                "mongo_posts": mongo_count,
                "mysql_users": mysql_count
            }
        )

    except Exception as error:
        return JSONResponse(
            status_code=500,
            content={
                "status": "ERROR",
                "error": str(error)
            }
        )