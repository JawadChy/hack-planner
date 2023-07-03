# line imports functionality into our project :D
from flask import Flask, render_template, request, redirect

# initializing our application. Basically creating our flask object here.
app = Flask(__name__)

# route associate path with a view
# view functions refer to functions that show something on the screen
# decorators are like wrapper functions

items = []

@app.route('/')
def checklist():
    return render_template('checklist.html', items=items)


@app.route("/add", methods=["POST"])
def add_item():
    item = request.form["item"]
    items.append(item) # Append new item to the list
    return redirect("/")

# now we're doing the update functionality
@app.route("/edit/<int:item_id>", methods=["GET", "POST"])
def edit_item(item_id):
    item = items[item_id - 1] # Retrive the item based on its input id

    if request.method == 'POST':
        new_item = request.form["item"]
        items[item_id - 1] = new_item
        return redirect("/")
    
    return render_template("edit.html", item = item, item_id = item_id)

# delete functionality

@app.route('/delete/<int:item_id>')
def delete_item(item_id):
    del items[item_id - 1]
    return redirect('/')



