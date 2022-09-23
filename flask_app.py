from flask import Flask, request, render_template
from processing import select_prompt, add_to_list, remove_from_list, display_data, remove_all, restore_original, size, restore_before

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET", "POST"])

def adder_page():
    if request.method == "POST":
        if request.form.get('action') == 'Generate':
            if size() > 0:
                generate = select_prompt()
                return render_template("generate.html", result=generate)
            else:
                MESSAGE = "The prompt list is currently empty. Please populate the list and try again."
                return render_template("modal.html",message=MESSAGE,type="'Generate Prompt'")

        elif request.form.get('action') == 'View List':
            if size() > 0:
                result = display_data()
                return render_template("view_list.html", result=result)
            else:
                MESSAGE = "The prompt list is currently empty. Please populate the list and try again."
                return render_template("modal.html",message=MESSAGE,type="'View List'")

        elif request.form.get('action') == 'Add Prompt':
            to_add = request.form["to_add"]
            result = add_to_list(to_add)
            if result == 0:
                MESSAGE = "This prompt is already present in the list. Please try again."
                return render_template("modal.html",message=MESSAGE,type="'Add Prompt'")
            elif result == 1:
                MESSAGE = "The prompt was successfully added to the list."
            elif result == 2:
                MESSAGE = "Empty input. Please try again."
                return render_template("modal.html",message=MESSAGE,type="'Add Prompt'")
            elif result == 3:
                MESSAGE = "Input is too long. Please try again."
                return render_template("modal.html",message=MESSAGE,type="'Add Prompt'")

        elif request.form.get('action') == 'Remove Prompt':
            to_remove = request.form["to_remove"]
            result = remove_from_list(to_remove)

            if result == 0:
                MESSAGE = "Empty input. Please try again."
                return render_template("modal.html",message=MESSAGE,type="'Remove Prompt'")
            elif result == 1:
                MESSAGE = "The prompt was successfully removed from the list."
            elif result == 2:
                MESSAGE = "This prompt is not present within the list. Please try again."
                return render_template("modal.html",message=MESSAGE,type="'Remove Prompt'")
            elif result == 3:
                MESSAGE = "The prompt list is currently empty. Please populate the list and try again."
                return render_template("modal.html",message=MESSAGE,type="'Remove Prompt'")

        elif request.form.get('action') == 'Remove All':
            if size() > 0:
                remove_all()
            else:
                MESSAGE = "The prompt list is currently empty. Please populate the list and try again."
                return render_template("modal.html",message=MESSAGE,type="'Remove All'")

        elif request.form.get('action') == 'Restore':
            restore_original()

        elif request.form.get('action') == 'Restore Before':
            restore_before()

    return render_template("index.html")

@app.route("/modal")
def modal():
    return render_template("modal.html", message=MESSAGE)

@app.route("/generate")
def generate():
    generate = select_prompt()
    return render_template("generate.html", result=generate)
