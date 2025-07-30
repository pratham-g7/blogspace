import requests

url = "http://localhost:3000/posts/new"  # change this if your server runs on a different URL or port

headers = {
    "Content-Type": "application/json"
}


names = ["Rahul", "Arjun", "Rohan", "Karan", "Aman", "Siddharth", "Aditya", "Varun", "Pranav", "Abhishek", "Priya", "Ananya", "Sneha", "Riya", "Aishwarya", "Isha", "Pooja", "Nisha", "Kavya", "Swati"]

posts = [
    {
        "name": "Too Quiet at 3AM",
        "content": "The world feels weirdly paused at 3AM. Streetlights flicker, fans hum louder than usual, and thoughts get heavier. It’s peaceful but kind of unnerving. Sometimes I write, sometimes I just sit there staring at the wall. Not sure if it’s insomnia or just overthinking."
    },
    {
        "name": "Train Ride Observations",
        "content": "On the metro today, a kid was singing full volume with headphones in. Completely off-beat. No one stopped him. Everyone just kind of smiled. Made me realize how rarely we see unfiltered joy in public. Wish I had that level of confidence again."
    },
    {
        "name": "Rain and Chai",
        "content": "Heavy rain, a cracked window, and overly sweet chai. No dramatic thoughts, no productivity. Just sat there watching the drops race down the glass. It’s one of those moments that feels small now but will come back to me in some random future nostalgia."
    },
    {
        "name": "Overheard at a Café",
        "content": "Some girl said, “He thought Kafka was a dessert.” Her friend laughed like she’d heard it ten times. They looked like they'd been friends since school. You can tell when people have shared silences that aren’t awkward anymore. I envy that kind of comfort."
    },
    {
        "name": "Sleep Schedule Ruined",
        "content": "I keep telling myself I’ll sleep early, but I somehow end up doom-scrolling, half-lost in Reddit threads and 3-hour video essays. The worst part is, I don’t even enjoy it. Just filling silence. Might try deleting apps again. Might not."
    },
    {
        "name": "That Awkward Hello",
        "content": "Saw someone I sort of knew from school. We both made eye contact and did that half-smile-half-nod thing. Didn’t stop to talk. I think we both knew the conversation would be too weird. Some connections are better left in the past."
    },
    {
        "name": "Old Photos Hit Different",
        "content": "Went down a photo rabbit hole. Noticed how everyone in old pics looks slightly off — like they were still becoming themselves. Even me. I don’t look sad, but I don’t look settled either. I kind of miss that version of myself."
    },
    {
        "name": "Empty Tiffin",
        "content": "Someone stole my dabba at work today. Not kidding. Left it in the pantry for 10 minutes and came back to nothing but the spoon. No note, no trace. I’m more impressed than mad. Hope they at least enjoyed the rajma."
    },
    {
        "name": "Sunday Slump",
        "content": "Woke up late, scrolled till noon, made Maggi, didn’t leave the house. It’s weird how relaxing and depressing that combo can be. I keep thinking I should do “something productive,” but then the day’s already gone. Oh well. There’s always Monday."
    },
    {
        "name": "People Watching",
        "content": "Sat at a bench today just observing people. A guy was trying to balance coffee and a phone call. A couple was arguing quietly. A kid kept trying to step only on the white tiles. Life is chaotic but weirdly patterned when you zoom out."
    },
    {
        "name": "Post-Rain Streets",
        "content": "There’s something oddly satisfying about watching the mess after heavy rain. Plastic bags clumped in puddles, scooters skidding a bit, dogs shaking off water. It’s gross, but it feels real. Like the city showed a side it normally hides."
    },
    {
        "name": "Dream I Forgot",
        "content": "Woke up remembering a dream that felt important, but within five minutes it was gone. Just a lingering feeling. Maybe about someone I haven’t spoken to in years. I hate that dreams vanish like that — like your brain redacts your own memories."
    },
    {
        "name": "The Waiter’s Smile",
        "content": "Went to a small place for lunch. The waiter seemed unusually cheerful — cracked jokes, remembered the order without writing. Felt genuine. I tipped more than usual. Not because I had to, but because it actually made my day."
    },
    {
        "name": "Tired But Not Sleepy",
        "content": "Body says crash, brain says scroll. That weird middle zone where you’re exhausted but not ready to end the day. You don’t want stimulation, but silence feels empty. I usually just lie there, eyes open, waiting for sleep to sneak up."
    },
    {
        "name": "Grocery Store Drama",
        "content": "Saw two people arguing over the last packet of brown bread like it was gold. Not yelling — just really intense passive-aggressiveness. One of them gave up and took multigrain. I think we’re all closer to snapping than we admit."
    },
    {
        "name": "Mismatched Socks",
        "content": "Wore mismatched socks all day without realizing. No one noticed. Or maybe they did and didn’t care. Either way, kind of liberating. The small stuff really doesn’t matter most days."
    },
    {
        "name": "Elevator Silence",
        "content": "Five strangers, one elevator, zero noise. It’s always the same awkward shuffle and sudden interest in phone screens. Funny how we’ve made it normal to avoid basic human interaction in small spaces."
    },
    {
        "name": "Forgot What I Was Saying",
        "content": "Started telling a story today and completely blanked halfway. Everyone just stared. I laughed it off but I’m still wondering what that story was. Maybe my brain decided it wasn’t worth sharing."
    },
    {
        "name": "The Last Biscuit",
        "content": "Had a pack of biscuits and promised myself I’d eat just two. Ended up finishing the whole thing before I even noticed. Happens more often than I care to admit. It’s not hunger. Just habit."
    },
    {
        "name": "Middle Seat Woes",
        "content": "Got stuck in the middle seat again during a flight. One guy hogged the armrest. The other snored with his head tilted my way. I just stared at the seatbelt sign, waiting for it to end. Air travel glamorized way too much."
    }
]


for post, name in zip(posts, names):
    post.update({"username": name})
    response = requests.post(url, json=post, headers=headers)
    if response.status_code == 200:
        print(f"✅ Posted: {post['name']}")
    else:
        print(f"❌ Failed: {post['name']} | Status: {response.status_code}")