from json_reader.decoder import PyJSONScanner


class CaseInsensitiveScanner(PyJSONScanner):
    def pre_process_text(self, nextchar, text):
        nextchar = nextchar.lower()
        text = text.lower()
        return nextchar, text

    def is_null(self, nextchar, text):
        nextchar, text = self.pre_process_text(nextchar, text)
        return nextchar == 'n' and text == 'null'

    def is_true(self, nextchar, text):
        nextchar, text = self.pre_process_text(nextchar, text)
        return nextchar == 't' and text == 'true'

    def is_false(self, nextchar, text):
        nextchar, text = self.pre_process_text(nextchar, text)
        return nextchar == 'f' and text == 'false'

    def is_nan(self, nextchar, text):
        nextchar, text = self.pre_process_text(nextchar, text)
        return nextchar == 'n' and text == 'nan'

    def is_infinity(self, nextchar, text):
        nextchar, text = self.pre_process_text(nextchar, text)
        return nextchar == 'i' and text == 'infinity'

    def is_negative_infinity(self, nextchar, text):
        nextchar, text = self.pre_process_text(nextchar, text)
        return nextchar == '-' and text == '-infinity'
