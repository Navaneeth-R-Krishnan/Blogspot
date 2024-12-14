from crewai import Agent
from tools import yt_tool
from dotenv import load_dotenv

load_dotenv()

# 2 Agents will be used, a content reseacher and a content writer 

# A senior blog content researcher agent
blog_researcher =Agent(
    role='Blog Researcher from Youtube Videos',
    goal='get the relevant video transcription for the topic {topic} from the provided Yt channel',
    verboe=True,
    memory=True,
    backstory=(
       "Expert in understanding videos in Engineering, STEM and providing suggestion" 
    ),
    tools=[yt_tool],
    allow_delegation=True
)

# A senior blog content writer agent
blog_writer = Agent(
    role = 'Blog Writer',
    goal="Narrate compelling tech stories about the video {topic} from YT video",
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    tools=[yt_tool],
    allow_delegation=False

)

