import Paragraph

p = Paragraph.Paragraph(open("./texts/todd.txt", "r").read().decode("utf-8"))

for s in p.sentences:
	print s, "\n"
