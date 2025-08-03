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
]



def addPosts():
  url = "http://localhost:3000/posts/new" 
  for post in posts:
      response = requests.post(url, json=post, headers=headers)
      if response.status_code == 200:
          print(f"✅ Posted: {post['name']}")
      else:
          print(f"❌ Failed: {post['name']} | Status: {response.status_code}")

def addComments():
    ids = ["4g6t5vicz", "kacahsk1f", "xhu935ew3", "uk0fulabm"]
    for i, _id in enumerate(ids):
      url = f"http://localhost:3000/posts/{_id}/comments"
      for comment in comments[i]:
          response = requests.post(url, json=comment, headers=headers)
          if response.status_code == 200:
              print(f"✅ Comment added to post {_id}")
          else:
              print(f"❌ Failed to add comment to post {_id} | Status: {response.status_code}")


def deleteComments():
    comments = {
    "kcn2160j0": ["golumzt95", "dmh2nrei8", "hrqhefu4l"],
    "4g6t5vicz": ["pob3kmdx1", "03q92uoik", "mi65v8b8w"],
    "kacahsk1f": ["hoqo458sb", "xlzy4n3oz", "66eqg2uot", "54n4h08lq"],
    "xhu935ew3": ["o5gl8s0q9", "j1lw6gvtc"],
    "uk0fulabm": ["hcshcd70j", "p5jrj0owy", "ld4ebkjue"]
}


    for post_id, comment_ids in comments.items():
        for comment_id in comment_ids:
            del_url = f"http://localhost:3000/posts/{post_id}/comments/{comment_id}"
            res = requests.delete(del_url)
            if res.status_code == 200:
                print(f"🗑️ Deleted comment {comment_id} from post {post_id}")
            else:
                print(f"❌ Failed to delete comment {comment_id} | Status: {res.status_code}")

