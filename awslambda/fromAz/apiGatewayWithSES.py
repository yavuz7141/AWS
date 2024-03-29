import json, boto3

ses = boto3.client('ses')

FROM_EMAIL_ADDRESS = 'yavuz7141@gmail.com'

#customerEmail='yavuz7141@hotmail.com' #when using this code on lambda, it will ask the customer lambda.if u run tjis code on laambda dont use customerEmail.
                  # indicate,use customerEmail='' in code if  you run this code locally on your laptop.

def lambda_handler(event, context):
    #Step 1: Parse given query string parameters
	purchaseId = event['queryStringParameters']['purchaseId'] #API captures event(for ex: search, mouse click,..any request) queries coming from application
	purchaseItem = event['queryStringParameters']['item']   #here "item" request coming from application and API captures this request
	purchaseAmount = event['queryStringParameters']['amount']
	customerEmail = event['queryStringParameters']['email']

	print('purchaseId=' + purchaseId) # use (print) as much as u can, because whatever you print it goes to cloudwatch logs,will be easier to trobleshoot in case of issue.
	print('purchaseItem=' + purchaseItem)
	print('purchaseAmount=' + purchaseAmount)
	print('customerEmail='+customerEmail)

	#Step2: Create body of the response object
	purchaseResponse = {}
	purchaseResponse['orderNumber'] = purchaseId
	purchaseResponse['item'] = purchaseItem
	purchaseResponse['amount'] = purchaseAmount
	purchaseResponse['email'] = customerEmail
	purchaseResponse['message'] = 'We have received your order, thank you.'

	#Step 3: Create http response object
	responseObject = {}   # key: value (car:toyota, color: gray)
	responseObject['statusCode'] = 200
	responseObject['headers'] = {}
	responseObject['headers']['Content-Type'] = 'application/json'
	responseObject['body'] = json.dumps(purchaseResponse)
    
    #Step 4: Send email confirmation with SES
	orderPlacementText='Hello, your order is placed successfully. We will ship your item as soon as possible, thank you for your business.'
	ses.send_email( Source=FROM_EMAIL_ADDRESS,
        Destination={ 'ToAddresses': [customerEmail] }, 
        Message={ 'Subject': {'Data': 'Your order is placed.'},
            'Body': {'Text': {'Data': orderPlacementText}}
        }
    )
	
	#Step 5: Return the response object
	return responseObject

#https://9xjtn90vx0.execute-api.us-east-1.amazonaws.com/dev?purchaseId=3423&item=iphone&amount=1100&email=yavuz7141@hotmail.com

# queryStringParameters > ?purchaseId=3423&item=iphone&amount=1100&email=yavuz7141@hotmail.com