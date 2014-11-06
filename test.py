import ujson

json=ujson

basedir_test='/home/meng/papershow/20141027-2229-4ftymps-hierarchy-export-newid/'

dict_file=json.loads(open(basedir_test+'Tunnel_hierarchy-spectral_20140523-0533-4ldfgin.json').read())

fout_1=open(basedir_test+'out1','w')
fout_2=open(basedir_test+'out2','w')

def print_use_org(e_id_map,node,layer):
    for i in range(layer):
        fout_1.write('    ')
    
    for v in node['entities']:
        for ttt in e_id_map :
            if ttt['id']==v:
                fout_1.write(ttt['label']+' ')
    fout_1.write('\n')
    for c in node['children']:
        print_use_org(e_id_map,c,layer+1)


def print_use_newid(e_id_map,node,layer):
    for i in range(layer):
        fout_2.write('    ')
    for v in node['new_entities_id']:
        for ttt in e_id_map :
            if ttt['id']==v:
                fout_2.write(ttt['label']+' ')
    fout_2.write('\n')
    for c in node['children']:
        print_use_newid(e_id_map,c,layer+1)
        
        
        
        
print_use_org(dict_file['entity_labels'],dict_file['root'],0)        

print_use_newid(dict_file['entity_labels_new'],dict_file['root'],0)                 
    






fout_1.close()
fout_2.close()

print 'OK'
 