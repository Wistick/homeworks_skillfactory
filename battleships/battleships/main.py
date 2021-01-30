from game_logic import Game

from termcolor import colored as colour
import time


class Announce:
    @staticmethod
    def rules():
        print(colour('Welcome to battle of battleships!', 'red'))
        print('If you do not how to play this game, please, visit www.google.com')
        print()
        time.sleep(5)
        print('Joke! Rules are simple! Input coordinates like "1 1" or "3 5" To shoot the enemy board!')
        print('When all ships are destroyed - the game is over!')
        time.sleep(3)
        print()

    def menu(self):
        while True:
            try:
                choose = int(input('To start the game input --> [1]\nTo exit --> [2]\nInput: '))
            except ValueError:
                print('Wrong input!')
                continue

            if choose == 1:
                self.run()

            elif choose == 2:
                exit('Quit success!')

    def run(self):
        user_name = input('What\'s your name, Admiral? ')
        print(f'I have the honor, Admiral {user_name}')
        print('Let\'s win the battle! Place your battleships on board!')
        time.sleep(3)
        print()
        g = Game()
        num = 0
        while True:
            print('-' * 54)
            user = colour(f'Admiral {user_name} board', 'blue', attrs=['bold'])
            ai = colour('AI board', 'red', attrs=['bold'])
            print(user.center(27) + '                      ' + ai.center(27))
            pl_board = str(g.user.board).split('\n')
            co_board = str(g.ai.board).split('\n')
            result = ''
            for i in range(len(pl_board)):
                result += colour(pl_board[i], 'blue') + '      ' + colour(co_board[i], 'yellow') + '\n'
            print(result)
            print('-' * 54)
            if num % 2 == 0:
                print('-' * 54)
                print(colour(f'{user_name}\'s turn', 'blue'))
                repeat = g.user.move()
            else:
                print('-' * 54)
                print(colour('AI turn', 'red'))
                repeat = g.ai.move()

            if repeat:
                num -= 1

            if g.ai.board.count == 7:
                print('-' * 54)
                print(colour(f'{user_name} wins!', 'blue', attrs=['bold']))
                break
            if g.user.board.count == 7:
                print('-' * 54)
                print(colour('AI wins!', 'red', attrs=['bold']))
                break

        answer = input('Would you like to play one more time? Input y/N\n').lower()
        if answer == 'y':
            self.menu()
        elif answer == 'n':
            exit('Quit success!')
        while answer != 'y' or answer != 'n':
            answer = input('Input y/N to continue!').lower()
            if answer == 'y':
                self.menu()
            elif answer == 'n':
                exit('Quit success!')


if __name__ == '__main__':
    a = Announce()
    a.rules()
    a.menu()
