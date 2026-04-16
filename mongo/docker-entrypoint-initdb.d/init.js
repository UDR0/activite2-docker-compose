db = db.getSiblingDB("blog_db");

db.createCollection("posts", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["title", "content"],
      properties: {
        title: {
          bsonType: "string",
          description: "Le titre est obligatoire"
        },
        content: {
          bsonType: "string",
          description: "Le contenu est obligatoire"
        }
      }
    }
  }
});

db.posts.insertMany([
  { title: "Article 1", content: "Contenu du premier article" },
  { title: "Article 2", content: "Contenu du deuxième article" },
  { title: "Article 3", content: "Contenu du troisième article" },
  { title: "Article 4", content: "Contenu du quatrième article" },
  { title: "Article 5", content: "Contenu du cinquième article" }
]);