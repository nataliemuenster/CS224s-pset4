def computeScore(candidate_length,p_t_given_s,p_s_given_t,source,candidate):
    #you need to change this function, given a source, a candidate, and other features, compute the score for this candidate. 
    score=p_t_given_s
    #comment out the above line
    return score

def RerankNbestList():
    #reading the N best list 
    open_=open("data/test_N_best","r")
    write_=open("rerank_test","w")
    #open_=open("data/test_N_best","r")
    #write_=open("rerank_test","w")

    lines=open_.readlines();
    
    source_index=0
    best_score=float("-inf")
    select_candidate=""
    for i in range(0,len(lines)):
        line=lines[i]
        t1=line.find("|");
        index=int(line[0:t1]) # the index of the source
        t2=line.find("|",t1+1);
        candidate_length=int(line[t1+1:t2]);# the length of the current candidate
        t3=line.find("|",t2+1);
        p_t_given_s=float(line[t2+1:t3])# log p(t|s)
        t4=line.find("|",t3+1);
        p_s_given_t=float(line[t3+1:t4])# log p(s|t)
        t5=line.find("|",t4+1);
        current_source=line[t4+1:t5].strip()
        candidate=line[t5+2:].strip()
        score=computeScore(candidate_length,p_t_given_s,p_s_given_t,current_source,candidate)
        if index!=source_index:# we now encounter a new source
            if source_index!=0:# we have selected the best output
                
                write_.write(source+"|"+select_candidate+"\n")
            source=current_source;
            select_candidate=candidate;
            source_index=index
            best_score=score;
        else:
            if score>best_score:
                best_score=score;
                select_candidate=candidate
    write_.write(source+"|"+select_candidate+"\n")

RerankNbestList()
