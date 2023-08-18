from collections import Counter
import re

class DistrictInspector:
    def __init__(self, article_content):
        self.article_content = article_content

    def get_district_name(self):
        # Patterns to identify districts
        patterns = [
            r'School District',
            r'\bISD\b',
            r'\bUSD\b',
            r'Unified School District',
            r'Independent School District',
            r'Public Schools',
            r'Schools',
            r'District'
        ]

        potential_districts = []

        # Search for sequences of capitalized words that end just before a word from our pattern list
        for pattern in patterns:
            matches = re.findall(r'([A-Z][a-z]+(?: [A-Z][a-z]+){0,4}?) ' + pattern, self.article_content)
            potential_districts.extend([match + ' ' + pattern for match in matches])

        # Return the potential district name with the most capitalized words
        if potential_districts:
            return max(potential_districts, key=lambda x: len(re.findall(r'[A-Z][a-z]+', x)))
        else:
            return "District name not found in the article"

