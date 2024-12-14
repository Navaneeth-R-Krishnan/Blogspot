from crewai import Crew,Process
from agents import blog_researcher,blog_writer
from tasks import research_task,write_task


# Crew added with enhancements
crew = Crew(
    agents = [blog_researcher,blog_writer],
    tasks = [research_task,write_task],
    process = Process.sequential,  # Sequential is default 
    memory = True,
    cache = True,
    max_rpm = 100,
    share_crew = True
)

# Start the task execution process with feedback
result=crew.kickoff(inputs={'topic':'AI VS ML VS DL vs Data Science'})
print(result)
