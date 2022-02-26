from sys import stdin, stdout
from collections import defaultdict
import random
finput = stdin.readline
fprint = stdout.write

class Contributor:
    def __init__(self, name, skills):
        self.name = name
        self.skills = skills
        self.available = True

class Project:
    def __init__(self, name, days, score, best_before, roles):
        self.name = name
        self.days = days
        self.score = score
        self.best_before = best_before
        self.roles = roles
        self.assigned = [None] * len(roles)

n_contributors, n_projects = map(int, finput().split(" "))
contributors = []
for _ in range(n_contributors):
    name, n_skills = finput().split(" ")
    skills = defaultdict(int)
    for _ in range(int(n_skills)):
        skill_name, skill_level = finput().split(" ")
        skills[skill_name] = int(skill_level)
    new_contributor = Contributor(name, skills)
    contributors.append(new_contributor)
projects = []
for _ in range(n_projects):
    name, *params = finput().split(" ")
    days, score, best_before, n_roles = map(int, params)
    roles = []
    for _ in range(n_roles):
        skill_name, level_required = finput().split(" ")
        roles.append([skill_name, int(level_required)])
    new_project = Project(name, days, score, best_before, roles)
    projects.append(new_project)

cskills = defaultdict(list)
for contributor in contributors:
    for skill in contributor.skills:
        cskills[skill].append(contributor)

projects.sort(key=lambda p: (-p.best_before, -p.score, p.days))
for project in projects:
    assigned_contributors = []
    for i, role in enumerate(project.roles):
        for contributor in cskills[role[0]]:
            if  contributor.skills[role[0]] >= role[1] and contributor.available:
                assigned_contributors.append(contributor)
                project.assigned[i] = contributor.name
                contributor.available = False
                break
    for contributor in assigned_contributors:
        contributor.available = True
            
ans = []
for project in projects:
    assigned = project.assigned
    if all(assigned):
        ans.append(project.name + '\n' + ' '.join(assigned))
fprint(str(len(ans)) + '\n' + '\n'.join(ans))

# ----------------TEST---------------------
# print("Contributor List :", contributors)
# for contributor in contributors:
#     print("\n  Name   :", contributor.name)
#     print("  Skills :", contributor.skills)
# print("\nProjects List", projects)
# for project in projects:
#     print("\n  Name  :", project.name)
#     print("  Days  :", project.days)
#     print("  Score :", project.score)
#     print("  Best Before:", project.best_before)
#     print("  Roles :", project.roles)
# ----------------COMMENT-------------------
