from flask import Flask, request # start by importing flask, request for requesting data fom server

app = Flask(__name__) #create am object of flask using the 'name' constructor

# '/via_postman' is for creating the path for accessing your function
@app.route('/via_postman', methods=['POST']) #this creates a path which you can use to access the function
def math_operation(): #function we want to execute
    if (request.method=='POST'): #when data is sent from app
        #store all variables below
        operation=request.json['operation']
        num1=int(request.json['num1'])
        num2 = int(request.json['num2'])

        if (operation == 'add'):
            r = num1 + num2
            result = 'the sum of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'subtract'):
            r = num1 - num2
            result = 'the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'multiply'):
            r = num1 * num2
            result = 'the product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'divide'):
            r = num1 / num2
            result = 'the quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
        return result

@app.route('/ope', methods=['POST']) #this creates a path which you can use to access the function
def ope_operation(): #function we want to execute
    if (request.method=='POST'): #when data is sent from app
        #store all variables below
        num0=int(request.json['num0'])
        num1=int(request.json['num1'])
        num2 = int(request.json['num2'])

        return str(num1 + num2 + num0)


if __name__ == '__main__':
    app.run(debug=True)

# Open postman to test the code using url: http://127.0.0.1:5000/via_postman or localhost:5000/via_postman