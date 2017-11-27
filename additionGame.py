import datetime
import random
again = True
while again:
    fn = "additiongame" + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
    right = 0
    wrong = 0
    problems = []
    print "Please enter how many questions you would like to answer."
    try:
        questions = raw_input()    
    except SyntaxError:
        print "Please enter how many questions you would like to answer."
    except ValueError:
        print "Please enter how many questions you would like to answer."
    for count in range(int(questions)):
        answer = None
        x = random.randint(0,12)
        y = random.randint(0,12)
        print '{:>2}'.format(x), "+", '{:>2}'.format(y), "=",
        while not answer:
            try:
                answer = int(raw_input())
            except SyntaxError:
                print "Please type an answer"
                print '{:>2}'.format(x), "+", '{:>2}'.format(y), "=",
            except ValueError:
                print "Please type an answer"
                print '{:>2}'.format(x), "+", '{:>2}'.format(y), "=",
        if answer == x + y:
            print "Good job!"
            right += 1
            problems.append('{:>2}'.format(x) + "+" + '{:>2}'.format(y) + " = " + '{:>2}'.format(answer))
        else:
            print "Better luck next time."
            wrong += 1
            problems.append('{:>2}'.format(x) + "+" + '{:>2}'.format(y) + " = " + '{:>2}'.format(answer) + " X")
    f = open(fn, "w")
    for p in problems:
        print p
        f.write(p + "\n")
    f.write("Right answers: " + str(right) + " Wrong answers: " + str(wrong) + "\n")
    f.close()
    print "Right answers:", right, "Wrong answers:", wrong
    replay = raw_input("Play again? [Y/n] ")
    if replay == "N" or replay == "n":
        again = False
