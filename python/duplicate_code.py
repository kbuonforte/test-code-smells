"""Code smell: Duplicate Code — same logic copy-pasted across functions."""


def get_admin_dashboard(user):
    if user["role"] != "admin":
        return {"error": "Unauthorized"}
    if not user.get("active"):
        return {"error": "Account disabled"}
    if user.get("password_expired"):
        return {"error": "Password expired"}

    return {"view": "admin_dashboard", "user": user["name"]}


def get_editor_dashboard(user):
    if user["role"] != "editor":
        return {"error": "Unauthorized"}
    if not user.get("active"):
        return {"error": "Account disabled"}
    if user.get("password_expired"):
        return {"error": "Password expired"}

    return {"view": "editor_dashboard", "user": user["name"]}


def get_viewer_dashboard(user):
    if user["role"] != "viewer":
        return {"error": "Unauthorized"}
    if not user.get("active"):
        return {"error": "Account disabled"}
    if user.get("password_expired"):
        return {"error": "Password expired"}

    return {"view": "viewer_dashboard", "user": user["name"]}


def calculate_rectangle_area(width, height):
    if width <= 0 or height <= 0:
        raise ValueError("Dimensions must be positive")
    perimeter = 2 * (width + height)
    area = width * height
    print(f"Perimeter: {perimeter}, Area: {area}")
    return area


def calculate_rectangle_perimeter(width, height):
    if width <= 0 or height <= 0:
        raise ValueError("Dimensions must be positive")
    perimeter = 2 * (width + height)
    area = width * height
    print(f"Perimeter: {perimeter}, Area: {area}")
    return perimeter
