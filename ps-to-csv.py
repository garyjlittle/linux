import pprint
filename="ps.out.txt"
pids={}
with open(filename) as f:
    for line in f:
        if line.find("Sep") >0  :
            #print "found Tue"
            continue
        elif line.find("PID") >0 :
                #print "found PID"
                continue
        else:
            d=line.split()
            pstime=d[3]
            command="-".join(d[4:])
            pid=d[0]
            #spid is thread ID
            spid=d[1]
            (ps_h,ps_m,ps_s)=pstime.split(":")
            try:
                ps_sec=(int(ps_h)*3600)+(int(ps_m)*60)+int(ps_s)
            except ValueError:
                continue
            #print pid,spid,command,ps_sec,pstime,ps_h,ps_m,ps_s
            if pids.has_key(spid):
                pids[spid]["seconds"].append(int(ps_sec)-(pids[spid]["initial"]))
                pids[spid]["total"]=int(ps_sec)-(pids[spid]["initial"])
            else:
                #print "Adding",spid,command
                pids[spid]={}
                pids[spid]["initial"]=int(ps_sec)
                pids[spid]["total"]=0
                pids[spid]["seconds"]=[]
                pids[spid]["command"]=command
	

for key in pids.keys():
    if len(pids[key]["seconds"]) > 0:
        if int(pids[key]["total"]) > 0:
          print key,pids[key]["command"],pids[key]["total"],str(pids[key]["seconds"]).strip('[]')
