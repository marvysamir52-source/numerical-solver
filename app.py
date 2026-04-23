from flask import Flask, render_template, request
import math

app = Flask(__name__)

# =========================================================
# Chapter 1: Root Finding Methods
# =========================================================

def solve_bisection_data():
    eps = 1.0
    xl = 0.0
    xu = 1.0

    def f(x):
        return 4 * x**3 - 6 * x**2 + 7 * x - 2.3

    rows = []
    xr = 0
    error = 0
    iteration = 0

    if f(xl) * f(xu) >= 0:
        return "Bisection Method", "f(x) = 4x^3 - 6x^2 + 7x - 2.3 , xl = 0 , xu = 1 , eps = 1%", "Invalid interval", [], []

    while True:
        xr_old = xr
        xr = (xl + xu) / 2

        if iteration != 0 and xr != 0:
            error = abs((xr - xr_old) / xr) * 100

        rows.append([
            iteration,
            round(xl, 6),
            round(f(xl), 6),
            round(xu, 6),
            round(f(xu), 6),
            round(xr, 6),
            round(f(xr), 6),
            "-" if iteration == 0 else round(error, 6)
        ])

        if f(xl) * f(xr) < 0:
            xu = xr
        else:
            xl = xr

        iteration += 1

        if iteration != 1 and error <= eps:
            break

    return (
        "Bisection Method",
        "f(x) = 4x^3 - 6x^2 + 7x - 2.3 , xl = 0 , xu = 1 , eps = 1%",
        f"Root = {xr:.6f}",
        ["i", "xl", "f(xl)", "xu", "f(xu)", "xr", "f(xr)", "Error %"],
        rows
    )


def solve_false_position_data():
    eps = 0.2
    xl = -1.0
    xu = 0.0

    def f(x):
        return -13 - (20 * x) + (19 * x**2) - (3 * x**3)

    rows = []
    xr = 0
    error = 0
    iteration = 0

    if f(xl) * f(xu) >= 0:
        return "False Position Method", "f(x) = -13 - 20x + 19x^2 - 3x^3 , xl = -1 , xu = 0 , eps = 0.2%", "Invalid interval", [], []

    while True:
        xr_old = xr
        denominator = f(xl) - f(xu)

        if denominator == 0:
            break

        xr = xu - (f(xu) * (xl - xu)) / denominator

        if iteration != 0 and xr != 0:
            error = abs((xr - xr_old) / xr) * 100

        rows.append([
            iteration,
            round(xl, 6),
            round(f(xl), 6),
            round(xu, 6),
            round(f(xu), 6),
            round(xr, 6),
            round(f(xr), 6),
            "-" if iteration == 0 else round(error, 6)
        ])

        if f(xl) * f(xr) > 0:
            xl = xr
        else:
            xu = xr

        iteration += 1

        if iteration != 1 and error <= eps:
            break

    return (
        "False Position Method",
        "f(x) = -13 - 20x + 19x^2 - 3x^3 , xl = -1 , xu = 0 , eps = 0.2%",
        f"Root = {xr:.6f}",
        ["i", "xl", "f(xl)", "xu", "f(xu)", "xr", "f(xr)", "Error %"],
        rows
    )


def solve_fixed_point_data():
    eps = 0.2
    x0 = 5.0

    def g(x):
        return math.sqrt((1.8 * x) + 2.5)

    rows = []
    iteration = 0

    while True:
        x1 = g(x0)
        error = abs((x1 - x0) / x1) * 100 if x1 != 0 else 0

        rows.append([
            iteration,
            round(x0, 6),
            round(x1, 6),
            round(error, 6)
        ])

        iteration += 1

        if error <= eps:
            break

        x0 = x1

    return (
        "Fixed Point Method",
        "g(x) = sqrt(1.8x + 2.5) , x0 = 5 , eps = 0.2%",
        f"Root = {x1:.6f}",
        ["i", "Xi", "Xi+1", "Error %"],
        rows
    )


def solve_newton_data():
    eps = 0.5
    x0 = 1.0

    def f(x):
        return -2 + 6*x - 4*x**2 + 0.5*x**3

    def f_dash(x):
        return 6 - 8*x + 1.5*x**2

    rows = []
    iteration = 0

    while True:
        derivative = f_dash(x0)
        if derivative == 0:
            return "Newton Method", "f(x) = -2 + 6x - 4x^2 + 0.5x^3 , f'(x) = 6 - 8x + 1.5x^2 , x0 = 1 , eps = 0.5%", "Derivative = 0, cannot continue", [], []

        x1 = x0 - (f(x0) / derivative)
        error = abs((x1 - x0) / x1) * 100 if x1 != 0 else 0

        rows.append([
            iteration,
            round(x0, 6),
            round(f(x0), 6),
            round(derivative, 6),
            round(x1, 6),
            round(error, 6)
        ])

        iteration += 1

        if error <= eps:
            break

        x0 = x1

    return (
        "Newton Method",
        "f(x) = -2 + 6x - 4x^2 + 0.5x^3 , f'(x) = 6 - 8x + 1.5x^2 , x0 = 1 , eps = 0.5%",
        f"Root = {x1:.6f}",
        ["i", "Xi", "f(Xi)", "f'(Xi)", "Xi+1", "Error %"],
        rows
    )


