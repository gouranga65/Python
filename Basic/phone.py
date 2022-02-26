phnum=int(input('phone'))
digit={
    "1":"one",
    '2':'two',
    '3':'three',
    '4':'four'
}
output=''
for ch in phnum:
   output+=digit.get(ch)
print(output)