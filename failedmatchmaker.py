import random

job_titles = ["Backend Developer", "Frontend Ninja", "Data Wizard", "DevOps Overlord", "ML Rockstar"]
candidate_names = ["Kohli", "Rohit", "Messi", "Ronaldo", "Hamilton", "Max"]
reasons = [
    "has 5 years of experience in searching Kaggle",
    "once googled types of SQL Joins",
    "knows Python, but only for printing Hello World",
    "claims to be 'proficient' in Excel",
    "thinks Kubernetes is a Korean dish"
]

def match_candidate():
    candidate = random.choice(candidate_names)
    job = random.choice(job_titles)
    reason = random.choice(reasons)

    print(f" Matching {candidate} to the role of {job} because {reason}.")

if __name__ == "__main__":
    print("Running Totally Accurate AI Recruiter...")
    for _ in range(3):
        match_candidate()
