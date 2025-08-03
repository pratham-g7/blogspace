import requests

headers = {
    "Content-Type": "application/json"
}

posts = [
  {
    "name": "wtf is this week",
    "username": "Vishwa",
    "content": "this week was going FINE until EVERY FKIN SUBJ gave assignments ON THE SAME DAY!!! OS LAB, CN project, DBMS quiz… bro i actually can't. slept at 4am last night writing code that didn't even run 💀 sir said “run it again” like i didn't already do that 18 times. AND i forgot to submit the form for internals so now that's another email. i want peace. i want sleep. i want to drop out."
  },
  {
    "name": "why did i even come today",
    "username": "Diya",
    "content": "class started at 8am. sir didn't show up till 8:30. then he came and taught one page and left. that's it. one page. bro i woke up at 6:45 for THIS?? also forgot my ID so security gave me that look like i'm a criminal. now sitting in canteen with 40 mins left till next class.."
  },
  {
    "name": "never wearing white pants to workshop again",
    "username": "Sagar",
    "content": "who told me it was a good idea to wear white pants to WORKSHOP. there's fkin grease on my thighs, shirt, ID card… i look like i fought a car. canteen aunty laughed when she saw me. bmsce mech = no peace, only stains."
  },
  {
    "name": "i fucked up",
    "username": "Riya",
    "content": "woke up at 10, said i'll chill for 10 mins. it's 7:43pm now and i've done exactly 0% work. OS assignment is pending, CN ppt is pending, i haven't even opened the whatsapp group. and now i'm having an existential crisis over a Google Form. why do i only get productive at 1am??? sunday was supposed to be chill bro not a deadline jungle."
  }
  {
    "name": "GET ME OUT OF ECE!!!",
    "username": "Meghana",
    "content": "had back-to-back classes where nobody understood a single thing but everyone nodded like we did. sir said 'you'll get it if you revise' — REVISE WHAT BRO?? the notes look like alien script. then lab happened and my circuit smoked up. literally. now i have to redo the entire thing before next week or lose marks. i didn't sign up for this shit man i just wanted to code and vibe. why am i suffering."
  },
  {
    "name": "canteen betrayal",
    "username": "Arya",
    "content": "stood in line for 20 mins for that special paneer roll. they said 'over ho gaya'. OVER??? i could SEE it on the counter. then aunty gave the last one to some guy who just walked in and called her 'chikki'. bro i almost cried. had to eat that soggy samosa and pretend i was okay. i wasn't 😭."
  },
  {
    "name": "this lab hates me",
    "username": "Ananya",
    "content": "spent 2 hrs debugging my code just for sir to say 'it's correct but the logic is wrong'. WHAT DOES THAT EVEN MEAN. the guy next to me copied my code and got full marks. i asked a doubt and sir said 'you should've listened in class'. i was THERE. i WAS listening. i hate this place."
  }
]

