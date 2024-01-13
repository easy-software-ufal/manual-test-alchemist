from spacy import displacy
import spacy

text = """Allow the machine to reboot, select the first option at the grub menu"""
nlp = spacy.load("en_core_web_lg")
doc = nlp(text)
displacy.serve(doc, options={'compact':True})