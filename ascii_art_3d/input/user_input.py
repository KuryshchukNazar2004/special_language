class UserInput:
    def get_shape_params(self):
        shape_type = input("Введіть тип фігури (cube, sphere, pyramid): ").strip().lower()
        size = int(input("Введіть розмір фігури: "))
        color = input("Введіть колір фігури (red, green, blue, white): ").strip().lower()
        return shape_type, {'size': size, 'color': color}
