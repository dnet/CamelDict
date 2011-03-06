import argparse
import itertools
import os.path

def list_from_arg(a):
    ret=[]
     
    if os.path.exists(a):
        l=open(a)
        for line in l:
            ret.append(line.strip())
    else:
        ret=a.split(',')
    
    print ret

    return ret

def combine_words(w,l):
    tuples=itertools.product(w,repeat=l)
    ret=[]
    for t in tuples:
        word=''
        for x in t:
            word+=x.capitalize()
        ret.append(word)
    return ret 

def main():
    parser=argparse.ArgumentParser(description='Generate CamelCase wordlists')
    parser.add_argument('wordlists',metavar='wordlist',nargs='+', help='wordlists containing words to construct the CamelCase words from')
    parser.add_argument('--prefix', metavar='prefix_wordlist', nargs=1, help="wordlist of prefix words (always lowercase at the begining of the words)")
    parser.add_argument('--length', nargs=1, required=True, type=int)
    parser.add_argument('--postfix', nargs=1, help='postfix words')
    args = parser.parse_args()

    prefix_words=[]
    postfix_words=[]
    words=[]

    for wl in args.wordlists:
        l=open(wl)
        for line in l:
            words.append(line.strip())
    
    words_combined=combine_words(words,args.length[0])

    if args.prefix is not None:
        prefix_words=list_from_arg(args.prefix[0])

    if args.postfix is not None:
        postfix_words=list_from_arg(args.postfix[0])

    for w in words_combined:
        if len(prefix_words)>0 and len(postfix_words)>0:
            for pre in prefix_words:
                for post in postfix_words:
                    print pre+w+post
        elif len(prefix_words)>0:
            for pre in prefix_words:
                print pre+w
        elif len(postfix_words)>0:
            for post in postfix_words:
                print w+post
        else:
            print w


if __name__ == "__main__":
    main()