filepath = "C:/Users/Henrik Kiepe/Desktop/inputs.txt"

with open(filepath, 'r') as fopen:
  lines = fopen.readlines()

arr = []
for line in lines:
    text1 = line.replace('\n', '').split(';')
    text = '<xsl:if test="(((price/netto) * 0.8) > ' + text1[0] + ') and (((price/netto) * 0.8) &lt;= ' + text1[1] + \
           ')">\n'
    text = text + '\t<xsl:value-of select="format-number((price/netto) * 0.8 * ' + text1[2] + ' div 1.23' + \
           """,'#.##')"/>""" + '\n'
    text = text + '</xsl:if>'
    arr.append(text)

i = 0
with open('save.txt', 'w') as fopen:
    for line in arr:
        fopen.write(str(arr[i]) + '\n')
        i = i + 1
