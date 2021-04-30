import nltk
import re

from nltk.corpus import stopwords
from natasha import (
    Segmenter,
    MorphVocab,
    
    NewsEmbedding,
    NewsMorphTagger,
    NewsSyntaxParser,
    NewsNERTagger,
    
    PER,
    NamesExtractor,
    DatesExtractor,
    MoneyExtractor,
    AddrExtractor,

    Doc
)

segmenter = Segmenter()
morph_vocab = MorphVocab()

emb = NewsEmbedding()
morph_tagger = NewsMorphTagger(emb)
syntax_parser = NewsSyntaxParser(emb)
ner_tagger = NewsNERTagger(emb)

names_extractor = NamesExtractor(morph_vocab)
dates_extractor = DatesExtractor(morph_vocab)
money_extractor = MoneyExtractor(morph_vocab)
addr_extractor = AddrExtractor(morph_vocab)

def preproccesor(data):
    def to_lower(text):
        text = text.lower()
        return text
    
    def clean_text(lower_case):
        words  = nltk.word_tokenize(lower_case)
        punctuations = ['.', ',', '/', '!', '?', ';', ':', '(',')', '[',']', '-', '_', '%']
        punctuations = re.sub(r'\W', ' ', str(lower_case))
        stop_words  = stopwords.words('russian')
        w_num = re.sub('\w*\d\w*', '', lower_case).strip()
        lower_case = re.sub(r'\s+[a-zA-Z]\s+', ' ', lower_case)
        lower_case = re.sub(r'\s+', ' ', lower_case, flags=re.I)
        lower_case = re.sub(r'^b\s+', '', lower_case)
        lower_case = re.sub(r'^b\s+', '', lower_case)
        keywords = [word for word in words if not word in stop_words  and word in punctuations and  word in w_num]
        return keywords
    
    data = str(data)
    data = to_lower(data)
    text = clean_text(data)
    sentence = ' '.join(text)
    return sentence

def ner(text):
    doc = Doc(text)
    persons = []
    loc = []
    org = []
    doc = Doc(text)
    doc.segment(segmenter)
    doc.tag_morph(morph_tagger)
    for token in doc.tokens:
         token.lemmatize(morph_vocab)
    doc.parse_syntax(syntax_parser)
    doc.tag_ner(ner_tagger)
    for span in doc.spans:
        span.normalize(morph_vocab)
    for span in doc.spans:
        if span.type == 'PER':
            persons.append(span.text)
        elif span.type == 'ORG':
            org.append(span.text)
        elif span.type == 'LOC':
            loc.append(span.text)
    return loc, org, persons