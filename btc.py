import hashlib as h
import sys 
# block number = n
# transactiosn = tr
# previous hash = ph
n=6  # Make update
tr=""  # Enter 
ph=""  # Enter 
nonce=100000000000
zero=int(sys.argv[1])
# Number of 0 in BTS mining (google)
def main(n,tr,ph):
  for i in range(1000000,nonce):
   txt=str(n)+tr+ph+str(i)
   hash=h.sha256(txt.encode()).hexdigest()
   print(hash)
   if hash[0:zero]=="0"*zero:
     print(f"[+] Found Nonce : {i}")
     print(f"[+] Hash : {hash}")
     break
     
if __name__=="__main__":
 main(n,tr,ph)


#----
