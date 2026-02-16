import spacy
def find_medications_with_ner(text):
        """
        Find medications using Medical NER

        Example:
        Input: "Patient taking Aspirin and Naproxen
        Output:['Aspirin' ,'Naproxen']

        """

        #step1: loading the medical NER Model:
        nlp = spacy.load("en_ner_bc5cdr_md")

        #step2: processing the text through NER
        doc=nlp(text)

        #step3: extracting only mediactions(chemical entities)
        print("DEBUG: All entities found:")
        for entity in doc.ents:
            print(f"  - {entity.text} → {entity.label_}")
        print()
        medications = []
        for entity in doc.ents:
           if entity.label_ =="CHEMICAL":
              medications.append(entity.text)

        #step4:return the list of medications
        return medications

#testing the NER MEDICATION FINDER
test_note= """
              Patient presenting with chest pain.
              Started on Aspirin 81mg, Atorvastatin 40mg, and Metformin 1000mg.
             History of hypertension and diabetes.
           """

medications= find_medications_with_ner(test_note)
print("medications found with NER:")
print(medications)









