def dh(x_a,x_s,a,q):
    pub_A = (a**x_a)%q #here we create the pub key which we need to send to saad. we at arslan side rn
    pub_S = (a**x_s)%q# here we receive saads pub key . which we use in next line to deduce secret key
    k = (pub_S**x_a)%q
    return k

print(dh(165893,108037,3,17))