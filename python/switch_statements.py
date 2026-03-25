"""Code smell: Excessive Switch/If-Elif Chains — type checking instead of polymorphism."""


def calculate_area(shape_type, **kwargs):
    import math
    if shape_type == "circle":
        return math.pi * kwargs["radius"] ** 2
    elif shape_type == "rectangle":
        return kwargs["width"] * kwargs["height"]
    elif shape_type == "triangle":
        return 0.5 * kwargs["base"] * kwargs["height"]
    elif shape_type == "trapezoid":
        return 0.5 * (kwargs["base1"] + kwargs["base2"]) * kwargs["height"]
    elif shape_type == "ellipse":
        return math.pi * kwargs["semi_major"] * kwargs["semi_minor"]
    else:
        raise ValueError(f"Unknown shape: {shape_type}")


def calculate_perimeter(shape_type, **kwargs):
    import math
    if shape_type == "circle":
        return 2 * math.pi * kwargs["radius"]
    elif shape_type == "rectangle":
        return 2 * (kwargs["width"] + kwargs["height"])
    elif shape_type == "triangle":
        return kwargs["a"] + kwargs["b"] + kwargs["c"]
    elif shape_type == "trapezoid":
        return kwargs["base1"] + kwargs["base2"] + kwargs["leg1"] + kwargs["leg2"]
    else:
        raise ValueError(f"Unknown shape: {shape_type}")


def describe_shape(shape_type, **kwargs):
    if shape_type == "circle":
        return f"Circle with radius {kwargs['radius']}"
    elif shape_type == "rectangle":
        return f"Rectangle {kwargs['width']}x{kwargs['height']}"
    elif shape_type == "triangle":
        return f"Triangle with base {kwargs['base']}"
    elif shape_type == "trapezoid":
        return f"Trapezoid with bases {kwargs['base1']} and {kwargs['base2']}"
    else:
        return "Unknown shape"


def get_employee_pay(employee_type, hours, base_rate):
    if employee_type == "fulltime":
        return base_rate * 40
    elif employee_type == "parttime":
        return base_rate * hours
    elif employee_type == "contractor":
        return base_rate * hours * 1.3
    elif employee_type == "intern":
        return base_rate * min(hours, 20)
    elif employee_type == "executive":
        return base_rate * 40 + 5000  # bonus
    else:
        raise ValueError(f"Unknown employee type: {employee_type}")


def get_tax_rate(employee_type, income):
    if employee_type == "fulltime":
        return 0.25 if income > 50000 else 0.15
    elif employee_type == "parttime":
        return 0.15
    elif employee_type == "contractor":
        return 0.30
    elif employee_type == "intern":
        return 0.10
    elif employee_type == "executive":
        return 0.37
    else:
        return 0.20
