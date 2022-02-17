from random import choice, seed

# seed(1)

word_length = 5
max_try_num = 5

# https://github.com/jnoodle/English-Vocabulary-Word-List/blob/master/Oxford%205000.txt
with open("Oxford5000.txt") as f:
    wordlist = [l.strip() for l in f.readlines() if len(l)-1==word_length]

answer =choice(wordlist)
print(wordlist)

def get_result(guess, answer):
    answer = list(answer)
    r = []
    #(ex)ans:["g", "i", "v", "e", "n"] guess:eiive -> ans:["g", "", "v", "e", "n"]  r:⬜🟩⬜⬜⬜ 
    for i in range(len(guess)):
        if guess[i]==answer[i]:
            r.append("🟩")
            answer[i]="" # delete used letter
        else:
            r.append("⬜")
    #(ex)ans:["g", "i", "v", "e", "n"]  r:⬜🟩⬜⬜⬜ guess:eiive -> r:🟨🟩⬜🟨⬜ 
    for i in range(len(guess)):
        if guess[i] in answer:
            r[i] = "🟨"
            answer[answer.index(guess[i])]=""
    return "".join(r)


i = 1
while(True):
    guess = input("Try #{}: ".format(i))
    if len(guess)!=word_length:
        print("Input should be {} letters.".format(word_length))
        continue
    elif guess not in wordlist:
        print("Input is not a meaningful word.")
        continue
    result = get_result(guess, answer)
    print(result)
    if result=="🟩"*word_length:
        print("Congratulations! The answer is {}.".format(answer))
        break
    elif i > max_try_num:
        print("Game over! The answer is {}".format(answer))
        break
    else:
        i +=1
    
