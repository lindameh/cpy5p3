m = [0 for i in range(100)]
def m_series(i):
    for j in range(i):
        m[i] = m[i] + (j+1)/(j+2)

print("{0:<5}".format("i"),"m(i)")
for i in range(1,21):
    m_series(i)
    print("{0:<5}".format(i),"{0:.4f}".format(m[i]))
