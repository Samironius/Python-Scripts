import sys, json

path_to_files, path_to_result = sys.argv[1], sys.argv[2]
data = json.load(open(path_to_files, "r"))

ss = []
for i in data["matrix"]:
    ss.append(i["number"])
IHV = ss.index(max(ss))
print(IHV)

result = {"id": data["matrix"][IHV]["id"], "number": data["matrix"][IHV]["number"],
          "committer_name": data["committer_name"], "committer_email": data["committer_email"], }

json.dump(result, open(path_to_result, "w"))

<<<<<<< HEAD
#coment for jiraaaa
=======
#coment for jira
>>>>>>> parent of b6dfb2c... TEAM-10 fix: fixed bug with git
