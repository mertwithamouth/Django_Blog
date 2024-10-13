from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

# Create your views here.

posts_db=[
    {
        "slug":"suicide",
        "image": "https://thejournal.mt/wp-content/uploads/2024/03/Penser-le-suicide.jpg",
        "author":"Mert Akin",
        "date": date(2024, 10, 21),
        "title": "Suicide",
        "excerpt": "I have always wanted to kill myself since I saw my mother tried to commit suicide",
        "content": """
          I am so sick of this life. Like literal life. I am a Christian so I believe in God and positive thinking but I'm literally giving all this shit up.
I wanted to kill myself at 18 but somehow ended up at college. I graduated in 2020 so that tells you everything you need to know. I didn’t think I would make it past 18 so being here now is like what the fuck.
God isn't doing anything in my life. My positive thoughts aren't materializing. I don't even feel connection to the shit I believe in and am wishing for. My mind is literally turned off. I made muliple vision boards, read affirmations everyday, and do all the shit you're suppose to do. I can't do it anymore.
I've been praying for a job that I can start and get into and that will pay me all the money I need and more. I've been battling unemployment and under paying jobs for damn a year and some change. I am beyond that.
I am suppose to be a rich ass artist and had to take jobs at a gym wearing business casual making $15 an hour. $500 A WEEK. I FUCKING HATE IT. Haven't had a job all year. My heat is off now because I'm literally not making any money.
I HATE GOD AND ALL OF THIS POSITIVE THINKING SHIT, BECAUSE WHY IS IT NOT WORKING.
WHAT THE HELL.
I'm late on my rent this month, my parents have been supporting me but I'm tired of it. I want my own money. I want a life I love. I hate where I live even though it was my dream at one point. I might have to move back into my parents tiny disgusting home. I HATE THIS SHIT. I'm behind on so many bills.
I got a call for a job making $17-$19 but I had to pay $140 for a background check and license in a field that is not the one I set out to pursue. I DON'T HAVE $140 TO GIVE TO A JOB BEFORE I START WORKING IT. On top of that, it could take up to a month to get the license. So I'm out $140 and have to wait a month to even start working. BULLSHIT
I literally don't know what to do. What's the point of all that believing and shit if it don't work. I apply to so many jobs every day. I even made multiple resumes and shit. I literally don't know what to do.
I need money RIGHT NOW and a whole lot of it. Money that's sustainable so I can actually live and enjoy my life, go on vacations and shit. I grew up lower middle class and I hate that's it's following me in my adult life.
I HAVE NO MORE TIME TO WAIT ON ALL THE POSITIVE SHIT I WANT. I NEED IT TODAY.
I would rather kill myself then go through all these downs. I've been more down than up and I'm sick of this shit. FUCK THE WORLD. I RATHER NOT BE ON IT IF IT'S GOING TO BE THIS DEPRESSING.
I've only had one dream my whole life, be a wealthy and succesful tv and film writer, director, and producer. My whole life I've never dreamed of anything else. I started my career as a production assistant and don't even know what else to do with my life after that. I got out that role because iI hated the politics and dynamics of it and was getting severly underpaid, and since I'm a PA, nobody gives a fuck.
I've had one dream and one dream only. I don't even know what to do with my life. Even if I did move back in, I would just lay down and mope. I feel dead inside. I hate life. I'd rather it be over than feel this way.
        """

    },
    {
        "slug":"loneliness",
        "image": "https://i0.wp.com/mikefrost.net/wp-content/uploads/2020/07/154415-depressing-alone-crowds-loneliness.jpg?fit=1920%2C1200&ssl=1",
        "author":"Mert Akin",
        "date": date(2024, 7, 21),
        "title": "Loneliness",
        "excerpt": "Have ypu ever thought about being alone even in middle of full of people? I have and I feel terrible about it.",
        "content": """
       aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
        """

    },
    {
        "slug": "hate",
        "image": "https://i0.wp.com/mikefrost.net/wp-content/uploads/2020/07/154415-depressing-alone-crowds-loneliness.jpg?fit=1920%2C1200&ssl=1",
        "author": "Mert Akin",
        "date": date(2024, 1, 21),
        "title": "Hate",
        "excerpt": "I really hate myself and everything that happened in my life. ",
        "content": """
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    """

    },

    {
        "slug": "self_harm",
        "image": "https://promises.com.sg/wp-content/uploads/2016/04/self-harm.jpg",
        "author": "Mert Akin",
        "date": date(2024, 8, 25),
        "title": "Self Harm",
        "excerpt": "Sometimes I think about hurting myself because I feel like I earn it ",
        "content": """
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
"""

    },
]

def get_date(post):
    return post["date"]
def start_page(request):
    sorted_posts=sorted(posts_db,key=get_date)
    latest_posts=sorted_posts[-3:]
    return render(request,template_name='blog/start_page.html', context={'posts_db':latest_posts})


def posts(request):
    return render(request,template_name='blog/all_posts.html', context={'post_list':posts_db})





def post_detail(request,slug):
    post_text=posts_db[slug][0]
    return render(request,"blog/post_detail.html",
                      {  "text":post_text,
                                "post_name":slug})

