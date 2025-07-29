import express from 'express';
import morgan from 'morgan';

const app = express();
const PORT = 3000;

app.use(morgan("dev"))
app.use(express.static("public"));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

let posts = [] 

app.get("/", (req, res) => {
    res.render("index.ejs", {postList: null});
});
 
app.get("/posts", (req, res) => {
    res.render("index.ejs", {postList: posts});
}); 

app.get("/about", (req, res) => {
    res.render("index.ejs", {postList: null});
});

app.post("/posts/new", (req, res) => {  
    const postId = Math.random().toString(36).substr(2, 9);
    posts.push({id: postId, name: req.body.name, content: req.body.content});
    res.render("index.ejs", {postList: posts});
});

app.delete("/posts/delete/:id", (req, res) => {
    const postId = req.params.id;
    const index = posts.findIndex(p => p.id === postId)
    if (index !== -1) {
        posts.splice(index, 1);
    }
    res.sendStatus(204);
});   

app.patch("/posts/edit/:id", (req, res) => {
    const postId = req.params.id;
    const { name, content } = req.body;
    const post = posts.find(p => p.id === postId)
    if (post) {
        post.name = name;
        post.content = content;
    }
    res.sendStatus(204);
});

app.get("/posts/:id", (req, res) => {
    const postId = req.params.id;
    const post = posts.find(p => p.id === postId);
    if (post) {
        res.render("index.ejs", {postList: [post]});
    } else {
        res.status(404).send("Post not found");
    }
});
 
app.listen(PORT, () => {
    console.log(`Server is running on: http://localhost:${PORT}/`);
}); 