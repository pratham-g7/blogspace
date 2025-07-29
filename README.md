# 📝 BlogSpace – Minimal Personal Blogging Platform

**BlogSpace** is a lightweight web app that lets users create and publish simple blog posts with live character limits — ideal for quick thoughts, journal entries, or microblogs.

---

## 🔧 Tech Stack

- **Frontend:** HTML, CSS, JavaScript + jQuery  
- **Backend:** Node.js, Express.js  
- **Database:** MongoDB + Mongoose  

---

## ✨ Features

- 📝 **Create posts** with title and body  
- 🔢 **Live character counters** with input locking  
- 📱 **Mobile-friendly** input enforcement (works with Gboard)  
- 🎨 **Clean, responsive UI** with simple layout  
- 🗃️ **Posts stored** and retrieved from MongoDB  
- 🧱 **Page-based navigation** with server-rendered views  

---

## 📁 Project Structure
<pre>
blogspace/
├── public/ # Frontend static files
│ ├── assets/
│ │ └── main_image.jpg # Page Banner
│ ├── app.js # Main frontend JS
│ └── style.css # Main stylesheet
│
├── views/ # Server-rendered EJS templates
│ └── index.ejs # Main page template
│
├── index.js # Main Express server file
</pre>

---
