def winner(cookies):
  
    assert isinstance(cookies, list)
    assert len(cookies) > 0
    assert all(isinstance(x, int) and x >= 0 for x in cookies)

   
    cookies = tuple(sorted(x for x in cookies if x > 0))

    memo = {}

    def can_win(state):
        if not state:
            return False 
        if state in memo:
            return memo[state]

        n = len(state)

        for i in range(n):
            new_state = list(state)
            new_state[i] -= 1
            new_state = tuple(sorted(x for x in new_state if x > 0))
            if not can_win(new_state):
                memo[state] = True
                return True

       
        for i in range(n):
            for j in range(i + 1, n):
                new_state = list(state)
                new_state[i] -= 1
                new_state[j] -= 1
                new_state = tuple(sorted(x for x in new_state if x > 0))
                if not can_win(new_state):
                    memo[state] = True
                    return True

        memo[state] = False
        return False

    return "A" if can_win(cookies) else "B"
