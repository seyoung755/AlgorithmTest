from collections import defaultdict
def solution(words, queries):
    answer = []
    
    # 결국 trie로 ?가 등장할 때까지 검색하여 글자수가 같은 문자 개수를 리턴하면 된다.
    # ?가 앞에 등장하면? 뒤에서부터 검색 -> trie에 저장할 때도 뒤집어서
    # ?가 뒤에 등장하면? 앞에서부터 검색 -> ?가 등장하면 문자 수 리턴
    # ?만 등장하면? 같은 글자수인 문자를 모두 리턴 => 글자수를 세놔야 한다
    cnt = defaultdict(int)
    r_words = []
    for word in words:
        l = len(word)
        cnt[l] += 1
        r_words.append(word[::-1])
        
    
    trie = make_trie(words)
    r_trie = make_trie(r_words)
    
    for q in queries:
        l = len(q)
        if q[0] == '?' and q[-1] == '?':
            answer.append(cnt[l])
        elif q[0] == '?': # r_trie에서 검색
            answer.append(search(r_trie, q[::-1], l))
        elif q[-1] == '?': # trie에서 검색
            answer.append(search(trie, q, l))
    
    return answer

def search(trie, q, l):
    cur = trie
    for char in q:
        if char == '?':
            return cur['#'][l]
        if char in cur:
            cur = cur[char]
        else:
            return 0
    

def make_trie(words):
    trie = {}
    for word in words:
        cur = trie
        l = len(word)
        for char in word:
            # 이미 등장한 글자라면
            if char in cur:
                cur = cur[char] # 해당 노드로 이동한다
                # 현재 노드에 입력된 글자수를 기록한다
                if '#' in cur:
                    cur['#'][l] += 1 
                else:
                    cur['#'] = defaultdict(int)
                    cur['#'][l] = 1
            
            # 처음 등장하는 글자라면 
            else:
                cur[char] = {} # 다음 노드를 만든다 
                cur = cur[char] # 노드를 이동한뒤 
                # 현재 노드에 입력된 글자수를 기록한다
                if '#' in cur:
                    cur['#'][l] += 1 
                else:
                    cur['#'] = defaultdict(int)
                    cur['#'][l] = 1
    return trie
