from flask import Flask,render_template,request
app = Flask(_name_)
Sample_data_books=[
    {"id":1,"title":"Book 1","author":"Author 1","price":10.99},
    {"id":2,"title":"Book 2","author":"Author2","price":9.99},
    #Add more books as needed
    ]
@app.route("/")
def index():
    return render_template("index.html",books=Sample_data_books)
@app.route("/cart",methods=["POST"])
def cart():
    book_id=int(request.form["book_id"])#convert to integer
    book=next((book for book in Sample_data_books if book["id"]==book_id),None)
    #Add book to cart logic return render_template("cart.html",book=book)
    if _name_=="_main_":
        app.run(debug=true)
