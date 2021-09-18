import sys
import subprocess
import random
from datetime import datetime

def gen_number():
    n = random.randint(0,99)
    return n

def say(text):
    subprocess.call(['say', text])

def main():
    print('Deutsch Nummer TTS')
    n_total, n_correct = 0, 0
    total_time = 0
    while True:
        expected = gen_number() 
        say('{}'.format(expected))
        t0 = datetime.now()
        answered = input('Welche Nummer? ')
        t1 = datetime.now()
        if not answered.isdigit():
            print()
            break
        elif int(answered) == expected:
            n_correct += 1
            print('^__^ Richtig!')
        else:
            print('>''< Falsch! ({})'.format(expected))
        total_time += (t1-t0).total_seconds()
        n_total += 1
    print('Zusammenfassung:')
    print('  Richtigkeit: {:2.2f}%'.format(100*n_correct/n_total))
    print('  Reaktionszeit: {:.3f} sec.'.format(total_time/n_total))

if __name__ == '__main__':
    main()
