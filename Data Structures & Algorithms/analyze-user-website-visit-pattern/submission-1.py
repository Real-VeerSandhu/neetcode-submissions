class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        # store the user's movements

        indices = sorted(range(len(timestamp)), key=lambda i: timestamp[i])
    
        timestamp = [timestamp[i] for i in indices]
        username = [username[i] for i in indices]
        website = [website[i] for i in indices]
        
        user_map = defaultdict(list)

        for i in range(len(username)):
            user_map[username[i]].append(website[i])
        
        seqs = defaultdict(int)

        print(user_map)

        pattern_counts = defaultdict(int)

        max_pattern = (None, 0)


        for user in user_map:
            for i in range(len(user_map[user])):
                if (i+3) > len(user_map[user]):
                    continue
                
                pattern = []
                for j in range(i, i+3):
                    pattern.append(user_map[user][j])
                
                pattern_counts[tuple(pattern)] += 1

                # if pattern_counts[tuple(pattern)] > max_pattern[1]:
                #     max_pattern = (pattern, pattern_counts[tuple(pattern)])
                # elif pattern_counts[tuple(pattern)] == max_pattern[1]:
                #     max_pattern[0] = min(max_pattern[0], pattern)
                
        #         print('****')
        
        # print(pattern_counts)

        max_c = 0
        res = []
        for pattern, count in pattern_counts.items():
            if count > max_c:
                res = pattern
                max_c = count
            elif count == max_c:
                res = min(res, pattern)

        return list(res)