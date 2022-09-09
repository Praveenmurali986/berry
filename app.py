import random
import sys
import time




MAX_LIMIT=100
MIN_LIMIT=3

class berry:
    def __init__(self,no_of_berries,multiplayer) :
        self.no_of_berries=no_of_berries
        self.multiplayer=multiplayer

    def create_berries(self):
        berries=['*' for i in range(self.no_of_berries)]
        return berries

    def set_a_berry_as_rot(self,straw_berries):
        rot_index=random.randint(0,self.no_of_berries-1)
        straw_berries[rot_index]='#'
        return straw_berries
    
    def eat_straw_berries(self,player,straw_berries):  
        while True:
            if player=='I':
                valid=random.randint(1,3)
                print(f'i have eaten {valid} berries.')
                return valid
            else:
                eaten_berries=input(f'{player} enter the no of berries you want to eat(valid no of berries you can eat is 1 , 2 or 3). ')
                if eaten_berries =='e':
                    return eaten_berries
                elif eaten_berries in ['1','2','3']:
                    valid=self.validate(straw_berries=straw_berries,eaten_berries=int(eaten_berries))
                    if valid:
                        return eaten_berries
                    else:
                        continue
                else:
                    print('enter a valid entry')
                    continue
                
    def validate(self,straw_berries,eaten_berries):
        if eaten_berries>len(straw_berries):
            print('less berry is available!')
            return False
        else:
            return True



def check_for_loss(eaten_berries,straw_berries,player):
    loss=False
    berries=straw_berries[:eaten_berries]
    if '#' in  berries:
        loss=True
    if player=='I':
        you='I am'
    else:
        you='you are'
    if loss:
        print(f'\nsorry {player} have eaten roten berry.{you} gonna die soon.')
        time.sleep(2.5)
        return loss
    else:
        return loss


def check_exit(user_input):
    if user_input=='e':
        return sys.exit()


def ask_for_no_of_berries():
    while True:
        no_of_berries=input(f'enter no of berries you want to create(max limit is {MAX_LIMIT} and min limit is {MIN_LIMIT}). ')

        if no_of_berries in [str(i) for i in range(MIN_LIMIT,MAX_LIMIT+1)] or no_of_berries == 'e':
            return no_of_berries
        else:
            print('not valid!.\nenter a valid no of berries.')
            continue


def ask_for_multiplayer():
    while True:
        multiplayer=input('enter "y" for multiplayer or "n" to play with computer. ').lower()
        if multiplayer in ['y','n','e']:
            return multiplayer
        else:
            print('not valid !.')
            continue

def hort():
    while True:
        toss=input('tossing for the first chance.head(h) or tail(t).')
        if toss in ['h','t','e']:
            return toss
        else:
            print('call a valid toss.')
            continue
def tossing(hort):
    toss=random.choice(['h','t'])
    if toss==hort:
        print('cool ,you won the toss. ')
        time.sleep(.5)
        return True
    else:
        print('bad luck for you. computer won the toss')
        time.sleep(1.5)
        return False




def main():
    print('''\nthis is a simple game where eigther play with computer or one of your friends.
you have to simply eat berries to live.
you can only eat maximum of 3 berries a time.
try not to eat roten berry unless you want to be dead.
feel free to enter "e" anytime to exit the game.\n
             ================= good luck =================\n''')
    while True:

        #asking for multiplayer or not.
        multiplayer=ask_for_multiplayer()
        check_exit(multiplayer)

        #asking for no of berries.
        no_of_berries=ask_for_no_of_berries()
        check_exit(no_of_berries)


        straw_berry=berry(no_of_berries=int(no_of_berries),multiplayer=multiplayer)
        #creating berries.
        straw_berries=straw_berry.create_berries()

        #setting a berry as rot.
        straw_berries=straw_berry.set_a_berry_as_rot(straw_berries=straw_berries)
        print('\n',['@' for i in range(len(straw_berries))],'\n')

        while True:
            if multiplayer=='y':
                #for player 1 
                p1_eaten_berries=straw_berry.eat_straw_berries(player='player 1',straw_berries=straw_berries)
                check_exit(p1_eaten_berries)
                loss=check_for_loss(eaten_berries=int(p1_eaten_berries),straw_berries=straw_berries,player='player 1')
                if loss:
                    print('\ncongrats player 2 won\n\n')
                    main()
                straw_berries=straw_berries[int(p1_eaten_berries):]
                print('\n',['@' for i in range(len(straw_berries))],'\n')


                #for player 2
                p2_eaten_berries=straw_berry.eat_straw_berries(player='player 2',straw_berries=straw_berries)
                check_exit(p2_eaten_berries)
                loss=check_for_loss(eaten_berries=int(p2_eaten_berries),straw_berries=straw_berries,player='player 2')
                if loss :
                    print('\ncongrats player 1 won\n\n')
                    main()
                straw_berries=straw_berries[int(p2_eaten_berries):]
                print('\n',['@' for i in range(len(straw_berries))],'\n')
            else:
                #head or tail
                ht=hort()
                toss=tossing(hort=ht)
                while True:
                    if not toss:
                        #for computer
                        computer_eaten_berries=straw_berry.eat_straw_berries(player='I',straw_berries=straw_berries)
                        check_exit(computer_eaten_berries)
                        loss=check_for_loss(eaten_berries=int(computer_eaten_berries),straw_berries=straw_berries,player='I')
                        if loss:
                            print('\ncongrats you won !.\n\n')
                            time.sleep(.5)
                            main()
                        straw_berries=straw_berries[int(computer_eaten_berries):]
                        print('\n',['@' for i in range(len(straw_berries))],'\n')
                        toss=True

                    if toss:
                        
                        #for player
                        player_eaten_berries=straw_berry.eat_straw_berries(player='you',straw_berries=straw_berries)
                        check_exit(player_eaten_berries)
                        loss=check_for_loss(eaten_berries=int(player_eaten_berries),straw_berries=straw_berries,player='you')
                        if loss:
                            print('\ncomputer: i won ,die human.\n\n')
                            time.sleep(.5)
                            main()
                        straw_berries=straw_berries[int(player_eaten_berries):]
                        print('\n',['@' for i in range(len(straw_berries))],'\n')
                        toss=False
                        time.sleep(1.3)


        
if __name__=='__main__':
    main()