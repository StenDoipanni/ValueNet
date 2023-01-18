


import rdflib
import json
import os
import csv


sentilodic = '/Users/sdg/Desktop/SPICE/ValueReasoner/sentilo_trigs/out4_def_sentilo.json'
bedic = '/Users/sdg/Desktop/SPICE/Emotions/BE/BE_emotion_dictionary.json'
path = '/Users/sdg/Desktop/SPICE/experiments/MFRC/MFRC_fulll'


out2 = open('/Users/sdg/Desktop/SPICE/experiments/MFRC/MFRC_fulll/inferences/is_v_emo_overlaps.tsv', 'w')
writer = csv.writer(out2, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
writer.writerow(['id', 'is_v_emo', 'imgsch', 'v', 'emo', 'txt'])





### ----------- isaac:CONTACT some MFT, BHV, or Folk value ----------




# occurrences of Contact of any MFT, BHV or Folk value

def is_v_emo_overlaps(inputGraph):
    newg = rdflib.Graph()
    ourg = newg.parse(inputGraph, format='ttl')
    querystring = '''
                PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                PREFIX owl: <http://www.w3.org/2002/07/owl#>
                PREFIX role: <http://www.ontologydesignpatterns.org/ont/vn/abox/role/>
                PREFIX emo: <http://www.ontologydesignpatterns.org/ont/emotions/EmoCore.owl#>
                PREFIX be: <http://www.ontologydesignpatterns.org/ont/emotions/BasicEmotions.owl#>
                PREFIX vcvf: <http://www.ontologydesignpatterns.org/ont/values/valuecore_with_value_frames.owl#>
                PREFIX bhv: <https://w3id.org/spice/SON/SchwartzValues#>
                PREFIX mft: <https://w3id.org/spice/SON/HaidtValues#>
                PREFIX folk: <http://www.ontologydesignpatterns.org/ont/values/FolkValues.owl#>
                PREFIX isaac: <http://www.ontologydesignpatterns.org/ont/is/isaac_vanilla.owl#>
                PREFIX isnet: <http://www.ontologydesignpatterns.org/ont/is/isnet.owl#>

                SELECT DISTINCT ?is_v_emo ?emo ?value ?txt ?is
                WHERE {
                ?g <https://w3id.org/sdg/meta#graphFor> ?txt .
                ?is_v_emo emo:triggers ?emo ; vcvf:triggers ?value ; isnet:activates ?is .
                }
                
                ''' 
    result = ourg.query(querystring)
    for res in set(result):
        #pattern = f"isaac:CONTACT --> {str(res['value']).replace('https://w3id.org/spice/SON/HaidtValues#','mft:').replace('https://w3id.org/spice/SON/SchwartzValues#','bhv:').replace('http://www.ontologydesignpatterns.org/ont/values/FolkValues.owl#','folk:')}"
        id = str(inputGraph).replace('/Users/sdg/Desktop/SPICE/experiments/MFRC/MFRC_fulll/','')
        #role = str(res['role']).replace('http://www.ontologydesignpatterns.org/ont/vn/abox/role/','role:')
        #support_trig = res['class1']
        #value_trig = res['class2']
        is_v_emo = res['is_v_emo']
        emo = str(res['emo']).replace('http://www.ontologydesignpatterns.org/ont/emotions/BasicEmotions.owl#', 'be:')
        imgsch = str(res['is']).replace('http://www.ontologydesignpatterns.org/ont/is/isaac_vanilla.owl#', 'is:')
        v = str(res['value']).replace('https://w3id.org/spice/SON/HaidtValues#','mft:').replace('https://w3id.org/spice/SON/SchwartzValues#','bhv:').replace('http://www.ontologydesignpatterns.org/ont/values/FolkValues.owl#','folk:')
        #description = (f"Contact Situation triggered by {res['class1']}, taking as {str(res['role']).replace('http://www.ontologydesignpatterns.org/ont/vn/abox/role/','role:')} the entity {res['class2']}, trigger for {str(res['value']).replace('https://w3id.org/spice/SON/HaidtValues#','mft:').replace('https://w3id.org/spice/SON/SchwartzValues#','bhv:').replace('http://www.ontologydesignpatterns.org/ont/values/FolkValues.owl#','folk:')}")
        txt = res['txt']
        #print(f"CONTACT --> {str(res['value']).replace('https://w3id.org/spice/SON/HaidtValues#','mft:').replace('https://w3id.org/spice/SON/SchwartzValues#','bhv:').replace('http://www.ontologydesignpatterns.org/ont/values/FolkValues.owl#','folk:')} : Graph {inputGraph} presents some Support Situation, triggered by {res['class1']}, towards {res['class2']}, trigger for {str(res['value']).replace('https://w3id.org/spice/SON/HaidtValues#','mft:').replace('https://w3id.org/spice/SON/SchwartzValues#','bhv:').replace('http://www.ontologydesignpatterns.org/ont/values/FolkValues.owl#','folk:')}")
        writer.writerow([id, is_v_emo, imgsch, v, emo, txt])






for filename in os.listdir(path):
    if filename.endswith('.ttl'):
        file_path = os.path.join(path, filename)
        if os.path.isfile(file_path):
            is_v_emo_overlaps(file_path)