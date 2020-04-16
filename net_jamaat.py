#import packages
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
#read from dataset
result=pd.read_csv('diff.csv')
#print(result)
#type(result)
mat=result.values.tolist()
#print(mat)
type(mat)

#network creation
G=nx.Graph() #undirected graph
state_set=['ANI','AP','AP','ASSM','Bihar','Chandi','CHTG','DLH','Goa','Guj','Har','HP','JK','Jhar','KNTK','Ker','LDK','MP','Mah','Man','Miz','OD','PDC','Pun','Raj','TN','Tel','Trp','UP','UK','WB']
for each in state_set:
    G.add_node(each)
#print(G.nodes())
#nx.draw(G,with_labels=1)
#plt.show()        

#add edges
#print(G.nodes())
count=0
for i in range(30):
    for j in range(31):
        if(i!=j):
            if(mat[i][j]==1 and G.has_edge(i,j)==0):
                G.add_edge(state_set[i],state_set[j])
                count=count+1
nx.write_gml(G,'Covid-19_net.gml')
pos=nx.random_layout(G)
#nx.draw(G,pos,with_labels=1)
#nx.draw_networkx_edge_labels(G,pos)
#plt.show()
#print(G.nodes())
print("No of edges:",count)
print("NO of nodes:",G.number_of_nodes())
#print(nx.pagerank(G))#nx.draw_networkx_edge_labels(G,pos)
#plt.show()
#network formatting

plt.figure(figsize=(20,15))
nx.draw(G, pos, with_labels=1,edge_color='yellow', node_size=250, node_color='yellowgreen',font_size=20,font_color='black')
plt.title('Graph Representation of COVID-19 after Jamaat in India', size=25,color='Blue')
plt.show()

#pagerank calculation
d = nx.pagerank(G)
#print(d)
mx=0
i=0
print ("{:<8} {:<35} {:<25}".format('No','State/Union Territory','PageRank'))
for k, v in d.items():
    pagerank= v
    if(pagerank>mx):
        mx=pagerank
        state=k
    i=i+1
    print ("{:<8} {:<35} {:<25}".format(i,k,pagerank))
print("\n{} has the highest Pagerank: {}".format(state,mx))
