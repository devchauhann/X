
class PersonalizedTeacher:
    def generate_offline(self, reconstruction):
        nodes = reconstruction.get("target_nodes", [])
        explanation = reconstruction.get("explanation_short", "Review core concepts.")
        practice = [{"q":"Sample Q","a":"Sample A"}]
        return {"explanation": explanation, "practice": practice}
