def solution(s):
    result = 0
    zero_cnt = 0
    while s != "1":
        one_cnt = s.count("1")
        zero_cnt += len(s) - one_cnt
        s = str(format(one_cnt, 'b'))
        result += 1
    
    return [result, zero_cnt]