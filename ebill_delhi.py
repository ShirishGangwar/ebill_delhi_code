def smartbill(fun):
    def inner(u,r):
        if(u<=300):
            u=0
        elif(u>=300):
            u=u-300
        return fun(u,r)
    return inner
@smartbill
def ebill(u,r):
    bill=u*r
    print(bill)

ebill(301,10)

