class StopwordRemover:
    DEFAULT_STOPWORDS = {
        'Aanee', 'agarsiisoo', 'Akka', 'Akkam', 'akkasumas', 'Akkasumas', 'akkum', 'Akkuma', 'ala', 'Ala', 'alatti', 'Alatti', 'alla', 'amma', 'Amma', 'Ammo', 'ammoo', 'an', 'An', 'ana', 'anee', 'ani', 'Ani', 'Ati', 'bira', 'Bira', 'Booda', 'Booddee', 'dabalatees', 'dhaan', 'dudduuba', 'dugda', 'Dura', 'duuba', 'Duuba', 'Eega', 'eegana', 'Eegasii', 'ennaa', 'erga', 'ergii', 'f', 'faallaa', 'fagaatee', 'fi', 'Fi', 'fullee', 'fuullee', 'gajjallaa', 'gama', 'Gama', 'gararraa', 'garas', 'garuu', 'giddu', 'gidduu', 'Gidduu', 'gubbaa', 'Gubbaa', 'ha', 'hamma', 'Hanga', 'Henna', 'hoggaa', 'Hogguu', 'hoo', 'Illee', 'Immoo', 'ini', 'innaa', 'inni', 'Inni', 'irra', 'Irra', 'irraa', 'irraan', 'isa', 'Isaa', 'isaaf', 'Isaaf', 'isaan', 'isaani', 'isaanii', 'isaaniitiin', 'isaanirraa', 'Isaanirraa', 'isaanitti', 'isaatiin', 'isarraa', 'isatti', 'Isatti', 'isee', 'Iseen', 'ishee', 'ishii', 'Ishii', 'ishiif', 'Ishiif', 'ishiin', 'ishiirraa', 'Ishiirraa', 'ishiitti', 'isii', 'Isii', 'isiin', 'Isiin', 'isin', 'Isin', 'isini', 'isinii', 'isiniif', 'isiniin', 'isinirraa', 'isinitti', 'ittaanee', 'itti', 'Itti', 'Ittuu', 'itumallee', 'ituu', 'ituullee', 'jala', 'Jala', 'jara', 'Jara', 'jechaan', 'jechoota', 'jechuu', 'jechuun', 'kan', 'Kan', 'kana', 'Kana', 'kanaa', 'kanaaf', 'kanaafi', 'Kanaafuu', 'kanaan', 'kanaatti', 'karaa', 'Kee', 'keenna', 'Keenna', 'keenya', 'Keenya', 'keessa', 'Keessa', 'keessan', 'Keessan', 'keessatti', 'Keessatti', 'Kiyya', 'Koo', 'Kun', 'lafa', 'lama', 'Malee', 'manna', 'maqaa', 'moo', 'na', 'Na', 'naa', 'naaf', 'Naaf', 'naan', 'naannoo', 'narraa', 'Narraa', 'natti', 'Natti', 'nu', 'Nu', 'nuhi', 'nurraa', 'Nurraa', 'nuti', 'Nuti', 'nutti', 'nuu', 'nuuf', 'nuun', 'nuy', 'odoo', 'ofii', 'oggaa', 'oo', 'osoo', 'otoo', 'otumallee', 'otuu', 'otuullee', 'saaniif', 'sadii', 'sana', 'Sana', 'saniif', 'si', 'sii', 'siif', 'siin', 'Siin', 'Silaa', 'simmoo', 'sinitti', 'siqee', 'sirraa', 'sitti', 'Sitti', 'Sun', 'Ta‟ullee', 'tahullee', 'tahullee', 'tahuyyu', 'tahuyyuu', 'tana', 'Tanaaf', 'tanaafi', 'Tanaafuu', 'tawullee', 'teenya', 'Teenya', 'teessan', 'tiyya', 'too', 'tti', 'Tun', 'Utuu', 'waahee', 'waan', 'Waan', 'waggaa', 'wajjin', 'warra', 'Warra', 'woo', 'yammuu', 'yemmuu', 'Yeroo', 'yommii', 'Yommuu', 'Yoo', 'yookaan', 'Yookaan', 'yookiin', 'yoolinimoo', 'Yoom'
    }

    def __init__(self, stopwords=None):
        if not stopwords:
            stopwords = self.DEFAULT_STOPWORDS
        self.stopwords = set(stopwords)

    def remove_stopwords(self, tokens: iter) -> list:
        filtered_tokens = [
            token for token in tokens if token.lower() not in self.stopwords]
        return filtered_tokens


def main():
    # Example usage without providing custom stopwords (uses default stopwords)
    stopword_remover_default = StopwordRemover()
    filtered_tokens_default = stopword_remover_default.remove_stopwords(tokens)
    print(filtered_tokens_default)

    # Example usage with custom stopwords
    custom_stopwords = {"custom1", "custom2", ..., "customN"}
    stopword_remover_custom = StopwordRemover(custom_stopwords)
    filtered_tokens_custom = stopword_remover_custom.remove_stopwords(tokens)
    print(filtered_tokens_custom)


if __name__ == '__main___':
    main()
