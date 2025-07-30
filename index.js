import express from 'express';
import morgan from 'morgan';
import connectDB from './db/db.js';
import Blog from './db/schema.js';
const app = express();
const PORT = 3000;

app.use(morgan("dev"))
app.use(express.static("public"));
app.use(express.json());  
app.use(express.urlencoded({ extended: true }));

connectDB()

let posts = await Blog.find();

app.get("/", (req, res) => {
    res.render("index.ejs", {postList: null});
});
 
app.get("/posts", async (req, res) => {  
    const posts = await Blog.find();
    res.render("index.ejs", { postList: posts, showDel: false});
});

app.get("/about", (req, res) => {
    res.render("index.ejs", {postList: null});
});

app.post("/posts/new", async (req, res) => {
    const postId = Math.random().toString(36).substr(2, 9);
  try {
    await Blog.create({
      id: postId,
      author: req.body.username || "Anonymous",
      name: req.body.name,
      content: req.body.content
    });
    const posts = await Blog.find(); // re-fetch all
    res.render("index.ejs", { postList: posts });
  } catch (err) {
    console.error("Failed to add post:", err.message);
    res.status(500).send("Failed to create post");
  }
});


app.delete("/posts/delete/:id", async (req, res) => {
  const customId = req.params.id;

  try {
    await Blog.findOneAndDelete({ id: customId });
     
    const index = posts.findIndex(p => p.id === customId);
    if (index !== -1) {
      posts.splice(index, 1);
    }

    res.sendStatus(204);
  } catch (err) {
    console.error("Failed to delete post:", err.message);
    res.status(500).send("Deletion failed");
  }
});


app.patch("/posts/edit/:id", async (req, res) => {
    const postId = req.params.id;
    const { name, content } = req.body;

    try {
       
        const updatedPost = await Blog.findByIdAndUpdate(
            postId,
            { name, content },
            { new: true } 
        );

        if (!updatedPost) {
            return res.status(404).send("Post not found");
        }

        const index = posts.findIndex(p => p._id.toString() === postId);
        if (index !== -1) {
            posts[index] = updatedPost;
        }

        res.sendStatus(204);
    } catch (err) {
        console.error("Failed to update post:", err.message);
        res.status(500).send("Update failed");
    }
});


app.get("/posts/:id", (req, res) => {
    const postId = req.params.id;
    const post = posts.find(p => p.id === postId);
    if (post) {
        res.render("index.ejs", {postList: [post], showDel: true});
    } else {
        res.status(404).send("Post not found");
    }
});

 
app.listen(PORT, () => {
    console.log(`Server is running on: http://localhost:${PORT}/`);
}); 