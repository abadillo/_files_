# conky file formater

inc = 220   # horizontal spacer
col = 7     # columns
fil = 11     # rows

texto = [["" for j in range(col)] for i in range(fil)]
color = [[0  for j in range(col)] for i in range(fil)]

j = -1      # col
i = 0       # fil
# print(texto)


f = open("Plan.txt", "r")

for line in f:
    if (len(line) > 4):

        if line[0] == '#':
            i = 0
            j += 1
            color[i][j] = 1

        else:
            i += 1

            if line[0] == "*":
                color[i][j] = 1

            elif line[0] == "!":
                color[i][j] = 2

        linealt = line.replace("#","").replace("!","").replace("*","").strip()
        texto[i][j] = linealt





out = """${font1}\\"""
var = 20

for j in range(col):
    out = out + "\n${goto " + str(var) + "}" + "${color" + str(color[0][j]) + "}" + texto[0][j] + '\\'
    var += inc

out = out + """\n\n${hr 2}${font}"""

var = 20

for i in range(1,fil):
    for j in range(col):
        out = out + "\n${goto " + str(var) + "}" + "${color" + str(color[i][j]) + "}" + texto[i][j] + '\\'
        var += inc
    out = out + "\n"
    var = 20


f.close()

fheader = open("conkyheader.txt","r")

fout = open("../conky2.conf", "w")
fout.write(fheader.read() + out + "\n]]")
fout.close()

fheader.close()

print("listo")
