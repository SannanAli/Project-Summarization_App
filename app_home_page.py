import streamlit as st

#Additional Packages
#TextRank Algo
#from gensim.summarization.summarizer import summarize
#from collections.abc import Mapping

#LexRank Algo
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

#EDA packages
import pandas as pd

#Data visualization

import plotly.express as px
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg') #TkAgg #backend
import seaborn as sns

#for evaluation of Summary
from rouge import Rouge

#Ftn for LexRank Summarization
#Ftn for sumy Summarization

def sumy_summarization(docx,num=2):
    parser = PlaintextParser.from_string(docx,Tokenizer('english')) #processing the text with parser
    lex_summarizer = LexRankSummarizer()
    summary = lex_summarizer(parser.document , num)
    summary_list = [str(sentence) for sentence in summary]
    result = ''.join(summary_list)
    return result

#fth foe evaluation
def Evaluate_summary(summary,reference):
    r = Rouge()
    eval_score = r.get_scores(summary,reference)
    eval_score_df = pd.DataFrame(eval_score[0])
    return eval_score_df
instructions = '1. This is instruction Number 1 \n''2. This is instruction Number 2'
def home():
    st.title('Summarize Your Text 🗐')
    st.subheader('Summarizer')
    with st.expander('Instructions'):
        st.write(instructions)
        
    raw_text = st.text_area('Enter Your Text For Summarization Here 👇🏻')

    if st.button('Summerize'):
        with st.expander('Original Text'):
            st.write(raw_text)
        
        #Layout


        c1,c2 = st.columns(2)

        with c1:
            with st.expander('LexRank Summary'):
                LexRank_Summary = sumy_summarization(raw_text)
                Docx_length = {'Original Chatacters':len(raw_text),'Summary Chatacters':len(LexRank_Summary)}
                st.write(Docx_length)
                st.write(LexRank_Summary)
                st.info('Rouge Score')
                score = Evaluate_summary(LexRank_Summary,raw_text)
                st.dataframe(score.T,use_container_width=True)

                #plotting
                score ['Metrics'] = score.index
                fig = px.bar(score,'Metrics','rouge-1')
                st.plotly_chart(fig,use_container_width=True)


        

        with c2:
            with st.expander('TextRank Summary'):
                st.write('TextRank Summary Currently Not Avaliable')
                # TextRank_Summary = summarize(raw_text)
                # st.write(TextRank_Summary)


