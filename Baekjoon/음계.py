def get_answer(codes):
    ascending = [i for i in range(1,9)]
    descending = [i for i in range(8,0,-1)]
    
    if codes != ascending and codes != descending:
        return "mixed"

    return "ascending" if codes == ascending else "descending"

codes = list(map(int, input().split()))
print(get_answer(codes))