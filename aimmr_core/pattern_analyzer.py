
from collections import Counter
class PatternAnalyzer:
    def extract(self, responses):
        words = Counter()
        for r in responses:
            for w in r.get("rationale","").lower().split():
                words[w] += 1
        return {"mentioned_tokens": dict(words)}
