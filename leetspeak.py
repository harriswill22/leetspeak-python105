paragraph = "First things first, I'm the realest (realest). Drop this and let the whole world feel it (let 'em feel it). And I'm still in the Murda Bizness. I can hold you down, like I'm giving lessons in physics (right, right?)"
letters = ['a','e','i','o','s','t']
numbers = ['4','3','6','1','0','5','7']
for p in range(len(paragraph)):
    for l in range(len(letters)):
        if letters[l] == paragraph[p]:
            paragraph = paragraph.replace(paragraph[p],numbers[l])
print(paragraph)