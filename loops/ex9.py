story = ''
while True:
    line = input('>>>')
    if not line:
        break
    story += line + '\n'
    
print('the new chapter of story')
print(story)