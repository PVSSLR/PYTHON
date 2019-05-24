a = input("PLAYER 1:choose anyone Rock,Paper,Scissor ")
b = input("PLAYER 2:choose anyone Rock,Paper,Scissor ")
r = "Rock"
p = "Paper"
s = "Scissor"

if a==b:
    print("Draw");
else:
    if a==r and b==p:
      print('Player 1 wins');
    elif a==p and b==r:
      print('Player 2 wins');
    elif a == s and b == r:
      print('Player 2 wins');
    elif a == r and b == s:
      print('Player 1 wins');
    elif a == s and b == p:
      print('Player 1 wins');
    elif a == p and b == s:
      print('Player 2 wins');
    elif a != r or a != p or a !=s or b != r or b != p or b !=s :
        print('Please choose from the given option');



