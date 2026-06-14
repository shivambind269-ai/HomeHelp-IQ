def retrieve_knowledge(issue):

    try:
        with open(
            "data/knowledge_base.txt",
            "r",
            encoding="utf-8"
        ) as file:

            data = file.read()

        issue = issue.lower()

        if issue == "air conditioner":
            start = data.find("AIR CONDITIONER")
            end = data.find("PLUMBING")
            return data[start:end]

        elif issue == "plumbing":
            start = data.find("PLUMBING")
            end = data.find("ELECTRICAL")
            return data[start:end]

        elif issue == "electrical":
            start = data.find("ELECTRICAL")
            return data[start:]

        return "No specific knowledge found."

    except Exception as e:
        return str(e)