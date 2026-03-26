jobs = {
    "Data Scientist": ["python", "machine learning", "sql"],
    "Web Developer": ["html", "css", "javascript", "react"],
    "Software Engineer": ["c++", "java", "python"]
}

def match_jobs(skills):
    results = {}
    suggestions = []

    for job, req in jobs.items():
        match = len(set(skills) & set(req))
        score = int((match / len(req)) * 100)
        results[job] = score

        missing = list(set(req) - set(skills))

        if missing:
            suggestions.append(f"For {job}, consider adding: {', '.join(missing)}")

    sorted_jobs = sorted(results.items(), key=lambda x: x[1], reverse=True)

    return sorted_jobs, suggestions