def solve_secant_data():
    eps = 0.7
    xi_minus1 = 3.0
    xi = 4.0

    def f(x):
        return 2*x**3 - 11.7*x**2 + 17.7*x - 5

    rows = []
    iteration = 0
    error = 0

    while True:
        denominator = f(xi_minus1) - f(xi)
        if denominator == 0:
            return "Secant Method", "f(x) = 2x^3 - 11.7x^2 + 17.7x - 5 , x(i-1) = 3 , x(i) = 4 , eps = 0.7%", "Division by zero", [], []

        xi_next = xi - ((f(xi) * (xi_minus1 - xi)) / denominator)

        if xi_next != 0:
            error = abs((xi_next - xi) / xi_next) * 100

        rows.append([
            iteration,
            round(xi_minus1, 6),
            round(xi, 6),
            round(f(xi), 6),
            round(xi_next, 6),
            round(error, 6)
        ])

        iteration += 1

        if iteration != 1 and error <= eps:
            break

        xi_minus1 = xi
        xi = xi_next

    return (
        "Secant Method",
        "f(x) = 2x^3 - 11.7x^2 + 17.7x - 5 , x(i-1) = 3 , x(i) = 4 , eps = 0.7%",
        f"Root = {xi_next:.6f}",
        ["i", "Xi-1", "Xi", "f(Xi)", "Xi+1", "Error %"],
        rows
    )


# =========================================================
# Chapter 2: Linear Systems
# =========================================================

def solve_gauss_data():
    a, b, c = 2, 3, 8
    d, e, f = 1, -4, -2

    denominator = (a * e - b * d)
    if denominator == 0:
        return "Gauss Elimination", "2x + 3y = 8    and    1x - 4y = -2", "No unique solution", [], []

    y = (a * f - c * d) / denominator
    x = (c - b * y) / a

    rows = [
        ["Equation 1", f"{a}x + {b}y = {c}"],
        ["Equation 2", f"{d}x + {e}y = {f}"],
        ["x", round(x, 6)],
        ["y", round(y, 6)]
    ]

    return (
        "Gauss Elimination",
        "2x + 3y = 8    and    1x - 4y = -2",
        f"x = {x:.6f}, y = {y:.6f}",
        ["Step", "Value"],
        rows
    )


def solve_lu_data():
    a, b, c = 2, 3, 8
    d, e, f = 1, -4, -2

    if a == 0:
        return "LU Decomposition", "2x + 3y = 8    and    1x - 4y = -2", "Division by zero", [], []

    u11 = a
    u12 = b
    l21 = d / a
    u22 = e - l21 * b

    if u22 == 0:
        return "LU Decomposition", "2x + 3y = 8    and    1x - 4y = -2", "No unique solution", [], []

    z1 = c
    z2 = f - l21 * z1

    y = z2 / u22
    x = (z1 - u12 * y) / u11

    rows = [
        ["u11", round(u11, 6)],
        ["u12", round(u12, 6)],
        ["l21", round(l21, 6)],
        ["u22", round(u22, 6)],
        ["z1", round(z1, 6)],
        ["z2", round(z2, 6)],
        ["x", round(x, 6)],
        ["y", round(y, 6)]
    ]

    return (
        "LU Decomposition",
        "2x + 3y = 8    and    1x - 4y = -2",
        f"x = {x:.6f}, y = {y:.6f}",
        ["Step", "Value"],
        rows
    )


def solve_cramer_data():
    a, b, c = 2, 3, 8
    d, e, f = 1, -4, -2

    D = a * e - b * d

    if D == 0:
        return "Cramer's Rule", "2x + 3y = 8    and    1x - 4y = -2", "No unique solution", [], []

    Dx = c * e - b * f
    Dy = a * f - c * d

    x = Dx / D
    y = Dy / D

    rows = [
        ["D", round(D, 6)],
        ["Dx", round(Dx, 6)],
        ["Dy", round(Dy, 6)],
        ["x", round(x, 6)],
        ["y", round(y, 6)]
    ]

    return (
        "Cramer's Rule",
        "2x + 3y = 8    and    1x - 4y = -2",
        f"x = {x:.6f}, y = {y:.6f}",
        ["Step", "Value"],
        rows
    )


@app.route('/', methods=['GET', 'POST'])
def home():
    method_title = "Choose a method"
    problem_text = ""
    final_result = "The result will appear here"
    headers = []
    rows = []

    if request.method == 'POST':
        selected = request.form.get('method')

        if selected == 'bisection':
            method_title, problem_text, final_result, headers, rows = solve_bisection_data()
        elif selected == 'false_position':
            method_title, problem_text, final_result, headers, rows = solve_false_position_data()
        elif selected == 'fixed_point':
            method_title, problem_text, final_result, headers, rows = solve_fixed_point_data()
        elif selected == 'newton':
            method_title, problem_text, final_result, headers, rows = solve_newton_data()
        elif selected == 'secant':
            method_title, problem_text, final_result, headers, rows = solve_secant_data()
        elif selected == 'gauss':
            method_title, problem_text, final_result, headers, rows = solve_gauss_data()
        elif selected == 'lu':
            method_title, problem_text, final_result, headers, rows = solve_lu_data()
        elif selected == 'cramer':
            method_title, problem_text, final_result, headers, rows = solve_cramer_data()

    return render_template(
        'index.html',
        method_title=method_title,
        problem_text=problem_text,
        final_result=final_result,
        headers=headers,
        rows=rows
    )

if __name__ == '__main__':
    app.run(debug=True)