import crypto
import argparse

def main():
    ''' Main program for Piglatin Translator CLI Program. '''

    parser = argparse.ArgumentParser(
            description='Encrypts and decrypts')
    parser.add_argument('algo', type=str, choices=["substitution", "railfence", "playfair"],
                        help='choose to use substitution or railfence')
    parser.add_argument('mode', type=str, choices=["encrypt", "decrypt"],
                        help='choose to use encrypt or decrypt')
    parser.add_argument('key', type=str, help='key used for')
    parser.add_argument('message', type=str, help='text to encrypt or decrypt')

    args = parser.parse_args()

    if args.algo == 'substitution':
        sub = crypto.Substitution()
        if args.mode == 'encrypt':
            print(sub.encrypt(args.message))
        elif args.mode == 'decrypt':
            print(sub.decrypt(args.message))
    elif args.algo == 'railfence':
        rf = crypto.RailFence()
        if args.mode == 'encrypt':
            print(rf.encrypt(args.message))
        elif args.mode == 'decrypt':
            print(rf.decrypt(args.message)) 
    elif args.algo == 'playfair':
        rf = crypto.Playfair()
        if args.mode == 'encrypt':
            print(rf.encrypt(args.message))
        elif args.mode == 'decrypt':
            print(rf.decrypt(args.message))
    else:
        print('Error: unexpected translation mode')
    return

if __name__ == '__main__':
    main()

#key- 
#algo- sub or railfence
#message- 
#mode- encrypt or decrypt