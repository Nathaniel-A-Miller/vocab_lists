# -*- coding: utf-8 -*-

# -------------------------------
# Example: Arabic Morphological Analysis
# using CAMeL Tools
# -------------------------------

from camel_tools.morphology.database import MorphologyDB
from camel_tools.morphology.analyzer import Analyzer
from pprint import pprint  # for nice printing

# --- Step 1: Load the built-in morphological database ---
print("Loading morphology database...")
db = MorphologyDB.builtin_db()

# --- Step 2: Create an Analyzer instance ---
# In Streamlit, you can add explanations like this:
st.write("The 'backoff=\"ADD_ALL\"' option lets the analyzer return approximate analyses if no direct match is found.")
analyzer = Analyzer(db, backoff='ADD_ALL')

# --- Step 3: Analyze a single word ---
word = 'الكتاب'
analyses = analyzer.analyze(word)

print(f"\n🔍 Analyses for: {word}")
pprint(analyses[:2])  # print only first 2 analyses for clarity

# --- Step 4: Analyze multiple words ---
words = ['الكتاب', 'جميل', 'كتب', 'مدارسنا']
results = analyzer.analyze_words(words)

print("\n📚 Multiple word analyses:")
for analyzed_word in results:
    print(f"\nWord: {analyzed_word.word}")
    for analysis in analyzed_word.analyses[:2]:  # limit output
        print(f"  • Lemma: {analysis.get('lex')}")
        print(f"    POS: {analysis.get('pos')}")
        print(f"    Gloss: {analysis.get('gloss')}")
