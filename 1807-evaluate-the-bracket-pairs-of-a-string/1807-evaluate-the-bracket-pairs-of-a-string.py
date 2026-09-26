class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:

        # Step 1: Convert knowledge into dictionary
        knowledge_dict = {}

        for key, value in knowledge:
            knowledge_dict[key] = value

        # Step 2: Store the final answer
        result = ""

        # Step 3: Scan the string
        i = 0

        while i < len(s):

            # If current character is '('
            if s[i] == '(':

                # Find the closing bracket
                j = i + 1

                while s[j] != ')':
                    j += 1

                # Extract the key
                key = s[i + 1:j]

                # Find value or use '?'
                if key in knowledge_dict:
                    result += knowledge_dict[key]
                else:
                    result += "?"

                # Move i after ')'
                i = j + 1

            else:
                # Normal character
                result += s[i]
                i += 1

        return result
        