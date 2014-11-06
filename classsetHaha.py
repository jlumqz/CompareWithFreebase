

import ujson
json=ujson
spectral_filenames=[
"Act.EduInst_hierarchy-spectral_20140713-0949-0m76br6.json",
"Arch.Struct_hierarchy-spectral_20140329-1845-42iib6o.json",
"E.NP.WW_hierarchy-spectral_20140329-1845-05k6gq3.json",
"Event_hierarchy-spectral_20140329-1843-0m7igmx.json",
"Infr._hierarchy-spectral_20140329-1844-43m363w.json",
"Route_hierarchy-spectral_20140329-1844-0m7k7se.json",
"Species_hierarchy-spectral_20140329-1846-0140ukb.json",
"Tunnel_hierarchy-spectral_20140523-0533-4ldfgin.json"
]



basedir_newid_spectral='/home/meng/papershow/20141027-2229-4ftymps-hierarchy-export-lower-newid/'

basedir_freebase_newid_foreach='/home/meng/papershow/freebase_newid_foreach/'

def outputclassset(node,fout):
    for v in node['new_entities_id']:
        print >>fout,v,
    if len(node['new_entities_id'])!=0:
        print >>fout,','
    for c in node['children']:
        outputclassset(c,fout)

for filename in spectral_filenames:
    print filename
    spectral_json=json.loads(open(basedir_newid_spectral+filename).read())
    fout=open(basedir_newid_spectral+filename+'.classset','w')
    outputclassset(spectral_json['root'],fout)
    fout.close()
    
    freebase_json=json.loads(open(basedir_freebase_newid_foreach+filename).read())
    fout=open(basedir_freebase_newid_foreach+filename+'.classset','w')
    outputclassset(freebase_json['root'],fout)
    fout.close()


print 'Over'








