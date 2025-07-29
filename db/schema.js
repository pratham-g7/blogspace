import mongoose from "mongoose";

const blogSchema = new mongoose.Schema({
  id: String,
  name: String,
  content: String,
  createdAt: { type: Date, default: Date.now },
});

export default mongoose.model('Blog', blogSchema);
