import nltk.chunk
import nltk
from nltk.corpus import conll2000
import itertools
from nltk import pos_tag, word_tokenize

class UnigramChunker(nltk.ChunkParserI):
    def __init__(self, train_sents): 
        train_data = [[(t,c) for w,t,c in nltk.chunk.tree2conlltags(sent)]
                      for sent in train_sents]
        self.tagger = nltk.UnigramTagger(train_data) 

    def parse2(self, tokens):
        # split words and part of speech tags
        (words, tags) = zip(*tokens)
        # get IOB chunk tags
        chunks = self.tagger.tag(tags)
        # join words with chunk tags
        wtc = itertools.izip(words, chunks)
        # w = word, t = part-of-speech tag, c = chunk tag
        lines = [' '.join([w, t, c]) for (w, (t, c)) in wtc if c]
        # create tree from conll formatted chunk lines
        return nltk.chunk.conllstr2tree('\n'.join(lines))

def clean_punctuation(text):
    text = text.replace("."," .")
    text = text.replace(","," ,")
    text = text.replace("!"," !")
    text = text.replace(":"," :")
    text = text.replace("\""," \"")
    return text

def run(q_id):
    train_sents = conll2000.chunked_sents('train.txt')
    unigram_chunker = UnigramChunker(train_sents)

    import init
    #get document here and tag; put into this format:
    #tagged = [("the", "DT"), ("little", "JJ"), ("yellow", "JJ"),("dog", "NN"), ("barked", "VBD"), ("at", "IN"),  ("the", "DT"), ("cat", "NN"),(".", ".")]
    topdoc = init.get_corpus(q_id)
    doc_nums = topdoc.keys()
    answers= [];
    for key in doc_nums:
        doc_text = topdoc[key]
        docnum= key
        #print docnum
        doc_text = clean_punctuation(doc_text)
        #print doc_text
        doc_text= doc_text.split()
        tagged=pos_tag(doc_text)

    
        chunked=unigram_chunker.parse2(tagged)
        flatten= chunked.pos()
        #print flatten
        numbered= enumerate(flatten)
        currentTag=''
        words=[]
        for i,v in numbered:
            #print i,v
            ((word,tag),phrasetag)=v
            if currentTag=='':
                currentTag=phrasetag
            if currentTag==phrasetag:
                words.append(word)
            else:
                answers.append((' '.join(words),docnum,i-len(words),currentTag,q_id))
                currentTag= phrasetag
                words= [word]
        answers.append((' '.join(words),docnum,i-len(words),currentTag,q_id))
        #print answers
          
    return answers


if __name__=="__main__":
    print run(213)
    
