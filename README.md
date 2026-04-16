# Activité 2 - Docker Compose MongoDB / MySQL / FastAPI

## Présentation du projet

Ce projet a pour objectif de déployer une architecture multi-services avec Docker Compose.

L’application orchestre simultanément :

- une base de données NoSQL MongoDB ;
- une base de données SQL MySQL ;
- une interface d’administration Mongo Express ;
- une interface d’administration Adminer ;
- une API FastAPI permettant de communiquer avec les deux bases.

L’objectif principal est de mettre en place une stack hybride, résiliente, avec des services organisés, des volumes persistants, des healthchecks métier et une configuration via un fichier `.env`.

---

## Architecture du projet

```
activite2-docker-compose/
│
├── docker-compose.yml
├── .env.example
├── .gitignore
├── README.md
│
├── api/
│   ├── Dockerfile
│   ├── .dockerignore
│   ├── main.py
│   └── requirements.txt
│
├── mongo/
│   ├── Dockerfile
│   └── docker-entrypoint-initdb.d/
│       └── init.js
│
└── mysql/
    └── init.sql
```

---

## Services Docker

Le fichier `docker-compose.yml` lance 5 services :

| Service | Rôle | Port |
|--------|------|------|
| db_mongo | Base MongoDB | Interne |
| db_mysql | Base MySQL | Interne |
| admin_mongo | Mongo Express | 8081 |
| admin_mysql | Adminer | 8080 |
| api | FastAPI | 8000 |

---

## Routes API

| Route | Description |
|------|-------------|
| `/` | Accueil API |
| `/posts` | Articles MongoDB |
| `/users` | Utilisateurs MySQL |
| `/health` | État global |

---

## Technologies

- Docker
- Docker Compose
- MongoDB
- MySQL
- Mongo Express
- Adminer
- FastAPI
- Python

---

## Configuration

Créer un fichier `.env` :

```
MYSQL_ROOT_PASSWORD=rootpassword
MYSQL_DATABASE=blog_sql
MYSQL_USER=appuser
MYSQL_PASSWORD=apppassword

MONGO_INITDB_ROOT_USERNAME=admin
MONGO_INITDB_ROOT_PASSWORD=adminpassword
MONGO_DATABASE=blog_db

MONGO_EXPRESS_USER=admin
MONGO_EXPRESS_PASSWORD=admin

API_PORT=8000
```

---

## Lancement

```bash
docker compose build
docker compose up -d
```

Vérifier :

```bash
docker compose ps
```

---

## Accès

API :

http://localhost:8000

Articles MongoDB :

http://localhost:8000/posts

Utilisateurs MySQL :

http://localhost:8000/users

---

## Interfaces

Adminer (MySQL) :

http://localhost:8080

Connexion :

Serveur : db_mysql  
Utilisateur : appuser  
Mot de passe : apppassword  
Base : blog_sql  

Mongo Express :

http://localhost:8081

Connexion :

Utilisateur : admin  
Mot de passe : admin  

---

## Healthchecks

- MongoDB : vérifie la base + 5 articles  
- MySQL : vérifie la table utilisateurs  
- API : vérifie `/posts` et `/users`  

---

## Restart policy

restart: on-failure

---

## Volumes

- mongo_data  
- mysql_data  

---

## Réseau

- backend (réseau interne)

---

## Commandes utiles

docker compose ps  
docker compose logs  
docker compose down  
docker compose down -v  
docker compose up -d --build  

---

## Tests

curl http://localhost:8000/posts  
curl http://localhost:8000/users  

---

## Captures

- docker compose ps (5 services)  
- /posts (MongoDB)  
- /users (MySQL)  
- Adminer  
- Mongo Express  

---

## Auteur

Matias Bouchenoire  
B2 INFO CYBER - Conteneurisation
