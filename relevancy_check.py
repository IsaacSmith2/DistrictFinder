class RelevancyCheck:
    @staticmethod
    def check_relevancy(content):
        relevant_keywords = ["resign", "step down", "leave", "departure"]
        
        # Check for the word "superintendent"
        if "superintendent" not in content.lower():
            return False

        # Check for any of the relevant keywords
        if not any(keyword in content.lower() for keyword in relevant_keywords):
            return False

        return True
