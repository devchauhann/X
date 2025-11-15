
class MisconceptionDetector:
    def detect(self, inferred, canonical_nodes):
        inferred_nodes = set(inferred.get("nodes", []))
        missing = [c for c in canonical_nodes if c not in inferred_nodes]
        extra = [n for n in inferred_nodes if n not in canonical_nodes]
        return {"missing_nodes": missing, "extra_nodes": extra}
