from lark import Transformer
class NumTransformer(Transformer):
    def __init__(self):
        super().__init__()
        self.variables = {}

    def number(self, items):
        s = str(items[0])
        return float(s) if '.' in s else int(s)

    def string_val(self, items):
        return items[0][1:-1]  # убираем кавычки

    def get_var(self, items):
        name = str(items[0])
        if name in self.variables:
            return self.variables[name]
        raise NameError(f"Переменная '{name}' не определена")

    # --- Арифметика и сравнения ---
    def comp(self, items): return items[0] == items[1]
    def ncomp(self, items): return items[0] != items[1]
    def mr(self, items): return items[0] > items[1]
    def ls(self, items): return items[0] < items[1]
    def plus(self, items): return items[0] + items[1]
    def minus(self, items): return items[0] - items[1]
    def multiply(self, items): return items[0] * items[1]
    def divide(self, items): return items[0] / items[1]
    def division_integer(self, items): return items[0] // items[1]
    def neg(self, items): return -items[0]
    def pos(self, items): return items[0]

    # --- Инструкции ---
    def write(self, items):
        print(*items[1:])

    def var_definition_with_type(self, items):
        # items: [тип, имя, значение, (опционально: тип_спецификация)]
        var_type = str(items[0])  # 'num', 'str' или 'list'
        name = str(items[1])
        value = items[2]

        # Если num с указанием типа (int/float)
        if var_type == 'num' and len(items) == 4:
            type_hint = items[3]
            if type_hint == "int":
                value = int(value)
            elif type_hint == "float":
                value = float(value)

        self.variables[name] = value
        return None


    def start(self, items):
        return None 
