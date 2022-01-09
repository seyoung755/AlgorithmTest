def get_answer(codes):
    prev = 0
    answer_flag = ''
    for code in codes:
        if code > prev:
            if answer_flag == 'decending':
                return "mixed"
            answer_flag = 'asending'
            prev = code
        
        else:
            if answer_flag == 'ascending':
                return "mixed"
            answer_flag = 'decending'
            prev = code
    return answer_flag

codes = list(map(int, input().split()))
print(get_answer(codes))