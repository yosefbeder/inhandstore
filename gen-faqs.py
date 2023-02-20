import marko

file = open("faqs.md", encoding="utf8")
questions = []
n = 0

for node in marko.parse(file.read()).children:
    if isinstance(node, marko.block.Heading):
        questions.append([node.children[0]])
        n += 1
    elif not isinstance(node, marko.block.BlankLine):
        questions[n-1].append(node)

for question in questions:
    print("<details class=\"faqs__question-box\">")
    print("<summary class=\"faqs__question\">")
    print(marko.render(question[0]))
    print("</summary>")
    if len(question) > 1:
        for i in range(1, len(question)):
            print(marko.render(question[i]))
    print("</details>")
