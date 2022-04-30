from parsing import parse
code = ""
with open("test.drom") as f:
    code = f.read()

newcode = []
for line in code.split("\n"):
    if "##" in line:
        newcode.append(line[:line.find("##")])
    else:
        newcode.append(line)

newcode = "\n".join(newcode)
parsed = parse(newcode)
print(parsed.pretty())
