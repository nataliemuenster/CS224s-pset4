import random
def ReadDevTestFile():
    #reading source inputs from dev.txt or test.txt. Change the file name accordingly.
    open_=open("data/dev.txt","r")
    #reading dev.txt
    #open_=open("test.txt","r")
    #reading dev.txt
    lines=open_.readlines();
    sources=[];
    for line in lines:
        split_=line.strip().split("|");
        #split a readed line. split_[0] is the source input and split_[1] is the gold-standard output
        sources.append(split_[0])
    return sources

def ReadPool():
    #read data from pool.txt
    open_=open("data/pool.txt","r")
    lines=open_.readlines();
    pool_sources=[];
    pool_targets=[];
    for line in lines:
        split_=line.strip().split("|");
        pool_sources.append(split_[0])
        pool_targets.append(split_[1])
    return pool_sources,pool_targets

def SelectOutput(new_input,pool_sources,pool_targets):
    #please change this function, return a target in pool_targets
    
    #comment out the following line
    select_target=pool_targets[random.randint(0,len(pool_targets)-1)]
    return select_target


sources=ReadDevTestFile()
pool_sources,pool_targets=ReadPool()

open_write=open("dev_decode.tgt","w")
#open_write=open("test_decode.txt","w")
#write the correct file accordingly
i=0
for new_line in sources:
    i=i+1
    select_target=SelectOutput(new_line,pool_sources,pool_targets)
    open_write.write(new_line+"|"+select_target+"\n");

open_write.close()
