from courses import COURSES, TECH_DEGREES

def is_eligible(degree: str) -> bool:
    return degree.lower() in TECH_DEGREES

def get_recommendations(degree: str, skills: str) -> list:
    student_skills = [s.strip().lower() for s in skills.split(",") if s.strip()]
    degree = degree.lower()

    recommendations = []
    for course in COURSES:
        if degree in course["degrees"] and any(skill in course["skills"] for skill in student_skills):
            recommendations.append(f"{course['title']} — ⏳ Duration: {course['duration']}")

    # Ensure at least 2 courses are returned
    if len(recommendations) < 2:
        fallback = [f"{c['title']} — ⏳ Duration: {c['duration']}" for c in COURSES if degree in c["degrees"]]
        recommendations.extend(fallback)

    return recommendations[:10]
