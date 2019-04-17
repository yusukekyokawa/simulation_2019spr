def func(x):
    return x**2

def calcArea(a,b,N,function):
    h = (b-a)/N
    S = (h/2)*(function(a) + 2*sum(function(h*i)for i in range(1, N-1))+ function(b))
    return S

if __name__ == "__main__":
    for idx, num in zip([0,1,2,3,4,5],[0,0.2,0.4,0.6,0.8,1]):
        print("f_{0} = {1}".format(idx, func(num)))
    print("Calclulate result is {}".format(calcArea(0, 1, 6, func)))