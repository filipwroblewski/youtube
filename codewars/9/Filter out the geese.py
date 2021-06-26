geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    tmp = []
    for bird in birds:
        if bird not in geese:
            tmp.append(bird)
    return tmp


goose_filter(["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]) 
#["Mallard", "Hook Bill", "Crested", "Blue Swedish"]
goose_filter(["Mallard", "Barbary", "Hook Bill", "Blue Swedish", "Crested"])    
# ["Mallard", "Barbary", "Hook Bill", "Blue Swedish", "Crested"]
goose_filter(["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]) # []