comments= [
    # Post 1: "wtf is this week" — by Vishwa
    [
        {"comment": "same bro, i blinked and the whole week vanished", "username": "Aarav"},
        {"comment": "every prof thinks their subject is the only one 😩", "username": "Sneha"},
        {"comment": "sir's 'simple program' has 400 lines. help.", "username": "Yash"},
    ],

    # Post 2: "why did i even come today" — by Diya
    [
        {"comment": "got ready for an 8am class and the prof didn't even show up 💀", "username": "Ravi"},
        {"comment": "canteen is my new classroom atp", "username": "Kavya"},
        {"comment": "i once formals on lab day once. never again..", "username": "Neha"},
        {"comment": "security uncle looked at me like i was a criminal 😭", "username": "Simran"},
    ],

    # Post 3: "never wearing white pants to workshop again" — by Sagar
    [
        {"comment": "grease stains are mech student tattoos", "username": "Aryan"},
        {"comment": "bro my pants look like they did an internship in the engine", "username": "Farhan"},
    ],

    # Post 4: "i fucked up" — by Riya
    [
        {"comment": "woke up to study, ended up scrolling reels for 3 hours💀", "username": "Zoya"},
        {"comment": "just realized i did the wrong assignment lol", "username": "Priya"},
        {"comment": "google form stress is the new assignment stress", "username": "Tanya"},
    ]
    #// Post: "GET ME OUT OF ECE!!!" — by Meghana
    [
        {"comment": "bro ECE is just pain stacked on pain i swear", "username": "Nikhil"},
        {"comment": "fuck those notes i legit thought i opened the wrong pdf", "username": "Aarushi"},
        {"comment": "my circuit popped last week and sir said 'just fix it' like bro WHAT", "username": "Viraj"},
        {"comment": "nah i'm convinced this course is a social experiment", "username": "Sanya"},
        {"comment": "i didn't sign up to suffer this hard man wtf", "username": "Deepak"},
    ],

    #// Post: "canteen betrayal" — by Arya
    [
        {"comment": "don't even talk bro i once waited 30 mins and they gave the last roll to some dude who called aunty 'akka' 😭", "username": "Ritika"},
        {"comment": "that soggy samosa hits different when you're dead inside", "username": "Yuvraj"},
        {"comment": "aunty has a blacklist i swear. i'm on it.", "username": "Meera"},
        {"comment": "i almost threw hands over a paneer roll last friday da", "username": "Arjun"},
    ],

    #// Post: "this lab hates me" — by Ananya
    [
        {"comment": "he really said 'logic is wrong' like that explains anything 💀", "username": "Devika"},
        {"comment": "copied code kid got 10/10, i got fucked for asking a doubt. fuck this place", "username": "Krish"},
        {"comment": "i WAS listening bro he just talks like he's speedrunning the syllabus", "username": "Tanya"},
        {"comment": "every lab makes me wanna change my course", "username": "Rehaan"},
        {"comment": "i'm so done with these labs man i swear to god", "username": "Anjali"},
    ]

]

# from pymongo import MongoClient

# uri = "mongodb+srv://pratham-g7:Poil22769@tasklab.dqroodl.mongodb.net/blogspace?retryWrites=true&w=majority&appName=tasklab"

# db_name = "blogspace"
# collection_name = "blogs"

# client = MongoClient(uri)
# db = client[db_name]
# collection = db[collection_name]

# cursor = collection.find({}, {"id": 1, "comments.id": 1})

# post_comment_dict = {}

# for doc in cursor:
#     post_id = doc.get("id")
#     comments = doc.get("comments", [])
#     comment_ids = [comment.get("id") for comment in comments if "id" in comment]
#     if post_id:
#         post_comment_dict[post_id] = comment_ids

# client.close()


def addPosts():
  url = "http://localhost:3000/posts/new" 
  for post in posts:
      response = requests.post(url, json=post, headers=headers)
      if response.status_code == 200:
          print(f"✅ Posted: {post['name']}")
      else:
          print(f"❌ Failed: {post['name']} | Status: {response.status_code}")

def addComments():
    #ids = ["jdsgouws3", "kacahsk1f", "xhu935ew3", "uk0fulabm"]
    ids = ["z3eaqmgo4", "eykj9b4lu", "mea2z07h1"]
    for i, _id in enumerate(ids):
      url = f"http://localhost:3000/posts/{_id}/comments"
      for comment in comments[i]:
          response = requests.post(url, json=comment, headers=headers)
          if response.status_code == 200:
              print(f"✅ Comment added to post {_id}")
          else:
              print(f"❌ Failed to add comment to post {_id} | Status: {response.status_code}")


def deleteComments():
    comments = post_comment_dict

    for post_id, comment_ids in comments.items():
        for comment_id in comment_ids:
            del_url = f"http://localhost:3000/posts/{post_id}/comments/{comment_id}"
            res = requests.delete(del_url)
            if res.status_code == 200:
                print(f"🗑️ Deleted comment {comment_id} from post {post_id}")
            else:
                print(f"❌ Failed to delete comment {comment_id} | Status: {res.status_code}")
