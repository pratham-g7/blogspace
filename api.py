import requests

url = "http://localhost:3000/posts/new"  # change this if your server runs on a different URL or port

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
    "content": "class started at 8am. sir didn't show up till 8:30. then he came and taught one page and left. that’s it. one page. bro i woke up at 6:45 for THIS?? also forgot my ID so security gave me that look like i'm a criminal. now sitting in canteen with 40 mins left till next class.."
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



for post in posts:
    response = requests.post(url, json=post, headers=headers)
    if response.status_code == 200:
        print(f"✅ Posted: {post['name']}")
    else:
        print(f"❌ Failed: {post['name']} | Status: {response.status_code}")