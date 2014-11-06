

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


basedir_spectral='/home/meng/papershow/20141027-2229-4ftymps-hierarchy-export-lower/'
basedir_newid_spectral='/home/meng/papershow/20141027-2229-4ftymps-hierarchy-export-lower-newid/'

basedir_freebase='/home/meng/papershow/'
basedir_freebase_newid_foreach='/home/meng/papershow/freebase_newid_foreach/'

basedir_union='/home/meng/papershow/union/'


freebasefilename='0dataset.all.entities.in.freebase.class.comma.seprated.entity.typeid.uniq.tree.lower_cotopy.json'

import ujson
json=ujson




from bisect import bisect_left

def BinSearch_dict_use_id_2_find_label(list_input_dict,t):
    low = 0
    height = len(list_input_dict)-1
    while low <= height:
        mid = (low+height)/2
        if list_input_dict[mid].get('id') < t:
            low = mid + 1
        elif list_input_dict[mid].get('id') > t:
            height = mid - 1
        else:
            return list_input_dict[mid].get('label')

    return '------123-4343--1-error-meng--'



def binary_search(a, x, lo=0, hi=None):   # can't use a to specify default for hi
    hi = hi if hi is not None else len(a) # hi defaults to len(a)   
    pos = bisect_left(a,x,lo,hi)          # find insertion position
    return (pos if pos != hi and a[pos] == x else -1) # don't walk off the end

# netities_org is list that contains dict, entities is list that contains string
def replaceId(node,netities_org,entities_dst):
    entities_on_this_node_org=node['entities']
    entities_on_this_node_dst=[]
    for v in entities_on_this_node_org:
        label_tmp=BinSearch_dict_use_id_2_find_label(netities_org,v)
        dst_id=binary_search(entities_dst,label_tmp)
        if dst_id != -1:
            entities_on_this_node_dst.append(dst_id)
    node['new_entities_id']=entities_on_this_node_dst
    node.pop('entities')
    for c in node['children']:
        replaceId(c,netities_org,entities_dst)
        
def update_entity_labels(json_object,netities_org,entities_dst):   
    entities_label_new=[]
    for v in  json_object['entity_labels']:
        label_tmp=v['label']
        dict_tmp=dict()
        dict_tmp['label']=label_tmp
        dict_tmp['id']=binary_search(entities_dst,label_tmp)
        if dict_tmp['id']!=-1:
            entities_label_new.append(dict_tmp)
    json_object['entity_labels_new']=entities_label_new

def update_entity_labels_BADCODE(json_object,netities_org,entities_dst):   
    entities_label_new=[]
    for v in  json_object['entities']:
        label_tmp=v['label']
        dict_tmp=dict()
        dict_tmp['label']=label_tmp
        dict_tmp['id']=binary_search(entities_dst,label_tmp)
        if dict_tmp['id']!=-1:
            entities_label_new.append(dict_tmp)
    json_object['entity_labels_new']=entities_label_new

import sys
for filename_spectral in spectral_filenames: 
    print >>sys.stderr,filename_spectral
    f=open(basedir_union+filename_spectral+'.union')
    entities=[ entity.strip('\n') for entity in f]
    entities.sort()
    
    tmp_spectral=json.loads(open(basedir_spectral+filename_spectral).read())     
    netities_org=tmp_spectral['entity_labels']   
    
    netities_org=sorted(netities_org,key = lambda x:x['id'])
    
    replaceId(tmp_spectral['root'],netities_org,entities)
    update_entity_labels(tmp_spectral,netities_org,entities)
    
    newcontent=dict()
    newcontent['entity_labels_new']=tmp_spectral['entity_labels_new']
    newcontent['root']=tmp_spectral['root']
    newcontent['entity_labels']=tmp_spectral['entity_labels']
    
    f=open(basedir_newid_spectral+filename_spectral,'w')
    sys.stdout=f
    print json.dumps(newcontent)
    f.close()
    
    
    # VEry bad code , but I am very sleepy .should change the name of vars
    
    tmp_spectral=json.loads(open(basedir_freebase+freebasefilename).read())     
    netities_org=tmp_spectral['entities']   
    
    netities_org=sorted(netities_org,key = lambda x:x['id'])
    
    replaceId(tmp_spectral['root'],netities_org,entities)
    update_entity_labels_BADCODE(tmp_spectral,netities_org,entities)
    
    newcontent=dict()
    newcontent['entity_labels_new']=tmp_spectral['entity_labels_new']
    newcontent['root']=tmp_spectral['root']
   
    
    f=open(basedir_freebase_newid_foreach+filename_spectral,'w')
    sys.stdout=f
    print json.dumps(newcontent)
    f.close()
    
    
    
    
   
        

        
        

print >>sys.stderr,'OK!'






