import mongoose from "mongoose";

const commentSchema = new mongoose.Schema({
  id: String,
  text: { type: String, required: true },
  author: String,
  createdAt: { type: Date, default: Date.now }
});

const blogSchema = new mongoose.Schema({
  id: String,
  author: String,
  name: String,
  content: String,
  comments: [commentSchema],
  createdAt: { type: Date, default: Date.now },
});

export default mongoose.model('Blog', blogSchema);
