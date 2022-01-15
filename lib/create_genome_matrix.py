from installed_clients.WorkspaceClient import Workspace
import pandas as pd
from collections import Counter
class MatrixUtils:
    def __init__(self, config):
        self.ws_url = config['workspace-url']
        self.wsc = Workspace(self.ws_url)
    def get_genomes_in_genomeset(self,genomeset_ref):
           genome_elements = self.wsc.get_object_subset([{
           'included': ['/elements'],
            'ref': genomeset_ref
            }])[0]['data']['elements']
           genomes = genome_elements.keys()
           return list(genomes)
    
    def get_cds_functions(self, genome_ref):
        all_functions=list()
        cds_functions= self.wsc.get_object_subset([{
           'included': ["features/[*]/functions"],
            'ref': genome_ref
            }])[0]['data']['features']
        for fn in cds_functions:
            all_functions.append(list(fn.values()))
        glist =  sum(all_functions,[])
        return Counter(sum(glist,[]))
    def concatenate_df (self, df1,df2):
        #df = pd.merge(df1, df2, left_index=True, right_index=True)a
        df = df1.join (df2)
        return (df)
    
if __name__ == "__main__":
    df = pd.DataFrame()
    config=dict()
    config['workspace-url'] = "https://appdev.kbase.us/services/ws"
    matrix = MatrixUtils(config)
    genomeset_ref = "63151/537/2"
    m = matrix.get_genomes_in_genomeset(genomeset_ref)
    i = 0
    for genome_ref in m:
        i = i +1
       # if (i==4):
       #     break
    #genome_ref = "63151/536/2"
        print (genome_ref)
        fn = matrix.get_cds_functions(genome_ref)
   # print (fn)
        df1 = pd.DataFrame.from_dict(fn, orient="index", columns=[genome_ref])
        df = df1.join (df).fillna(0).astype(int)
    df.to_csv("genome_functions.tsv", sep="\t")