

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

import sys
for filename_spectral in spectral_filenames: 
    print filename_spectral   
    tmp_spectral=json.loads(open(basedir_spectral+filename_spectral).read())     
    spectralentities_tmp=tmp_spectral['entity_labels']      
    spectralentities=set()
    for v in spectralentities_tmp:
        spectralentities.add(v['label'])    
    tmp=dict()   
    tmp['filename']=filename_spectral
    tmp['entities']=spectralentities   
    entities_in_each_spectral_file.append(tmp)
    entities_in_all_spectral_file_sum=entities_in_all_spectral_file_sum|spectralentities
    
        

print  filename_freebase
tmp_freebase=json.loads(open(basedir_freebase+filename_freebase).read())
freebaseentities_tmp=tmp_freebase['entities']
for v in freebaseentities_tmp:
    freebaseentities.add(v['label'])
tmp=dict()
tmp['filename']=filename_freebase
tmp['entities']=freebaseentities

    







for spectralentities_dict in entities_in_each_spectral_file:
    f=open('/home/meng/papershow/union/'+spectralentities_dict['filename']+'.union', 'w');
    sys.stdout = f
    union_set=spectralentities_dict['entities']&freebaseentities
    for v in union_set:
        print v 
    f.close()
    
    
        
        
        

print >>sys.stderr,'OK!'





