import sumy
#import pandas as pd

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.summarizers.sum_basic import SumBasicSummarizer

#document1 ="""Machine learning (ML) is the scientific study of algorithms and statistical models that computer systems use to progressively improve their performance on a specific task. Machine learning algorithms build a mathematical model of sample data, known as "training data", in order to make predictions or decisions without being explicitly programmed to perform the task. Machine learning algorithms are used in the applications of email filtering, detection of network intruders, and computer vision, where it is infeasible to develop an algorithm of specific instructions for performing the task. Machine learning is closely related to computational statistics, which focuses on making predictions using computers. The study of mathematical optimization delivers methods, theory and application domains to the field of machine learning. Data mining is a field of study within machine learning, and focuses on exploratory data analysis through unsupervised learning.In its application across business problems, machine learning is also referred to as predictive analytics."""

#parser = PlaintextParser.from_string(document1,Tokenizer("english"))

file = "Input_File_For_Summarization.csv"
parser = PlaintextParser.from_file(file, Tokenizer("english"))

# Using LexRank
'''
print('Using Lex-Rank')
print('\n')
summarizer = LexRankSummarizer()
#Summarize the document with 2 sentences
summary = summarizer(parser.document, 250)
for sentence in summary:
    print(sentence)

'''

# Using Luhn
print('\n')
print('Using Luhn')
print('\n')
summarizer_1 = LuhnSummarizer()
summary_1 =summarizer_1(parser.document,250)
for sentence in summary_1:
    print(sentence)


# Using LSA
print('\n')
print('Using LSA')
print('\n')
summarizer_2 = LsaSummarizer()
summary_2 =summarizer_2(parser.document,250)
for sentence in summary_2:
    print(sentence)

# Using Text Rank
print('\n')
print('Using Text-Rank')
print('\n')
summarizer_3 = TextRankSummarizer()
summary_3 =summarizer_3(parser.document,250)
for sentence in summary_3:
    print(sentence)


# Using Sum Basic
print('\n')
print('Using Sum-Basic')
print('\n')
summarizer_4 = SumBasicSummarizer()
summary_4 =summarizer_4(parser.document,250)
for sentence in summary_4:
    print(sentence)

sentence_file=''
'''
sentence_file+="\nLex-Rank\n"
for sentence in summary:
    sentence_file+=str(sentence)
    sentence_file+="\n"
'''
sentence_file+="\nLuhn\n"
for sentence in summary_1:
    sentence_file+=str(sentence)
    sentence_file+="\n"
sentence_file+="\nLSA\n"
for sentence in summary_2:
    sentence_file+=str(sentence)
    sentence_file+="\n"
sentence_file+="\nText-Rank\n"
for sentence in summary_3:
    sentence_file+=str(sentence)
    sentence_file+="\n"
sentence_file+="\nSum-Basic\n"
for sentence in summary_4:
    sentence_file+=str(sentence)
    sentence_file+="\n"
sentence_file+="\n#######################################################\n"
    
with open("Output_Having_Luhn_LSA_Text-Rank.csv","w") as f:
    f.write(sentence_file)

##########################################  To Be Used #################################################
'''
ls=[]
for sentence in summary:
    new = (sentence)
    ls.append(new)
ls=pd.DataFrame(ls)
print(ls)
ls.to_csv("check.csv")
'''
##########################################################################################################
