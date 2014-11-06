

spectral_filenames=["Act.EduInst_hierarchy-spectral_20140713-0949-0m76br6.json",
"Arch.Struct_hierarchy-spectral_20140329-1845-42iib6o.json",
"E.NP.WW_hierarchy-spectral_20140329-1845-05k6gq3.json",
"Event_hierarchy-spectral_20140329-1843-0m7igmx.json",
"Infr._hierarchy-spectral_20140329-1844-43m363w.json",
"Route_hierarchy-spectral_20140329-1844-0m7k7se.json",
"Species_hierarchy-spectral_20140329-1846-0140ukb.json",
"Tunnel_hierarchy-spectral_20140523-0533-4ldfgin.json"
]

filename_freebase='0dataset.all.entities.in.freebase.class.comma.seprated.entity.typeid.uniq.tree.lower_cotopy.json'                  

basedir_spectral='/home/meng/papershow/20141027-2229-4ftymps-hierarchy-export/'
basedir_freebase='/home/meng/papershow/'


import ujson
json=ujson

entities_in_each_spectral_file=[]
entities_in_all_spectral_file_sum=set()

freebaseentities=set()

def pullEntitiesFromChild(node):
    if len(node['children'])==0:
        node['entities_lower']=node['entities']
        return node['entities']
    else:
        entities=set()
        for c in node['children']:
            entities=entities|set(pullEntitiesFromChild(c))
        node['entities_lower']=entities
        return entities


import sys
for filename_spectral in spectral_filenames:   
    tmp_spectral=json.loads(open(basedir_spectral+filename_spectral).read())     
    pullEntitiesFromChild(tmp_spectral['root'])
    f=open('/home/meng/papershow/20141027-2229-4ftymps-hierarchy-export-lower/'+filename_spectral,'w')
    sys.stdout=f
    print json.dumps(tmp_spectral)
    f.close()
        


    




print >>sys.stderr,'OK!'





