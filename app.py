from flask import Flask, render_template, request
from project import check_type, return_recipe

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    recipe = None
    error = None

    if request.method == "POST":
        category = request.form.get("type")
        query = request.form.get("query", "").strip()

        if category not in ["ingredient", "name", "random"]:
            error = "Invalid category."
        else:
            query = "" if category == "random" else query


            url = check_type(category)
            result = return_recipe(url, query)

            if isinstance(result, dict):
                recipe = result
            else:
                error = result

    return render_template(
        "index.html",
        recipe=recipe,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)