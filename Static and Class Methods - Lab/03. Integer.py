class Integer:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if isinstance(float_value, float):
            return cls(int(float_value))
        return f'value is not a float'

    @classmethod
    def from_roman(cls, value):  # can "pip install roman" and import roman
        roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        last_char = 0
        result = 0
        n = len(value)
        for i in range(n - 1, -1, -1):
            if roman[value[i]] >= last_char:
                result += roman[value[i]]
            else:
                result -= roman[value[i]]
            last_char = roman[value[i]]
        return cls(result)

    @classmethod
    def from_string(cls, value):
        if isinstance(value, str):
            try:
                int_value = int(value)
                return cls(int_value)
            except:
                pass
        return 'wrong type'

    def __repr__(self):
        return f'{self.value}'