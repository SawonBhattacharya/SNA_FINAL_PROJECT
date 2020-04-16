#import packkages

import networkx as nx
import matplotlib.pyplot as plt

#graph reading

G=nx.read_gml('Covid-19_network.gml')
G.nodes()

#colors depending upon most affected_state

colors=[]
for each in G.nodes():
    if each=='DLH':	#DLH is affected by the jamaat
        colors.append('red')
    else:
        colors.append('skyblue')#not affected
#print(colors)
#required function to analyse the cascading behavior

def find_neigh(each,col,G,colors):
    num=0
    i=0
    for each1 in G.neighbors(each):
        if colors[i]==col:
            num=num+1
        i=i+1
    return num
def cal_effect(G,colors):
    #payoff(skyblue=4)not_affected
    #payoff(red=6)affected
    s=5
    r=100
    i=0
    for each in G.nodes():
        num_s=find_neigh(each,'skyblue',G,colors)
        num_r=find_neigh(each,'red',G,colors)
        payoff_s=s*num_s
        payoff_r=r*num_r
        if(payoff_r>=payoff_s):
            colors[i]='red'
        else:
            colors[i]='skyblue'
        i=i+1

#Cascading Behavior

def cas_behavior():
    flag=1
    cb_count=0
    #print(colors)
    while(flag):
        #print(colors)
        cal_effect(G,colors)
        #print(flag)
        for i in colors:
            if(i=='skyblue'):
                flag=1
                break
            else:
                flag=0
        cb_count=cb_count+1
        #network visualizatiion
        pos=nx.random_layout(G)
        plt.figure(figsize=(20,15))
        nx.draw(G, pos, with_labels=1,edge_color='yellow', node_size=250, node_color=colors,font_size=20,font_color='black')
        plt.title('Graph Representation of Cascading of COVID-19(State-wise) in INDIA', size=25,color='Blue')
        plt.show()
    print("{} it has iterated for full cascading.".format(cb_count))
    
#network visualizatiion(initial phase)

pos=nx.random_layout(G)
plt.figure(figsize=(20,15))
nx.draw(G, pos, with_labels=1,edge_color='yellow', node_size=250, node_color=colors,font_size=20,font_color='black')
plt.title('Graph Representation of COVID-19 after Jamaat in Delhi', size=25,color='Blue')
plt.show()



#Function calling

cas_behavior()