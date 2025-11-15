
import json
class CognitiveModelBuilder:
    def build_offline(self, features):
        nodes = list(features.get("mentioned_tokens", {}).keys())[:3]
        edges = []
        return {"nodes": nodes, "edges": edges}

    def build_gemini(self, rationales, model):
        prompt = f"Extract conceptual nodes from: {rationales}. Return JSON: {{'nodes':[], 'edges':[]}} only."
        raw = model.generate_content(prompt)
        try:
            return json.loads(raw.text)
        except:
            return self.build_offline({"mentioned_tokens": {w:1 for w in ' '.join(rationales).split()}})
