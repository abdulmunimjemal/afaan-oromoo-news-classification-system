"""
Rule-Based Afaan Oromoo word Stemmer

Author: Abdulmunim Jundurahman Jemal
Date: Nov 14 2023
Institute: Addis Ababa Institute of Technology

Based on the paper: "Designing a Stemmer for Afaan Oromo Text: A Hybrid Approach" by Debela Tesfaye
"""


class AfaanOromooStemmer:
    def __init__(self):
        pass

    def apply_rules(self, word):
        word = word.lower()  # for the sake of consistency
        # Rule clusters as described in the provided information
        clusters = [
            lambda w: self.rule_cluster_1(w),
            lambda w: self.rule_cluster_2(w),
            lambda w: self.rule_cluster_3(w),
            lambda w: self.rule_cluster_4(w),
            lambda w: self.rule_cluster_5(w),
            lambda w: self.rule_cluster_6(w),
            lambda w: self.rule_cluster_7(w)
        ]
        for cluster in clusters:
            stemmed_word = cluster(word)
            if stemmed_word:
                return stemmed_word
        # If no rule in the clusters matches, return the original word
        return word

    def rule_cluster_1(self, word):
        # Rule cluster 1: Delete suffixes if measure is greater or equal to 1
        # Example: "olee", "olii", "oolii", "ota", "oolee", "oota"
        suffixes = ["olee", "olii", "oolii", "ota", "oolee", "oota"]
        for suffix in suffixes:
            if word.endswith(suffix) and self.measure(word) >= 1:
                return word[:-len(suffix)]
        return None

    def rule_cluster_2(self, word):
        # Rule cluster 2: Delete specific suffixes if measure >= 1
        # Example: "ittii", "dha", "ttii", "irra", "tii", "rra"
        suffixes = ["ittii", "dha", "ttii", "irra", "tii", "rra"]
        for suffix in suffixes:
            if word.endswith(suffix) and self.measure(word) >= 1:
                return word[:-len(suffix)]
        return None

    def rule_cluster_3(self, word):
        # Rule cluster 3: Delete suffixes if measure >= 1 and ends with consonant
        # Example: "eenya", "ina", "offaa", "annoo", "umsa", "ummaa", "insa"
        suffixes = ["eenya", "ina", "offaa", "annoo", "umsa", "ummaa", "insa"]
        for suffix in suffixes:
            if word.endswith(suffix) and self.measure(word) >= 1 and word[-1] in "bcdfghjklmnpqrstvwxyz":
                return word[:-len(suffix)]
        return None

    def rule_cluster_4(self, word):
        # Rule cluster 4: Suffixes that are removed if measure is greater or equal to 1
        # or substituted with the suffix -` if measure equals zero
        suffixes = ["`aa", "'uu", "'ee", "`a", "'e", "'u", "s",
                    "suu", "sa", "se", "si", "Ssi", "sse", "ssa", "nye", "nya"]
        for suffix in suffixes:
            if word.endswith(suffix):
                if self.measure(word) >= 1:
                    return word[:-len(suffix)]
                else:
                    return word[:-len(suffix)] + "`"
        return None

    def rule_cluster_5(self, word):
        # Rule cluster 5: Special cases handling
        special_suffixes = ["du", "di", "dan",
                            "Lee", "wwan", "een", "an", "f", "n"]
        for suffix in special_suffixes:
            if word.endswith(suffix):
                if suffix in ["du", "di", "dan"] and self.measure(word) >= 1:
                    return word[:-len(suffix)]
                elif suffix == "dan" and self.measure(word) == 0:
                    return word[:-len(suffix)] + "d"
                elif suffix == "Lee" and self.measure(word) >= 1:
                    return word[:-len(suffix)]
                elif suffix in ["wwan", "een"] and self.measure(word) >= 1:
                    return word[:-len(suffix)]
                elif suffix == "an" and self.measure(word) >= 1:
                    return word[:-len(suffix)]
                elif suffix in ["f", "n"] and self.measure(word) >= 1:
                    return word[:-len(suffix)]
        return None

    def rule_cluster_6(self, word):
        # Rule cluster 6: Suffixes that are removed if measure is greater or equal to 1
        # or substituted with –t if measure equals zero
        suffixes = ["te", "tu", "ti", "tee", "tuu", "ne", "nu", "na", "nne", "nnu", "nna", "dhaa", "chaaf",
                    "dhaaf", "tiif", "ach", "adh", "Chuu", "at", "att", "ch", "Tanu", "tanuu", "tan", "tani"]
        for suffix in suffixes:
            if word.endswith(suffix):
                if self.measure(word) >= 1:
                    return word[:-len(suffix)]
                else:
                    return word[:-len(suffix)] + "t"
        return None

    def rule_cluster_7(self, word):
        # Rule cluster 7: Rules that conflate words formed by duplication of the first syllabus
        if len(word) <= 3:
            return word
        if word[0] == word[1]:
            return word[0] + word[2:]
        if word[0] == 'C' and word[1] == 'C':
            return word[0] + word[1] + word[2:]
        if word[0] == 'V' and word[1] == '`':
            return word[0] + word[2:]
        return None

    def measure(self, word):
        # Calculate the number of vowel-consonant sequences in the word
        # A vowel-consonant sequence is defined where consecutive vowels or consonants are counted as one
        vowels = set("aeiou")
        measure = 0
        consecutive_count = 0
        for char in word:
            if char.lower() in vowels:
                if consecutive_count == 0:
                    measure += 1
                    consecutive_count = 1
            else:
                consecutive_count = 0
        return measure

    def stem(self, word):
        stemmed_word = self.apply_rules(word)
        return stemmed_word


if __name__ == "__main__":
    stemmer = AfaanOromooStemmer()
    sample = "Sirni Gadaa diimookraatawaa barbaadanittiakka jabaatti, qulqullaa'uun"
    tokens = remove_stopwords(sample)
    print("Original Text: " + sample)
    print("---- RUNNING STOPWORDS REMOVER AND TOKENIZER ")
    print("Length of tokens: ", len(tokens))
    print("Tokens: ", tokens)
    print("--- RUNNING STEMMER")
    stemmed = [stemmer.stem(token) for token in tokens]
    print("STEMMED: ", stemmed)
