

import ujson
json=ujson
spectral_filenames=[

"Act.EduInst_hierarchy-entity-cobweb-partitioning_decreasing_20140624-0705-4ldfadv.json",
"Act.EduInst_hierarchy-entity-cobweb-partitioning_increasing_20140624-0705-3z6b8kn.json",
"Act.EduInst_hierarchy-entity-cobweb-partitioning-pruned_decreasing_20140624-0705-4ldfadv.json",
"Act.EduInst_hierarchy-entity-cobweb-partitioning-pruned_increasing_20140624-0705-3z6b8kn.json",
"Act.EduInst_hierarchy-entity-cobweb-partitioning-pruned_random_20140624-0705-0nbhpj2.json",
"Act.EduInst_hierarchy-entity-cobweb-partitioning_random_20140624-0705-0nbhpj2.json",
"Act.EduInst_hierarchy-spectral_20140713-0949-0m76br6.json",
"Arch.Struct_hierarchy-entity-cobweb-partitioning_decreasing_20140417-2147-0m7g6cl.json",
"Arch.Struct_hierarchy-entity-cobweb-partitioning_increasing_20140329-2037-3z6kdki.json",
"Arch.Struct_hierarchy-entity-cobweb-partitioning-pruned_decreasing_20140417-2147-0m7g6cl.json",
"Arch.Struct_hierarchy-entity-cobweb-partitioning-pruned_increasing_20140329-2037-3z6kdki.json",
"Arch.Struct_hierarchy-entity-cobweb-partitioning-pruned_random_20140309-0202-43m4eba.json",
"Arch.Struct_hierarchy-entity-cobweb-partitioning_random_20140309-0202-43m4eba.json",
"Arch.Struct_hierarchy-spectral_20140329-1845-42iib6o.json",
"E.NP.WW_hierarchy-entity-cobweb-partitioning_decreasing_20140417-2147-0hrpu4q.json",
"E.NP.WW_hierarchy-entity-cobweb-partitioning_increasing_20140329-2037-42ih2wf.json",
"E.NP.WW_hierarchy-entity-cobweb-partitioning-pruned_decreasing_20140417-2147-0hrpu4q.json",
"E.NP.WW_hierarchy-entity-cobweb-partitioning-pruned_increasing_20140329-2037-42ih2wf.json",
"E.NP.WW_hierarchy-entity-cobweb-partitioning-pruned_random_20140417-2147-43mfa1l.json",
"E.NP.WW_hierarchy-entity-cobweb-partitioning_random_20140417-2147-43mfa1l.json",
"E.NP.WW_hierarchy-spectral_20140329-1845-05k6gq3.json",
"Event_hierarchy-entity-cobweb-partitioning_decreasing_20140309-0128-3z6ad5i.json",
"Event_hierarchy-entity-cobweb-partitioning_increasing_20140329-2044-014ed20.json",
"Event_hierarchy-entity-cobweb-partitioning-pruned_decreasing_20140309-0128-3z6ad5i.json",
"Event_hierarchy-entity-cobweb-partitioning-pruned_increasing_20140329-2044-014ed20.json",
"Event_hierarchy-entity-cobweb-partitioning-pruned_random_20140309-0225-0m7jilf.json",
"Event_hierarchy-entity-cobweb-partitioning_random_20140309-0225-0m7jilf.json",
"Event_hierarchy-spectral_20140329-1843-0m7igmx.json",
"Infr._hierarchy-entity-cobweb-partitioning_decreasing_20140309-0129-42ig0i5.json",
"Infr._hierarchy-entity-cobweb-partitioning_increasing_20140329-2050-3y2oswr.json",
"Infr._hierarchy-entity-cobweb-partitioning-pruned_decreasing_20140309-0129-42ig0i5.json",
"Infr._hierarchy-entity-cobweb-partitioning-pruned_increasing_20140329-2050-3y2oswr.json",
"Infr._hierarchy-entity-cobweb-partitioning-pruned_random_20140406-1132-04ga789.json",
"Infr._hierarchy-entity-cobweb-partitioning_random_20140406-1132-04ga789.json",
"Infr._hierarchy-spectral_20140329-1844-43m363w.json",
"Route_hierarchy-entity-cobweb-partitioning_decreasing_20140309-0158-4lde8l4.json",
"Route_hierarchy-entity-cobweb-partitioning_increasing_20140329-2038-4ftmp6v.json",
"Route_hierarchy-entity-cobweb-partitioning-pruned_decreasing_20140309-0158-4lde8l4.json",
"Route_hierarchy-entity-cobweb-partitioning-pruned_increasing_20140329-2038-4ftmp6v.json",
"Route_hierarchy-entity-cobweb-partitioning-pruned_random_20140309-0232-000chke.json",
"Route_hierarchy-entity-cobweb-partitioning_random_20140309-0232-000chke.json",
"Route_hierarchy-spectral_20140329-1844-0m7k7se.json",
"Species_hierarchy-entity-cobweb-partitioning_decreasing_20140419-1021-0ivma65.json",
"Species_hierarchy-entity-cobweb-partitioning_increasing_20140329-2038-0nbhpn3.json",
"Species_hierarchy-entity-cobweb-partitioning-pruned_decreasing_20140419-1021-0ivma65.json",
"Species_hierarchy-entity-cobweb-partitioning-pruned_increasing_20140329-2038-0nbhpn3.json",
"Species_hierarchy-entity-cobweb-partitioning-pruned_random_20140419-1413-4gxl2xc.json",
"Species_hierarchy-entity-cobweb-partitioning_random_20140419-1413-4gxl2xc.json",
"Species_hierarchy-spectral_20140329-1846-0140ukb.json",
"Tunnel_hierarchy-entity-cobweb-partitioning_decreasing_20140309-1808-0005g03.json",
"Tunnel_hierarchy-entity-cobweb-partitioning_increasing_20140329-2037-0hrq6ju.json",
"Tunnel_hierarchy-entity-cobweb-partitioning-pruned_decreasing_20140309-1808-0005g03.json",
"Tunnel_hierarchy-entity-cobweb-partitioning-pruned_increasing_20140329-2037-0hrq6ju.json",
"Tunnel_hierarchy-entity-cobweb-partitioning-pruned_random_20140309-1817-000gojq.json",
"Tunnel_hierarchy-entity-cobweb-partitioning_random_20140309-1817-000gojq.json",
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








