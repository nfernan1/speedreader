from goody       import safe_open
from math        import ceil 
from collections import defaultdict # Use dict or defaultdict


# Define your functions here.

def read_graph(file):
    main_dict = dict()
    mapping = defaultdict(set)
    for line in file.readlines():
        line_split = line.strip().split(';')
        person, friend = line_split[0],line_split[1]
        mapping[person].add(friend)
        mapping[friend].add(person)
        main_dict[person] = mapping[person]
        main_dict[friend] = mapping[friend]
    return main_dict
    
def print_graph(graph):
    print('Graph: source nodes (ordered) -> destination nodes (ordered)')
    for item in sorted(graph):
        friends = sorted(graph[item])
        sof = ', '
        print('  {} -> {}'.format(item, sof.join(friends)))

def find_influencers(graph):
    infl = dict()
    for key in graph:
        number = len(graph[key])
        value = number - ceil(number/2)
        infl[key] = value
    
    while True:
        negative_count = 0  

        for key in infl:
            if infl[key] < 0: 
                negative_count += 1
        if len(infl) - negative_count != 0:
            cand = []
            for key in infl:
                if infl[key] >= 0: cand.append((infl[key],len(graph[key]),key))
        
            minimum = min(cand)
            del infl[minimum[2]]
        
            for key in graph:
                if minimum[2] in graph[key]:
                    infl[key] = infl[key] -1

        else:
            final = set(infl.keys()) 
    return final

    
# Script

if __name__ == '__main__':
    graph = read_graph(safe_open('Enter name of file with graph', 'r',
                                 'Could not find that file'))

    print_graph(graph)
    core = find_influencers(graph)
    print('Influencers =', find_influencers(graph))
