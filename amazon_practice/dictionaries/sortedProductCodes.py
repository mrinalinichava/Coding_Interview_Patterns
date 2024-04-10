from collections import defaultdict
def sortedProduct(order,productCodes):
    d = defaultdict(int)
    for i,ele in enumerate(order):
        d[ele]= i
    print(d)

    for productcode in productCodes:
        print(d[productcode])

    res_prodcode = sorted(productCodes,key = lambda x: [d[char] for char in x])
    return res_prodcode

order = "hgfedcba"
productCodes = ["abc", "bca", "cab", "bac"]
print(sortedProduct(order,productCodes))

