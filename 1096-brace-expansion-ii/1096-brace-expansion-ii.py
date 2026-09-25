class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:

        def parse(i):
            result = set()
            current = {""}

            while i < len(expression) and expression[i] != '}':
                
                # Case 1: comma
                if expression[i] == ',':
                    result |= current
                    current = {""}
                    i += 1

                # Case 2: opening brace
                elif expression[i] == '{':
                    inside, i = parse(i + 1)

                    # Concatenate current with inside
                    new_current = set()

                    for a in current:
                        for b in inside:
                            new_current.add(a + b)

                    current = new_current

                # Case 3: lowercase letter
                else:
                    new_current = set()

                    for word in current:
                        new_current.add(word + expression[i])

                    current = new_current
                    i += 1

            # Add the last part
            result |= current

            # Skip '}'
            if i < len(expression) and expression[i] == '}':
                i += 1

            return result, i

        result, _ = parse(0)

        return sorted(result)
        