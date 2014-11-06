import ujson

json=ujson

basedir_test='/home/meng/papershow/freebase_newid_foreach/'
dict_file=json.loads(open(basedir_test+'Tunnel_hierarchy-spectral_20140523-0533-4ldfgin.json').read())

fout_1=open(basedir_test+'out1','w')
 

def print_use_org(e_id_map,node,layer):
    for i in range(layer):
        fout_1.write('    ')
    print node.keys()
    for v in node['new_entities_id']:
#         for ttt in e_id_map :
#             if ttt['id']==v:
                fout_1.write(str(v)+' ')
    fout_1.write('\n')
    for c in node['children']:
        print_use_org(e_id_map,c,layer+1)
 
        
print    dict_file.keys()     
        
        
print_use_org(dict_file['entity_labels_new'],dict_file['root'],0)        

             
    






fout_1.close()
 

print 'OK'
 